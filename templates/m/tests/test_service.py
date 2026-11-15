"""Exercise the service with an isolated temporary JSON file."""

import pytest

from example_app.service import add_task
from example_app.storage import load_tasks


def test_add_task(tmp_path) -> None:
    path = tmp_path / "tasks.json"
    assert add_task(path, " Review PCB ") == ["Review PCB"]
    assert add_task(path, "Build enclosure") == ["Review PCB", "Build enclosure"]
    assert load_tasks(path) == ["Review PCB", "Build enclosure"]


def test_invalid_json_is_reported(tmp_path) -> None:
    path = tmp_path / "tasks.json"
    path.write_text('{"not":"a list"}', encoding="utf-8")
    with pytest.raises(ValueError, match="list"):
        add_task(path, "Review PCB")
