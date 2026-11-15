"""Exercise the small script without third-party test dependencies."""

import tempfile
import unittest
from pathlib import Path

from main import count_nonempty_lines


class TestCountLines(unittest.TestCase):
    """Check the script's principal behavior."""

    def test_count_nonempty_lines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.txt"
            path.write_text("one\n\n two \n   \n", encoding="utf-8")
            self.assertEqual(count_nonempty_lines(path), 2)

    def test_missing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            count_nonempty_lines(Path("this-file-should-not-exist.txt"))


if __name__ == "__main__":
    unittest.main()
