"""Read-only document checks against the shared schema; never rewrite or publish."""
from __future__ import annotations
import argparse, datetime, json, re, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker

DISPLAY={'README.md','posts/2026/posts-toy-reference.md'}
CONFIG={'posts/_wordpress/trigger.md','intake/sources.md','intake/llm-context.md','intake/gpt.md'}
class UniqueLoader(yaml.SafeLoader):pass

def unique_mapping(loader,node,deep=False):
    out={}
    for key_node,value_node in node.value:
        key=loader.construct_object(key_node,deep=deep)
        if key in out:raise ValueError(f'duplicate YAML key: {key}')
        out[key]=loader.construct_object(value_node,deep=deep)
    return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique_mapping)

def plain(value):
    if isinstance(value,(datetime.date,datetime.datetime)):return value.isoformat()
    if isinstance(value,dict):return {str(k):plain(v) for k,v in value.items()}
    if isinstance(value,list):return [plain(v) for v in value]
    return value

def read_metadata(path):
    text=path.read_text(encoding='utf-8').lstrip('\ufeff')
    m=re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
    if not m:raise ValueError('missing frontmatter')
    data=yaml.load(m[1],Loader=UniqueLoader)
    if not isinstance(data,dict):raise ValueError('frontmatter must be a mapping')
    return plain(data)

def eligible(path,root,repo):
    rel=path.relative_to(root)
    if any(part.startswith('.') for part in rel.parts):return False
    if path.name.lower() in {'index.md','index.html'}:return False
    if repo=='devlog' and rel.as_posix() in DISPLAY|CONFIG:return False
    return path.suffix.lower()=='.md'

def check(root,schema_path,repo='devlog',reference_roots=()):
    schema=json.loads(schema_path.read_text(encoding='utf-8'))
    validator=Draft202012Validator(schema,format_checker=FormatChecker())
    errors=[];warnings=[];documents=[];ids={};registry=set()
    for folder in [root,*reference_roots]:
        for p in folder.rglob('*.md'):
            if any(x.startswith('.') for x in p.relative_to(folder).parts):continue
            try:meta=read_metadata(p)
            except (ValueError,yaml.YAMLError):continue
            if meta.get('id'):registry.add(meta['id'])
            registry.update(meta.get('aliases') or [])
    for p in sorted(root.rglob('*.md')):
        if not eligible(p,root,repo):continue
        rel=p.relative_to(root).as_posix()
        try:meta=read_metadata(p)
        except (ValueError,yaml.YAMLError) as exc:errors.append(f'{rel}: {exc}');continue
        documents.append(rel)
        for err in validator.iter_errors(meta):errors.append(f'{rel}: {".".join(map(str,err.path))}: {err.message}')
        ident=meta.get('id')
        if ident:
            if ident in ids:errors.append(f'{rel}: duplicate id also in {ids[ident]}')
            ids[ident]=rel
            if p.stem!=ident and meta.get('filename_policy') not in {'entrypoint','stable-link'}:
                errors.append(f'{rel}: filename must match id, or record a path exception')
        if meta.get('created') and meta.get('updated') and meta['updated']<meta['created']:
            errors.append(f'{rel}: updated precedes created')
        for key in ['parents','related']:
            for ident in meta.get(key,[]) if isinstance(meta.get(key),list) else []:
                if ident not in registry:warnings.append(f'{rel}: unresolved {key}: {ident}')
        if meta.get('status') in {'active','publish','published'} and meta.get('visibility')=='private':
            warnings.append(f'{rel}: index status and intended visibility differ; no access control is implied')
    return {'documents':len(documents),'errors':errors,'warnings':warnings}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path('.'));ap.add_argument('--schema',type=Path,required=True)
    ap.add_argument('--repo',choices=['devlog','spec','assets'],default='devlog');ap.add_argument('--references',type=Path,action='append',default=[])
    ap.add_argument('--json',type=Path);a=ap.parse_args()
    result=check(a.root.resolve(),a.schema.resolve(),a.repo,[p.resolve() for p in a.references])
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if a.json:a.json.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return bool(result['errors'])
if __name__=='__main__':sys.exit(main())
