"""
standardgrid.standards
======================

Definitions of supported official spatial reference grid standards.

Each standard defines:

- Official name
- Internal code
- Coordinate Reference System (CRS)
- Grid origin
- Coordinate units
- Supported grid resolutions

These definitions are immutable and used throughout the library.

Author
------
Pedro Monteiro & OpenAI

License
-------
MIT
"""

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class GridStandard:
    """
    Immutable definition of a spatial reference grid standard.
    """

    name: str
    code: str
    crs: str
    origin: Tuple[float, float]
    units: str
    resolutions: Tuple[float, ...]


# ---------------------------------------------------------------------
# C-Squares
# ---------------------------------------------------------------------

CSQUARES = GridStandard(
    name="C-Squares",
    code="csquares",
    crs="EPSG:4326",
    origin=(0.0, 0.0),
    units="degrees",
    resolutions=(
        10.0,
        5.0,
        1.0,
        0.5,
        0.1,
        0.05,
        0.01,
        0.005,
        0.001,
        0.0005,
        0.0001,
        0.00005,
        0.00001,
    ),
)


# ---------------------------------------------------------------------
# INSPIRE
# ---------------------------------------------------------------------

INSPIRE = GridStandard(
    name="INSPIRE",
    code="inspire",
    crs="EPSG:3035",
    origin=(0.0, 0.0),
    units="metres",
    resolutions=(
        100000.0,
        10000.0,
        1000.0,
        100.0,
        10.0,
        1.0,
    ),
)


# ---------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------

_STANDARDS: Dict[str, GridStandard] = {
    CSQUARES.code: CSQUARES,
    INSPIRE.code: INSPIRE,
}


def get_standard(code: str) -> GridStandard:
    """
    Return a grid standard from its code.

    Parameters
    ----------
    code : str
        Standard identifier (case insensitive).

    Returns
    -------
    GridStandard

    Raises
    ------
    ValueError
        If the requested standard is not supported.
    """

    key = code.lower()

    if key not in _STANDARDS:
        raise ValueError(
            f"Unknown grid standard '{code}'. "
            f"Available standards: {', '.join(_STANDARDS.keys())}"
        )

    return _STANDARDS[key]


def available_standards() -> tuple[str, ...]:
    """
    Return the identifiers of all supported standards.
    """

    return tuple(sorted(_STANDARDS.keys()))