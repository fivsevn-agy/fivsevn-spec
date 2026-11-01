from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from media_naming import media_filename, check
from site_post_metadata import normalize_metadata, dump_frontmatter

class MediaNamingTests(unittest.TestCase):
    def test_same_instant_and_identity_is_stable_across_timezones(self):
        self.assertEqual(media_filename('stills','album','2026-12-31T16:00:00Z',1,'.JPEG'),
                         media_filename('stills','album','2027-01-01T00:00:00+08:00',1,'.jpg'))
        self.assertRegex(media_filename('stills','album','2026-12-31T16:00:00Z',1,'.JPEG'),
                         r'^20270101-000000-stills-[a-f0-9]{12}-001\.jpg$')
    def test_same_second_posts_and_boards_have_distinct_names(self):
        stamp='2026-11-01T14:00:00+08:00'
        names={media_filename(board,ident,stamp,1,'.webp') for board in ['flux','savour','fieldlog','stills','motion'] for ident in ['a','b']}
        self.assertEqual(10,len(names))
        self.assertTrue(media_filename('stills','a',stamp,1000,'.png').endswith('-1000.png'))
    def test_requires_evidenced_time_positive_number_and_safe_identity(self):
        for board,ident,stamp,number in [('stills','../a','2026-11-01T14:00:00Z',1),('stills','a','2026-11-01T14:00:00',1),('stills','a','2026-11-01T14:00:00Z',0)]:
            with self.assertRaises(ValueError):media_filename(board,ident,stamp,number,'.jpg')
    def test_checker_rejects_unrenamed_image_and_duplicate_ordinals(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);folder=root/'2026/11/a';(folder/'assets').mkdir(parents=True)
            meta=normalize_metadata({'id':'a','date':'2026-11-01T14:00:00Z'},site='flux')
            (folder/'index.md').write_text(dump_frontmatter(meta))
            path=folder/'assets/IMG_1234.jpg';path.write_bytes(b'photo')
            with self.assertRaises(ValueError):check(root,'flux')
            name=media_filename('flux','a',meta['extra']['published_at'],1,'.jpg');path.rename(folder/'assets'/name)
            self.assertEqual(1,check(root,'flux'))
            (folder/'assets'/name.replace('.jpg','.png')).write_bytes(b'other')
            with self.assertRaises(ValueError):check(root,'flux')

if __name__=='__main__':unittest.main()
