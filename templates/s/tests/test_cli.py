"""Test the installed CLI entry point."""

import subprocess
import sys


def test_entry_point() -> None:
    process = subprocess.run(
        [sys.executable, "-m", "example_cli.cli", "5", "0.02"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode == 0
    assert process.stdout.strip() == "0.1 W"


def test_invalid_value() -> None:
    process = subprocess.run(
        [sys.executable, "-m", "example_cli.cli", "-1", "2"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert process.returncode == 2
    assert "nonnegative" in process.stderr
