"""
standardgrid.standards
======================

Definitions of the official spatial reference grid standards supported
by StandardGrid.

Each standard defines:

- Official name
- Stable API identifier
- Coordinate Reference System (CRS)
- Grid origin
- Coordinate units
- Supported grid resolutions

The definitions are immutable and are used throughout the library.

Author
------
Pedro Monteiro

License
-------
MIT
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GridStandard:
    """
    Immutable definition of a spatial reference grid standard.

    Attributes
    ----------
    name
        Official human-readable name.

    code
        Stable identifier used by the StandardGrid API.

    crs
        Coordinate Reference System of the standard.

    origin
        Origin of the reference grid.

    units
        Coordinate units used by the standard.

    resolutions
        Supported grid resolutions.
    """

    name: str
    code: str
    crs: str
    origin: tuple[float, float]
    units: str
    resolutions: tuple[float, ...]
    extent: tuple[float, float, float, float] | None


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
    extent=(
        -180.0,
        -90.0,
        180.0,
        90.0,
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
    extent=None,
)


# ---------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------

#: Registry of supported grid standards.
_STANDARDS: dict[str, GridStandard] = {
    CSQUARES.code: CSQUARES,
    INSPIRE.code: INSPIRE,
}


def get_standard(code: str) -> GridStandard:
    """
    Return a grid standard from its API identifier.

    Parameters
    ----------
    code : str
        API identifier of the standard
        (e.g. "csquares", "inspire").

        Comparison is case insensitive.

    Returns
    -------
    GridStandard
        The requested grid standard.

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
    Return the API identifiers of all supported grid standards.
    """

    return tuple(sorted(_STANDARDS.keys()))


def standards() -> tuple[GridStandard, ...]:
    """
    Return all supported grid standards.
    """

    return tuple(_STANDARDS.values())



