"""Check that generated README instructions match actual starter interfaces."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.create_project import _readme, create_project


class TestGeneratedReadmes(unittest.TestCase):
    """Verify proportionate French documentation and executable examples."""

    def test_xs_has_a_minimal_working_example(self) -> None:
        readme = _readme("line-counter", "xs")
        self.assertIn("Script Python autonome", readme)
        self.assertIn("uv run main.py README.md", readme)
        self.assertIn("unittest discover", readme)
        self.assertNotIn("uv.lock", readme)
        self.assertNotIn("pyproject.toml", readme)

    def test_s_instructions_match_package_entry_point(self) -> None:
        readme = _readme("sensor-cli", "s")
        self.assertIn("Python 3.12", readme)
        self.assertIn("uv sync --locked", readme)
        self.assertIn("uv run --locked sensor-cli 5 0.02", readme)
        self.assertIn("pytest -q", readme)
        self.assertIn("ruff format --check .", readme)
        self.assertNotIn(".env.example", readme)

    def test_m_instructions_match_package_entry_point(self) -> None:
        readme = _readme("task-manager", "m")
        self.assertIn('task-manager --file tasks.json "Review schematic"', readme)
        self.assertIn("uv build", readme)
        self.assertIn("gestion de tâches", readme)

    def test_without_lock_requires_generating_lock_first(self) -> None:
        readme = _readme("sensor-cli", "s", locked=False)
        self.assertIn("uv lock\nuv sync --locked", readme)

    def test_optional_configuration_is_described_without_false_claims(self) -> None:
        readme = _readme("sensor-cli", "s", with_env=True)
        self.assertIn("SENSOR_CLI_TIMEOUT_SECONDS", readme)
        self.assertIn("cp .env.example .env", readme)
        self.assertIn("uv run --env-file .env --locked sensor-cli --help", readme)
        self.assertIn("La CLI n'utilise pas", readme)

    def test_generated_project_has_french_readme_and_correct_version(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project("line-counter", "xs", Path(directory))
            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertTrue(readme.startswith("# line-counter"))
            self.assertIn("Script Python autonome", readme)
            self.assertIn("uv run main.py README.md", readme)
            marker = (root / ".project-python.toml").read_text(encoding="utf-8")
            self.assertIn('standards-version = "0.4.0"', marker)

    def test_s_without_ci_or_lock_documents_first_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project(
                "sensor-cli", "s", Path(directory), ci=False, lock=False
            )
            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertIn("uv lock\nuv sync --locked", readme)
            self.assertIn("uv run --locked sensor-cli 5 0.02", readme)


if __name__ == "__main__":
    unittest.main()
