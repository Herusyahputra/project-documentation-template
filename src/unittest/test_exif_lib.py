import sys
sys.path.append("..")

from exif_lib import MetaImage
import unittest


class TestExivlib(unittest.TestCase):
    comment = "Raspi"

    def test_modify_comment(self):
        img = MetaImage("../../SourceImage/image.jpg")
        img.modify_comment(self.comment)
        self.assertEqual(img.read_comment(), self.comment)
        print(">>> Test modify comment past")

    def test_read_comment(self):
        img = MetaImage("../../SourceImage/image.jpg")
        self.assertEqual(img.read_comment(), self.comment)
        print(">>> Test read comment past")

    def test_clear_comment(self):
        img = MetaImage("../../SourceImage/image.jpg")
        self.assertEqual(img.clear_comment(), None)
        print(">>> Test clear comment past")


if __name__ == "__main__":
    unittest.main()
