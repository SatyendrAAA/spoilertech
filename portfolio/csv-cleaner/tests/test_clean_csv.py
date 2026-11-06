import csv
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "clean_csv.py"


class CleanerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "input.csv"
        self.output = self.root / "output.csv"

    def run_cleaner(self, source=None, output=None):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(source or self.source), str(output or self.output)],
            capture_output=True, text=True, check=False,
        )

    def test_cleans_duplicates_blank_rows_and_quoted_values(self):
        self.source.write_text('\ufeff Name ,Note\n Alice ," hello, world "\nAlice,"hello, world"\n,\nBob,"two\nlines"\n', encoding="utf-8")
        result = self.run_cleaner()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("2 rows", result.stdout)
        self.assertIn("1 duplicates and 1 blank rows", result.stdout)
        with self.output.open(newline="", encoding="utf-8") as output:
            self.assertEqual(list(csv.reader(output)), [["Name", "Note"], ["Alice", "hello, world"], ["Bob", "two\nlines"]])

    def test_never_overwrites_existing_file_or_input(self):
        self.source.write_text("name\nAlice\n", encoding="utf-8")
        self.output.write_text("keep me", encoding="utf-8")
        self.assertNotEqual(self.run_cleaner().returncode, 0)
        self.assertEqual(self.output.read_text(encoding="utf-8"), "keep me")
        self.assertNotEqual(self.run_cleaner(output=self.source).returncode, 0)
        self.assertEqual(self.source.read_text(encoding="utf-8"), "name\nAlice\n")

    def test_bad_row_removes_incomplete_output(self):
        self.source.write_text("name,city\nAlice,Patna\nBob\n", encoding="utf-8")
        result = self.run_cleaner()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected 2", result.stderr)
        self.assertFalse(self.output.exists())

    def test_invalid_headers_and_empty_input(self):
        for content in ("", "name,Name\n", "name, \n"):
            with self.subTest(content=content):
                self.source.write_text(content, encoding="utf-8")
                self.assertNotEqual(self.run_cleaner().returncode, 0)
                self.assertFalse(self.output.exists())

    def test_invalid_utf8_removes_incomplete_output(self):
        self.source.write_bytes(b"name\nAlice\n\xff\n")
        self.assertNotEqual(self.run_cleaner().returncode, 0)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
