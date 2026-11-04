"""Shared site-post behavior: stable identity, explicit controls, and offline checks."""
from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import site_post_metadata as posts
import check_metadata


class SitePostTests(unittest.TestCase):
    def raw(self, **values):
        metadata = {"id": "old-stable-id", "date": "2026-07-15T09:08:24+08:00",
                    "title": "A saved observation", "image": "assets/original.jpg"}
        metadata.update(values)
        return metadata

    def normalize(self, site="fieldlog", **values):
        return posts.normalize_metadata(self.raw(**values), site=site)

    def test_defaults_preserve_id_instant_and_content_dates(self):
        raw = self.raw(created="2025-03-23", updated="2026-07-16", title="  ")
        before = deepcopy(raw)
        meta = posts.normalize_metadata(raw, site="fieldlog", post_id="old-stable-id",
                                        published_at="2030-01-01T00:00:00+08:00")
        posts.validate_metadata(meta, site="fieldlog", schema_dir=ROOT / "content")
        self.assertEqual(raw, before)
        self.assertEqual(meta["id"], "old-stable-id")
        self.assertEqual(meta["created"], "2025-03-23")
        self.assertEqual(meta["updated"], "2026-07-16")
        self.assertEqual(meta["extra"]["published_at"], raw["date"])
        self.assertEqual(meta["title"], "15 Jul, 2026 09:08")
        self.assertEqual(meta["extra"]["author"], "五月七日")
        self.assertEqual(meta["extra"]["observation_id"], "260715090824")
        self.assertEqual(meta["extra"]["display_status"], "Archived")
        self.assertEqual((meta["module"], meta["submodule"]), ("natsci", "fieldlog"))
        self.assertNotIn("date", meta)
        self.assertNotIn("image", meta)

    def test_repeat_normalization_is_identical_on_a_later_day(self):
        canonical = self.normalize()
        canonical["metadata_updated"] = "2026-10-01"
        class LaterDatetime(datetime):
            @classmethod
            def now(cls, tz=None):
                return cls(2035, 1, 1, tzinfo=tz)
        with patch.object(posts, "datetime", LaterDatetime):
            self.assertEqual(posts.normalize_metadata(canonical, site="fieldlog"), canonical)
        self.assertEqual(posts.dump_frontmatter(canonical), posts.dump_frontmatter(deepcopy(canonical)))

    def test_explicit_controls_never_default_to_publication(self):
        for status in ["draft", "hidden", "private", "archive", "archived"]:
            with self.subTest(status=status):
                meta = self.normalize(status=status, visibility="public", image=None)
                posts.validate_metadata(meta, site="fieldlog")
                self.assertEqual(meta["status"], status)
                self.assertFalse(posts.is_published(meta))
        for visibility in ["internal", "private"]:
            meta = self.normalize(status="published", visibility=visibility, image=None)
            posts.validate_metadata(meta)
            self.assertEqual(meta["visibility"], visibility)
            self.assertFalse(posts.is_published(meta))
        for status in ["active", "publish", "published"]:
            self.assertTrue(posts.is_published(self.normalize(status=status)))
        with self.assertRaises(ValueError):
            posts.validate_metadata(self.normalize(status="pending"))

    def test_runtime_and_unknown_fields_survive_without_returning_to_canonical_top_level(self):
        raw = self.raw(source="wordpress-live", sync="manual", upload={"path": "trigger_imgs/a.jpg", "sha256": "abc"},
                       wp_post_id=4259, wp_slug="old-slug", source_key="a stable import key", publish_slug="fixed-url",
                       published=False, arbitrary={"nested": [1, 2]},
                       extra={"image": "assets/new.jpg", "custom": {"x": True}})
        meta = posts.normalize_metadata(raw, site="fieldlog")
        posts.validate_metadata(meta)
        view = posts.metadata_view(meta)
        for key in ["source", "sync", "upload", "wp_post_id", "wp_slug", "source_key", "publish_slug", "arbitrary"]:
            self.assertEqual(view[key], raw[key])
            self.assertNotIn(key, meta)
        self.assertEqual(meta["legacy"]["metadata"]["published"], False)
        self.assertEqual(meta["legacy"]["metadata"]["image"], "assets/original.jpg")
        self.assertEqual(view["image"], "assets/new.jpg")
        self.assertEqual(view["archive_status"], "Archived")
        self.assertEqual(view["date"], raw["date"])
        self.assertEqual(meta["extra"]["custom"], {"x": True})
        self.assertEqual(posts.normalize_metadata(meta, site="fieldlog"), meta)
        with self.assertRaisesRegex(ValueError, "Only canonical"):
            posts.dump_frontmatter(view)

    def test_timezone_and_site_mapping_and_invalid_identity(self):
        meta = self.normalize(site="savour", date="2026-01-01T00:30:00+14:00", title="")
        self.assertEqual(meta["title"], "31 Dec, 2025 18:30")
        self.assertEqual((meta["module"], meta["submodule"]), ("savour", "2025"))
        posts.validate_metadata(meta, site="savour")
        self.assertIsNotNone(posts.published_datetime(meta).utcoffset())
        with self.assertRaises(ValueError):
            posts.validate_metadata(meta, site="flux")
        with self.assertRaisesRegex(ValueError, "refusing to rename"):
            posts.normalize_metadata(self.raw(), site="fieldlog", post_id="new-id")
        for date in ["2026-07-15", "2026-07-15T09:08:24", None]:
            with self.subTest(date=date), self.assertRaises(ValueError):
                self.normalize(date=date)

    def test_primary_images_required_only_for_formal_single_image_sites(self):
        for site in ["savour", "fieldlog"]:
            with self.subTest(site=site), self.assertRaises(ValueError):
                posts.validate_metadata(self.normalize(site=site, image=None), site=site)
        posts.validate_metadata(self.normalize(site="flux", image=None), site="flux")

    def test_store_boards_keep_identity_and_require_video_metadata_only_for_cctv(self):
        system_log = self.normalize(site="sys", image=None)
        posts.validate_metadata(system_log, site="sys")
        self.assertEqual((system_log["module"], system_log["submodule"], system_log["source_of_truth"]),
                         ("57store", "sys", "site"))
        self.assertNotIn("image", system_log["extra"])
        with self.assertRaisesRegex(ValueError, "video_ids"):
            posts.validate_metadata(self.normalize(site="cctv", image=None), site="cctv")
        video = self.normalize(site="cctv", image=None, extra={"video_ids": ["AbCdEf123_-"]})
        posts.validate_metadata(video, site="cctv")
        self.assertEqual((video["module"], video["submodule"], video["source_of_truth"]),
                         ("57store", "cctv", "site"))
        for identifiers in [[], ["short"], ["contains space"]]:
            invalid = deepcopy(video)
            invalid["extra"]["video_ids"] = identifiers
            with self.subTest(video_ids=identifiers), self.assertRaises(ValueError):
                posts.validate_metadata(invalid, site="cctv")
        with self.assertRaisesRegex(ValueError, "Site identity"):
            posts.validate_metadata(video, site="sys")

    def test_store_package_roots_and_authoritative_cli_use_plain_stable_id(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for board in ["sys", "cctv"]:
                with self.subTest(board=board):
                    data = self.raw(image=None, date="2026-12-31T17:00:00Z",
                                    extra={"video_ids": ["AbCdEf123_-"]} if board == "cctv" else {})
                    meta = posts.normalize_metadata(data, site=board)
                    package = root / board / "2027/01/old-stable-id"
                    package.mkdir(parents=True)
                    (package / "index.md").write_text(posts.dump_frontmatter(meta) + "Saved text\n")
                    result = posts.check_packages(root / board, site=board, schema_dir=ROOT / "content")
                    self.assertEqual((result["documents"], result["errors"]), (1, []))
                    args = ["check_metadata.py", "--profile", "site-post-v1", "--site", board,
                            "--root", str(root), "--content-root", board,
                            "--schema", str(ROOT / "content/content-metadata.schema.json")]
                    with patch.object(sys, "argv", args):
                        self.assertEqual(check_metadata.main(), 0)
                    package.rename(package.with_name("2027-01-01-010000-old-stable-id"))
                    result = posts.check_packages(root / board, site=board, schema_dir=ROOT / "content")
                    self.assertEqual(len(result["errors"]), 1)

    def test_frontmatter_roundtrip_preserves_body_and_rejects_duplicate_or_unclosed_yaml(self):
        canonical = self.normalize()
        body = "\n**Caption**\n\n    code\n\n"
        text = posts.dump_frontmatter(canonical) + body
        meta, preserved = posts.read_frontmatter(text)
        self.assertEqual(meta, canonical)
        self.assertEqual(preserved, body)
        self.assertEqual(posts.read_frontmatter("Free-form trigger\n"), ({}, "Free-form trigger\n"))
        self.assertEqual(posts.read_frontmatter("---\n---\nBody"), ({}, "Body"))
        for bad in ["---\nid: one\nid: two\n---\n", "---\nid: unclosed\n"]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                posts.read_frontmatter(bad)

    def test_explicit_profile_checks_saved_index_packages_and_ignores_triggers(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / "flux/2026/07/old-stable-id"
            folder.mkdir(parents=True)
            source = folder / "index.md"
            source.write_text(posts.dump_frontmatter(self.normalize(site="flux")) + "Body\n")
            trigger = root / "flux/trigger_imgs"
            trigger.mkdir()
            (trigger / "README.md").write_text("An uploader guide, not a post")
            (root / "flux/index.md").write_text("An ordinary display index")
            result = check_metadata.check(root, ROOT / "content/content-metadata.schema.json",
                                          profile="site-post-v1", content_root="flux", site="flux")
            self.assertEqual(result["documents"], 1)
            self.assertEqual(result["errors"], [])
            source.write_text(source.read_text().replace("visibility: public", "visibility: invalid"))
            result = posts.check_packages(root / "flux", site="flux", schema_dir=ROOT / "content")
            self.assertEqual(result["documents"], 1)
            self.assertEqual(len(result["errors"]), 1)

    def test_cli_normalization_preserves_body_and_prevalidates_the_entire_batch(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "2026/07/old-stable-id/index.md"
            second = root / "2026/07/invalid-id/index.md"
            first.parent.mkdir(parents=True)
            second.parent.mkdir(parents=True)
            body = "\nA caption with trailing lines.\n\n"
            first.write_text("---\n" + json.dumps(self.raw(site_note="kept")) + "\n---\n" + body)
            second.write_text("---\nid: invalid-id\n---\nMissing timestamp")
            before = first.read_bytes()
            args = ["site_post_metadata.py", "normalize", "--site", "flux", "--root", str(root),
                    "--schema-dir", str(ROOT / "content")]
            with patch.object(sys, "argv", args), self.assertRaises(ValueError):
                posts.main()
            self.assertEqual(first.read_bytes(), before)
            second.unlink()
            with patch.object(sys, "argv", args):
                self.assertEqual(posts.main(), 0)
            self.assertEqual(posts.read_frontmatter(first)[1], body)
            canonical_bytes = first.read_bytes()
            with patch.object(sys, "argv", args):
                self.assertEqual(posts.main(), 0)
            self.assertEqual(first.read_bytes(), canonical_bytes)

    def test_cli_normalization_rejects_package_errors_without_any_writes(self):
        batches = [
            ('flux', [
                ('2026/07/first', self.raw(id='first')),
                ('2026/07/last', self.raw(id='last', date='2026-06-15T09:08:24+08:00')),
            ], 'package directory'),
            ('flux', [
                ('2026/06/same-id', self.raw(id='same-id', date='2026-06-15T09:08:24+08:00')),
                ('2026/07/same-id', self.raw(id='same-id')),
            ], 'duplicate id'),
            ('motion', [
                ('2026/06/2026-06-15-090824-same-id', self.raw(
                    id='same-id', date='2026-06-15T09:08:24+08:00', extra={'video_ids': ['AbCdEf123_-']})),
                ('2026/07/2026-07-15-090824-same-id', self.raw(
                    id='same-id', extra={'video_ids': ['AbCdEf123_-']})),
            ], 'duplicate id'),
            ('stills', [
                ('bygone', self.raw(id='bygone', extra={
                    'mode': 'album', 'images': [{'file': 'assets/original.jpg'}]})),
            ], 'independent collection'),
        ]
        for site, packages, error in batches:
            with self.subTest(site=site, error=error), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                for relative, raw in packages:
                    source = root / relative / 'index.md'
                    source.parent.mkdir(parents=True)
                    source.write_text('---\n' + json.dumps(raw) + '\n---\nBody\n')
                before = {path: path.read_bytes() for path in root.rglob('index.md')}
                args = ['site_post_metadata.py', 'normalize', '--site', site, '--root', str(root),
                        '--schema-dir', str(ROOT / 'content')]
                with patch.object(sys, 'argv', args), \
                        patch.object(Path, 'write_text', side_effect=AssertionError('failed batch must not write')), \
                        self.assertRaisesRegex(ValueError, error):
                    posts.main()
                self.assertEqual({path: path.read_bytes() for path in before}, before)

    def test_cli_normalization_preserves_motion_and_bygone_package_rules(self):
        for site, relative, raw in [
            ('motion', '2027/01/2027-01-01-010000-old-stable-id', self.raw(
                date='2026-12-31T17:00:00Z', extra={'video_ids': ['AbCdEf123_-']})),
            ('stills', 'bygone', self.raw(id='bygone', extra={
                'mode': 'collection', 'images': [{'file': 'assets/original.jpg'}]})),
        ]:
            with self.subTest(site=site), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                source = root / relative / 'index.md'
                source.parent.mkdir(parents=True)
                body = '\nThe original caption.\n\n'
                source.write_text('---\n' + json.dumps(raw) + '\n---\n' + body)
                args = ['site_post_metadata.py', 'normalize', '--site', site, '--root', str(root),
                        '--schema-dir', str(ROOT / 'content')]
                with patch.object(sys, 'argv', args):
                    self.assertEqual(posts.main(), 0)
                self.assertEqual(posts.check_packages(root, site=site)['errors'], [])
                meta, preserved = posts.read_frontmatter(source)
                self.assertEqual((meta['id'], preserved), (raw['id'], body))


if __name__ == "__main__":
    unittest.main()
