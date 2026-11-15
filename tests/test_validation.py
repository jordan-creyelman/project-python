"""Verify that repository checks identify missing links and invalid syntax."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_repo import check_links, check_syntax, strip_fenced_blocks


class TestDocumentationValidation(unittest.TestCase):
    """Exercise the validation helpers with temporary sample files."""

    def test_existing_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text("[guide](guide.md)", encoding="utf-8")
            self.assertEqual(check_links(root), [])

    def test_missing_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[missing](absent.md)", encoding="utf-8")
            self.assertEqual(len(check_links(root)), 1)

    def test_external_links_are_not_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[official](https://docs.astral.sh/uv/)", encoding="utf-8"
            )
            self.assertEqual(check_links(root), [])

    def test_fenced_examples_are_skipped(self) -> None:
        text = "Keep [guide](here.md)\n\x60\x60\x60md\n[skip](missing.md)\n\x60\x60\x60"
        self.assertIn("[guide]", strip_fenced_blocks(text))
        self.assertNotIn("[skip]", strip_fenced_blocks(text))

    def test_invalid_yaml_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "invalid.yml").write_text("name: [not-closed\n", encoding="utf-8")
            self.assertTrue(any("YAML error" in error for error in check_syntax(root)))

    def test_invalid_python_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "bad.py").write_text("def broken(:\n", encoding="utf-8")
            self.assertTrue(
                any("Python error" in error for error in check_syntax(root))
            )


if __name__ == "__main__":
    unittest.main()
