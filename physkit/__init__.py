"""Reusable graphics, vector icons, and numerical solvers for In Silico Physics Lab."""

from .style import (
    NAVY,
    TEAL,
    GOLD,
    SLATE,
    LIGHT_BG,
    apply_lab_style,
    get_hammer_marker,
    get_feather_marker,
)
from .integrators import simulate_vertical_fall

__all__ = [
    "NAVY",
    "TEAL",
    "GOLD",
    "SLATE",
    "LIGHT_BG",
    "apply_lab_style",
    "get_hammer_marker",
    "get_feather_marker",
    "simulate_vertical_fall",
]