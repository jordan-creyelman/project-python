"""Test safe validation of the standards release metadata."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_release import main, validate_release


class TestReleaseMetadata(unittest.TestCase):
    """Check version agreement without creating remote releases."""

    def _fixture(self, directory: str, *, version: str = "0.2.0") -> Path:
        """Write the minimum useful release metadata for a test."""
        root = Path(directory)
        (root / "VERSION").write_text(version + "\n", encoding="utf-8")
        (root / "CHANGELOG.md").write_text(
            "# Changelog\n\n## [Unreleased]\n\n"
            "## [0.2.0] - 2026-11-15\n\n### Added\n- Project generator\n\n"
            "## [0.1.0] - 2026-11-15\n- Initial rules\n",
            encoding="utf-8",
        )
        return root

    def test_valid_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            version, notes = validate_release(root, "0.2.0")
            self.assertEqual(version, "0.2.0")
            self.assertIn("Project generator", notes)
            self.assertNotIn("Initial rules", notes)

    def test_mismatch_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            with self.assertRaisesRegex(ValueError, "Requested version"):
                validate_release(root, "0.3.0")

    def test_invalid_version_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory, version="not-semver")
            with self.assertRaisesRegex(ValueError, "MAJOR.MINOR.PATCH"):
                validate_release(root)

    def test_missing_release_notes_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            (root / "CHANGELOG.md").write_text(
                "# Changelog\n\n## [0.2.0] - 2026-11-15\n\n### Added\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "substantive"):
                validate_release(root)

    def test_notes_file_created_only_after_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = self._fixture(directory)
            notes_file = root / "notes.md"
            self.assertEqual(
                main(
                    [
                        "--path",
                        str(root),
                        "--version",
                        "0.2.0",
                        "--notes-file",
                        str(notes_file),
                    ]
                ),
                0,
            )
            self.assertIn("Project generator", notes_file.read_text())


if __name__ == "__main__":
    unittest.main()
