"""
standardgrid

A Python library for generating official spatial reference grids.
"""

from .grid import Grid

from .standards import (
    get_standard,
    available_standards,
)

__version__ = "0.5.0"