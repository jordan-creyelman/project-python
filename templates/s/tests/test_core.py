"""Verify normal, invalid, and extreme electrical inputs."""

import pytest

from example_cli.core import calculate_power


def test_calculate_power() -> None:
    assert calculate_power(5, 0.02) == pytest.approx(0.1)


@pytest.mark.parametrize("values", [(-1, 1), (1, -1), (float("inf"), 1), (1e308, 1e308)])
def test_invalid_power(values: tuple[float, float]) -> None:
    with pytest.raises(ValueError):
        calculate_power(*values)
