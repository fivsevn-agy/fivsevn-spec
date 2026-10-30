"""Read-only shared metadata validation; never rewrite sources or publish content."""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

DISPLAY = {"README.md", "posts/2026/posts-toy-reference.md"}
CONFIG = {
    "posts/_wordpress/trigger.md", "posts/_flux/trigger.md", "intake/sources.md",
    "intake/llm-context.md", "intake/gpt.md",
}


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently keeping the last value."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def plain(value: Any) -> Any:
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(key): plain(item) for key, item in value.items()}
    if isinstance(value, list):
        return [plain(item) for item in value]
    return value


def read_metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8").lstrip("\ufeff")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("missing or unclosed frontmatter")
    metadata = yaml.load(match[1], Loader=UniqueLoader)
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return plain(metadata)


def eligible(path: Path, root: Path, repo: str) -> bool:
    relative = path.relative_to(root)
    if any(part.startswith(".") for part in relative.parts):
        return False
    if path.name.lower() in {"index.md", "index.html"}:
        return False
    if repo == "devlog" and relative.as_posix() in DISPLAY | CONFIG:
        return False
    return path.suffix.lower() == ".md"


def pending_draft(path: Path, root: Path, repo: str) -> bool:
    """Raw first-level drafts are intentionally completed by the existing draft task."""
    relative = path.relative_to(root)
    if repo != "devlog" or len(relative.parts) != 3:
        return False
    if relative.parts[0] not in {"posts", "natsci", "netcom"} or relative.parts[1] != "_drafts":
        return False
    if path.name.startswith("TEMPLATE-"):
        return True
    text = path.read_text(encoding="utf-8")
    return not text.startswith(("---\n", "---\r\n"))


def check(root: Path, schema_path: Path, repo="devlog", reference_roots=(), *,
          profile=None, content_root=None, site=None) -> dict:
    if profile is not None:
        if profile != "site-post-v1":
            raise ValueError(f"Unknown metadata profile: {profile}")
        from site_post_metadata import check_packages
        folder = Path(content_root) if content_root is not None else root
        if not folder.is_absolute():
            folder = root / folder
        return check_packages(folder, site=site, schema_dir=schema_path.parent)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors, warnings, documents, pending = [], [], [], []
    ids, registry = {}, set()
    for folder in [root, *reference_roots]:
        for path in folder.rglob("*.md"):
            if any(part.startswith(".") for part in path.relative_to(folder).parts):
                continue
            try:
                metadata = read_metadata(path)
            except (ValueError, TypeError, yaml.YAMLError):
                continue
            if isinstance(metadata.get("id"), str):
                registry.add(metadata["id"])
            aliases = metadata.get("aliases", [])
            if isinstance(aliases, list):
                registry.update(value for value in aliases if isinstance(value, str))

    for path in sorted(root.rglob("*.md")):
        if not eligible(path, root, repo):
            continue
        relative = path.relative_to(root).as_posix()
        if pending_draft(path, root, repo):
            pending.append(relative)
            continue
        try:
            metadata = read_metadata(path)
        except (ValueError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{relative}: {error}")
            continue
        documents.append(relative)
        invalid = list(validator.iter_errors(metadata))
        for error in invalid:
            location = ".".join(map(str, error.path))
            errors.append(f"{relative}: {location}: {error.message}")
        if invalid:
            continue
        ident = metadata["id"]
        if ident in ids:
            errors.append(f"{relative}: duplicate id also in {ids[ident]}")
        ids[ident] = relative
        if path.stem != ident and metadata.get("filename_policy") not in {"entrypoint", "stable-link"}:
            errors.append(f"{relative}: filename must match id, or record a path exception")
        if metadata.get("filename_policy") == "stable-link" and not metadata.get("note"):
            errors.append(f"{relative}: explain the stable-link exception in note")
        if metadata.get("created") and metadata.get("updated") and metadata["updated"] < metadata["created"]:
            errors.append(f"{relative}: updated precedes created")
        for field in ["parents", "related"]:
            for target in metadata[field]:
                if target not in registry:
                    warnings.append(f"{relative}: unresolved {field}: {target}")
        if metadata["status"] in {"active", "publish", "published"} and metadata["visibility"] == "private":
            warnings.append(f"{relative}: index status and intended visibility differ; metadata is not access control")
    return {"documents": len(documents), "pending_drafts": pending, "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--repo", choices=["devlog", "spec", "assets"], default="devlog")
    parser.add_argument("--references", type=Path, action="append", default=[])
    parser.add_argument("--json", type=Path)
    parser.add_argument("--profile", choices=["site-post-v1"],
                        help="Explicitly validate saved post-package index.md files")
    parser.add_argument("--content-root", type=Path,
                        help="Package root relative to --root, or an absolute path")
    parser.add_argument("--site", choices=["flux", "savour", "fieldlog"],
                        help="Enforce the site's module/submodule mapping with --profile")
    args = parser.parse_args()
    if (args.content_root is not None or args.site is not None) and args.profile is None:
        parser.error("--content-root and --site require --profile")
    result = check(args.root.resolve(), args.schema.resolve(), args.repo, [p.resolve() for p in args.references],
                   profile=args.profile, content_root=args.content_root, site=args.site)
    output = json.dumps(result, ensure_ascii=False, indent=2)
    print(output)
    if args.json:
        args.json.write_text(output + "\n", encoding="utf-8")
    return int(bool(result["errors"]))


if __name__ == "__main__":
    sys.exit(main())
