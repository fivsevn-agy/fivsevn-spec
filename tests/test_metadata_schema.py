"""Shared schema checks; no external requests or writes to document sources."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import check_metadata as check

class SchemaTests(unittest.TestCase):
    def test_schema_is_valid(self):
        Draft202012Validator.check_schema(json.loads((ROOT / 'content/content-metadata.schema.json').read_text()))

    def test_duplicate_yaml_keys_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'x.md'
            path.write_text('---\nid: x\nid: y\n---\n')
            with self.assertRaises(ValueError):
                check.read_metadata(path)

    def test_display_and_configuration_exemptions(self):
        for name in ['README.md', 'now/index.md', 'intake/index.html', 'intake/sources.md', 'posts/_wordpress/trigger.md', 'posts/_flux/trigger.md', 'posts/2026/posts-toy-reference.md',
                     'posts/index.md', 'posts/ai-discourse-analysis/index.md', 'posts/2026/11/index.md',
                     'posts/2026/11/assets/index.md', 'posts/2026/11/_drafts/index.md',
                     'natsci/fieldlog/2026/11/observation/index.md']:
            self.assertFalse(check.eligible(ROOT / name, ROOT, 'devlog'))
        self.assertTrue(check.eligible(ROOT / 'posts/README.md', ROOT, 'devlog'))
        for name in ['posts/2026/11/an-article/index.md',
                     'posts/ai-discourse-analysis/2026/11/004-a-case/index.md']:
            self.assertTrue(check.eligible(ROOT / name, ROOT, 'devlog'))
            self.assertFalse(check.eligible(ROOT / name, ROOT, 'spec'))

    def long_form_metadata(self, ident):
        meta = check.read_metadata(ROOT / 'README.md')
        meta.update(id=ident, module='posts', submodule='2026', type='article',
                    source_of_truth='devlog', created='2026-11-04', updated='2026-11-04')
        return meta

    def write_metadata(self, root, relative, meta):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('---\n' + json.dumps(meta) + '\n---\nBody\n')
        return path

    def test_long_form_packages_receive_core_metadata_and_date_checks(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            article = self.long_form_metadata('an-article')
            case = self.long_form_metadata('posts-ai-discourse-analysis-004')
            article_path = 'posts/2026/11/an-article/index.md'
            case_path = 'posts/ai-discourse-analysis/2026/11/004-a-case/index.md'
            self.write_metadata(root, article_path, article)
            self.write_metadata(root, case_path, case)
            result = check.check(root, ROOT / 'content/content-metadata.schema.json')
            self.assertEqual((result['documents'], result['errors']), (2, []))

            article['updated'] = '2020-01-01'
            del case['summary']
            self.write_metadata(root, article_path, article)
            self.write_metadata(root, case_path, case)
            result = check.check(root, ROOT / 'content/content-metadata.schema.json')
            self.assertEqual(result['documents'], 2)
            self.assertTrue(any(article_path in error and 'updated precedes created' in error
                                for error in result['errors']))
            self.assertTrue(any(case_path in error and "'summary' is a required property" in error
                                for error in result['errors']))

    def test_long_form_ids_share_the_regular_document_uniqueness_check(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            meta = self.long_form_metadata('same-identity')
            for relative in ['same-identity.md', 'posts/2026/11/article/index.md',
                             'posts/ai-discourse-analysis/2026/11/004-a-case/index.md']:
                self.write_metadata(root, relative, meta)
            result = check.check(root, ROOT / 'content/content-metadata.schema.json')
            self.assertEqual(result['documents'], 3)
            self.assertEqual(len(result['errors']), 2)
            self.assertTrue(all('duplicate id also in' in error for error in result['errors']))

    def test_generated_site_is_excluded_from_sources_and_relation_registry(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            article = self.long_form_metadata('an-article')
            article['related'] = ['generated-only-id']
            self.write_metadata(root, 'posts/2026/11/an-article/index.md', article)
            self.write_metadata(root, '_site/generated-only-id.md', self.long_form_metadata('generated-only-id'))
            generated = root / '_site/intake/llm-context.md'
            generated.parent.mkdir(parents=True)
            generated.write_text('Generated output without source frontmatter.\n')
            result = check.check(root, ROOT / 'content/content-metadata.schema.json')
            self.assertEqual((result['documents'], result['errors']), (1, []))
            self.assertEqual(result['warnings'], [
                'posts/2026/11/an-article/index.md: unresolved related: generated-only-id'])

    def test_current_spec_documents(self):
        result = check.check(ROOT, ROOT / 'content/content-metadata.schema.json', 'spec')
        self.assertEqual(result['errors'], [])

    def test_new_raw_draft_waits_for_existing_automation(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / 'posts/_drafts/随手写.md'
            path.parent.mkdir(parents=True)
            path.write_text('# QA: 游戏测试\n\n原稿\n')
            result = check.check(root, ROOT / 'content/content-metadata.schema.json')
            self.assertEqual(result['errors'], [])
            self.assertEqual(result['pending_drafts'], ['posts/_drafts/随手写.md'])

    def test_malformed_types_report_errors_without_crashing(self):
        for header in ['id: [not, scalar]', 'id: x\naliases: [one, {bad: shape}]', 'id: x\ncreated: []\nupdated: 5']:
            with self.subTest(header=header), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                (root / 'x.md').write_text('---\n' + header + '\n---\n')
                result = check.check(root, ROOT / 'content/content-metadata.schema.json')
                self.assertTrue(result['errors'])

    def test_unclosed_draft_metadata_is_not_pending(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / 'posts/_drafts/x.md'
            path.parent.mkdir(parents=True)
            path.write_text('---\nid: x\n')
            result = check.check(root, ROOT / 'content/content-metadata.schema.json')
            self.assertTrue(result['errors'])
            self.assertEqual(result['pending_drafts'], [])

if __name__ == '__main__':
    unittest.main()
