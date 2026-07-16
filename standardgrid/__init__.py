"""
standardgrid

A Python library for generating official spatial reference grids.
"""

from .grid import Grid

from .standards import (
    GridStandard,
    get_standard,
    available_standards,
    standards,
)

__version__ = "1.0.0"

__all__ = [
    "Grid",
    "GridStandard",
    "get_standard",
    "available_standards",
    "standards",
]