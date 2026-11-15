"""Cover task title validation independently of storage."""

import pytest

from example_app.domain import normalize_title


def test_normalize_title() -> None:
    assert normalize_title("  Read datasheet ") == "Read datasheet"


def test_blank_title_is_rejected() -> None:
    with pytest.raises(ValueError, match="empty"):
        normalize_title("   ")
