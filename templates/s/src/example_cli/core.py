"""Calculate electrical power independently of the CLI."""

from __future__ import annotations

import math


def calculate_power(voltage_v: float, current_a: float) -> float:
    """Return power in watts from a voltage and a current in amperes."""
    if not all(math.isfinite(value) and value >= 0 for value in (voltage_v, current_a)):
        raise ValueError("Voltage and current must be finite and nonnegative.")
    power_w = voltage_v * current_a
    if not math.isfinite(power_w):
        raise ValueError("The calculated power cannot be represented.")
    return power_w
