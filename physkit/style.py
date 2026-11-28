"""Unified visual styling and reusable vector icons matched to the lab brand."""

import matplotlib.pyplot as plt
from matplotlib.path import Path

# Brand palette sampled from In Silico Physics Lab logo
NAVY = "#0B1F3A"
TEAL = "#1C939A"
GOLD = "#D97706"
SLATE = "#64748B"
LIGHT_BG = "#F8FAFC"


def apply_lab_style() -> None:
    """Apply clean, publication-grade Matplotlib defaults across all simulations."""
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": LIGHT_BG,
            "axes.edgecolor": "#CBD5E1",
            "axes.linewidth": 1.0,
            "axes.titlesize": 11,
            "axes.titleweight": "bold",
            "axes.titlecolor": NAVY,
            "axes.labelsize": 10,
            "axes.labelcolor": NAVY,
            "xtick.color": SLATE,
            "ytick.color": SLATE,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "grid.color": "#E2E8F0",
            "grid.linestyle": "--",
            "grid.linewidth": 0.8,
            "legend.frameon": True,
            "legend.facecolor": "white",
            "legend.edgecolor": "#E2E8F0",
            "legend.fontsize": 8.5,
            "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
        }
    )


def get_hammer_marker() -> Path:
    """Return a reusable vector Path icon representing a hammer."""
    vertices = [
        # Handle
        (-0.12, -1.00),
        (0.12, -1.00),
        (0.12, 0.35),
        (-0.12, 0.35),
        (-0.12, -1.00),
        # Hammer head
        (-0.65, 0.35),
        (0.65, 0.35),
        (0.65, 0.85),
        (-0.65, 0.85),
        (-0.65, 0.35),
    ]
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    return Path(vertices, codes)


def get_feather_marker() -> Path:
    """Return a reusable vector Path icon representing a feather."""
    vertices = [
        (-0.75, -0.75),  # Quill tip
        (-0.35, -0.35),
        (-0.45, 0.15),
        (-0.05, 0.65),
        (0.65, 0.85),    # Feather tip
        (0.55, 0.25),
        (0.20, -0.10),
        (-0.20, -0.30),
        (-0.75, -0.75),
    ]
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    return Path(vertices, codes)