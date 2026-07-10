"""Validation helpers for depth-indexed calculation inputs."""

from __future__ import annotations

import math
from typing import Iterable, List


class ValidationError(ValueError):
    """Raised when an input cannot be used for a calculation."""


def as_float_list(values: Iterable[float], name: str) -> List[float]:
    result = [float(value) for value in values]
    if not result:
        raise ValidationError(f"{name} must contain at least one value")
    for index, value in enumerate(result):
        if not math.isfinite(value):
            raise ValidationError(f"{name}[{index}] must be finite")
    return result


def require_same_length(left: List[float], right: List[float], left_name: str, right_name: str) -> None:
    if len(left) != len(right):
        raise ValidationError(
            f"{left_name} and {right_name} must have the same length "
            f"({len(left)} != {len(right)})"
        )


def validate_strictly_increasing(values: Iterable[float], name: str = "depth") -> List[float]:
    result = as_float_list(values, name)
    for index in range(1, len(result)):
        if result[index] <= result[index - 1]:
            raise ValidationError(
                f"{name} must be strictly increasing at index {index}: "
                f"{result[index - 1]} -> {result[index]}"
            )
    return result


def validate_positive(values: Iterable[float], name: str) -> List[float]:
    result = as_float_list(values, name)
    for index, value in enumerate(result):
        if value <= 0:
            raise ValidationError(f"{name}[{index}] must be positive")
    return result


def validate_non_negative(values: Iterable[float], name: str) -> List[float]:
    result = as_float_list(values, name)
    for index, value in enumerate(result):
        if value < 0:
            raise ValidationError(f"{name}[{index}] must be non-negative")
    return result


def validate_biot_coefficient(alpha: float) -> float:
    alpha = float(alpha)
    if not math.isfinite(alpha) or alpha < 0.0 or alpha > 1.0:
        raise ValidationError("Biot coefficient must be finite and between 0 and 1")
    return alpha
