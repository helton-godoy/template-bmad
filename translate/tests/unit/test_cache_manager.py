import unittest
from pathlib import Path
import os
import shutil
from translate.cache.cache_manager import TranslationCache

class TestTranslationCache(unittest.TestCase):
    def setUp(self):
        self.test_cache_file = "translate/cache/test_hash_tracker.json"
        self.cache = TranslationCache(cache_file=self.test_cache_file)
        self.test_dir = Path("test_files")
        self.test_dir.mkdir(exist_ok=True)

    def tearDown(self):
        if Path(self.test_cache_file).exists():
            Path(self.test_cache_file).unlink()
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_get_file_hash_success(self):
        test_file = self.test_dir / "test.md"
        test_file.write_text("hello world")
        file_hash = self.cache.get_file_hash(str(test_file))
        self.assertNotEqual(file_hash, "")
        self.assertEqual(len(file_hash), 32) # MD5 hexdigest length

    def test_get_file_hash_failure(self):
        # File does not exist
        file_hash = self.cache.get_file_hash("non_existent_file.md")
        self.assertEqual(file_hash, "")

    def test_is_cached(self):
        test_file = self.test_dir / "test.md"
        test_file.write_text("hello world")

        self.assertFalse(self.cache.is_cached(str(test_file)))

        self.cache.mark_translated(str(test_file))
        self.assertTrue(self.cache.is_cached(str(test_file)))

        # Change file content
        test_file.write_text("hello world modified")
        self.assertFalse(self.cache.is_cached(str(test_file)))

if __name__ == "__main__":
    unittest.main()
