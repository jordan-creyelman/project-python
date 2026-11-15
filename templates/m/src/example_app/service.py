"""Orchestrate task operations across domain and storage."""

from __future__ import annotations

from pathlib import Path

from example_app.domain import normalize_title
from example_app.storage import load_tasks, save_tasks


def add_task(path: Path, title: str) -> list[str]:
    """Add a validated task and persist the new task list."""
    normalized = normalize_title(title)
    tasks = load_tasks(path)
    tasks.append(normalized)
    save_tasks(path, tasks)
    return tasks
