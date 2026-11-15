"""Test deterministic project-convention checks."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_project import check_project, main


class TestProjectStandards(unittest.TestCase):
    """Cover size-aware standards and non-destructive failure handling."""

    def test_xs_accepts_a_single_script(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.py").write_text('print("hello")\n', encoding="utf-8")
            self.assertEqual(check_project(root, "xs"), [])

    def test_requires_size_without_marker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(check_project(Path(directory))[0].level, "error")

    def test_rejects_invalid_marker(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".project-python.toml").write_text(
                "[project-python\nsize = 's'\n", encoding="utf-8"
            )
            self.assertEqual(check_project(root)[0].level, "error")

    def test_s_reports_recommendations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.py").write_text('print("hi")\n', encoding="utf-8")
            (root / "README.md").write_text("Example\n", encoding="utf-8")
            (root / "pyproject.toml").write_text(
                '[project]\nname = "example"\nrequires-python = ">=3.12"\n',
                encoding="utf-8",
            )
            findings = check_project(root, "s")
            self.assertTrue(any(f.level == "warning" for f in findings))
            self.assertFalse(any(f.level == "error" for f in findings))
            self.assertEqual(main(["--path", str(root), "--size", "s", "--strict"]), 1)

    def test_m_requires_ci_and_lockfile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.py").write_text('print("hi")\n', encoding="utf-8")
            findings = check_project(root, "m")
            messages = " ".join(f.message for f in findings)
            self.assertIn("uv.lock", messages)
            self.assertIn("CI", messages)
            self.assertIn("pyproject.toml", messages)

    def test_invalid_python_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.py").write_text("def broken(:\n", encoding="utf-8")
            findings = check_project(root, "xs")
            self.assertTrue(any("Invalid Python" in f.message for f in findings))


if __name__ == "__main__":
    unittest.main()
