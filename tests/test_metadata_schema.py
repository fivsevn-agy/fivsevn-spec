"""Shared schema checks; no external requests or writes to document sources."""
import json, sys, tempfile, unittest
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import check_metadata as check
class SchemaTests(unittest.TestCase):
    def test_schema_is_valid(self):
        Draft202012Validator.check_schema(json.loads((ROOT/'content/content-metadata.schema.json').read_text()))
    def test_duplicate_yaml_keys_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.md';p.write_text('---\nid: x\nid: y\n---\n')
            with self.assertRaises(ValueError):check.read_metadata(p)
    def test_display_and_configuration_exemptions(self):
        for name in ['README.md','now/index.md','intake/index.html','intake/sources.md','posts/_wordpress/trigger.md','posts/2026/posts-toy-reference.md']:
            self.assertFalse(check.eligible(ROOT/name,ROOT,'devlog'))
        self.assertTrue(check.eligible(ROOT/'posts/README.md',ROOT,'devlog'))
    def test_current_spec_documents(self):
        result=check.check(ROOT,ROOT/'content/content-metadata.schema.json','spec')
        self.assertEqual(result['errors'],[])
if __name__=='__main__':unittest.main()
