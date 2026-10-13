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
        for name in ['README.md', 'now/index.md', 'intake/index.html', 'intake/sources.md', 'posts/_wordpress/trigger.md', 'posts/2026/posts-toy-reference.md']:
            self.assertFalse(check.eligible(ROOT / name, ROOT, 'devlog'))
        self.assertTrue(check.eligible(ROOT / 'posts/README.md', ROOT, 'devlog'))

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
