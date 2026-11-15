"""Test project creation and file-name transformations safely."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.create_project import create_project


class TestProjectGenerator(unittest.TestCase):
    """Ensure generation is predictable and does not overwrite projects."""

    def test_generate_xs_without_uv(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project("line-counter", "xs", Path(directory))
            self.assertTrue((root / "main.py").is_file())
            self.assertFalse((root / "pyproject.toml").exists())
            self.assertFalse((root / ".github").exists())
            self.assertIn('size = "xs"', (root / ".project-python.toml").read_text())

    def test_generate_s_with_renamed_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project(
                "sensor-cli", "s", Path(directory), ci=False, lock=False
            )
            self.assertTrue((root / "src" / "sensor_cli" / "core.py").exists())
            metadata = (root / "pyproject.toml").read_text()
            self.assertIn('name = "sensor-cli"', metadata)
            self.assertIn("sensor_cli.cli:main", metadata)
            tests = (root / "tests" / "test_core.py").read_text()
            self.assertIn("from sensor_cli.core import", tests)
            self.assertFalse((root / "uv.lock").exists())

    def test_generate_m_with_renamed_imports(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project(
                "task-manager", "m", Path(directory), ci=False, lock=False
            )
            service = (root / "src" / "task_manager" / "service.py").read_text()
            self.assertIn("from task_manager.domain import", service)
            self.assertIn("task-manager", (root / "README.md").read_text())

    def test_refuse_unsafe_name_without_writing_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            for name in ("../outside", "BadName", "a--b", ".", ""):
                with self.assertRaises(ValueError):
                    create_project(name, "xs", parent)
            self.assertEqual(list(parent.iterdir()), [])

    def test_refuse_existing_destination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            existing = parent / "my-script"
            existing.mkdir()
            sentinel = existing / "keep.txt"
            sentinel.write_text("preserve", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                create_project("my-script", "xs", parent)
            self.assertEqual(sentinel.read_text(), "preserve")

    def test_ci_cannot_be_enabled_without_lockfile(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaisesRegex(ValueError, "requires"),
        ):
            create_project("sensor-cli", "s", Path(directory), ci=True, lock=False)

    def test_lock_failure_leaves_no_partial_project(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with (
                patch("scripts.create_project.shutil.which", return_value="/bin/uv"),
                patch("scripts.create_project.subprocess.run") as lock,
            ):
                from subprocess import CalledProcessError

                lock.side_effect = CalledProcessError(
                    1, ["uv", "lock"], stderr="offline"
                )
                with self.assertRaisesRegex(RuntimeError, "offline"):
                    create_project("sensor-cli", "s", Path(directory))
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_default_s_generates_ci_and_lockfile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:

            def fake_lock(command, *, cwd, check, capture_output, text):
                self.assertEqual(command, ["uv", "lock"])
                Path(cwd, "uv.lock").write_text("version = 1\n", encoding="utf-8")

            with (
                patch("scripts.create_project.shutil.which", return_value="/bin/uv"),
                patch("scripts.create_project.subprocess.run", side_effect=fake_lock),
            ):
                root = create_project("sensor-cli", "s", Path(directory))
            self.assertTrue((root / "uv.lock").exists())
            self.assertTrue((root / ".github/workflows/python-ci.yml").exists())
            self.assertTrue((root / "scripts/check_project.py").exists())


if __name__ == "__main__":
    unittest.main()


    def test_opt_in_config_for_s_renames_prefix_and_tests(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project(
                "sensor-cli", "s", Path(directory),
                ci=False, lock=False, with_env=True,
            )
            config = (root / "src" / "sensor_cli" / "config.py").read_text()
            env_example = (root / ".env.example").read_text()
            test = (root / "tests" / "test_config.py").read_text()
            self.assertIn("SENSOR_CLI_TIMEOUT_SECONDS", config)
            self.assertIn("SENSOR_CLI_LOG_LEVEL=INFO", env_example)
            self.assertIn("from sensor_cli.config import", test)
            self.assertFalse((root / ".env").exists())
            self.assertIn(".env", (root / ".gitignore").read_text())

    def test_no_config_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project(
                "sensor-cli", "s", Path(directory), ci=False, lock=False
            )
            self.assertFalse((root / ".env.example").exists())
            self.assertFalse((root / "src" / "sensor_cli" / "config.py").exists())

    def test_opt_in_config_for_m(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = create_project(
                "task-manager", "m", Path(directory),
                ci=False, lock=False, with_env=True,
            )
            self.assertIn(
                "TASK_MANAGER_LOG_LEVEL",
                (root / "src" / "task_manager" / "config.py").read_text(),
            )
            self.assertIn(
                "from task_manager.config import",
                (root / "tests" / "test_config.py").read_text(),
            )

    def test_reject_environment_config_for_xs(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaisesRegex(ValueError, "S/M"),
        ):
            create_project("mini-script", "xs", Path(directory), with_env=True)
