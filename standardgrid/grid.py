"""
standardgrid.grid
=================

Public API for generating standards-aligned reference grids.
"""

from __future__ import annotations

from typing import Tuple

import pandas as pd

from .generator import GridGenerator
from .standards import get_standard


class Grid:
    """
    Public interface for generating standards-aligned reference grids.
    """

    def __init__(
        self,
        standard: str,
        resolution: float,
    ) -> None:

        self._standard = get_standard(standard)

        if resolution not in self._standard.resolutions:

            supported = "\n".join(
                f"  • {r}"
                for r in self._standard.resolutions
            )

            raise ValueError(
                f"Resolution {resolution} is not supported for "
                f"{self._standard.name}.\n\n"
                f"Supported resolutions are:\n"
                f"{supported}"
            )

        self._resolution = resolution

        self._bbox = None
        self._points = None

        self._generator = GridGenerator(
            self._standard,
            resolution,
        )

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def standard(self):
        return self._standard

    @property
    def resolution(self):
        return self._resolution

    @property
    def bbox(self):
        return self._bbox

    @property
    def bounds(self):
        return self._bounds

    @property
    def points(self) -> pd.DataFrame | None:
        return self._points

    @property
    def nrows(self) -> int | None:
        return self._nrows

    @property
    def ncols(self) -> int | None:
        return self._ncols

    @property
    def npoints(self) -> int | None:
        return self._npoints

    @property
    def shape(self):
        if self._nrows is None:
            return None
        return (self._nrows, self._ncols)

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def generate(self, bbox: tuple[float, float, float, float]) -> "Grid":
        self._bbox = bbox
        self._points = self._generator.generate(bbox)

        self._bounds = self._generator.bounds
        self._nrows = self._generator.nrows
        self._ncols = self._generator.ncols
        self._npoints = self._generator.npoints

        return self

    def __repr__(self) -> str:
        if self._points is None:
            return (
                f"Grid(standard='{self.standard.code}', "
                f"resolution={self.resolution})"
            )

        return (
            "Grid\n"
            "----\n"
            f"Standard   : {self.standard.name}\n"
            f"CRS        : {self.standard.crs}\n"
            f"Resolution : {self.resolution} {self.standard.units}\n"
            f"Rows       : {self.nrows}\n"
            f"Columns    : {self.ncols}\n"
            f"Points     : {self.npoints}\n"
            f"Bounds     : {self.bounds}"
        )

    def to_csv(self, filename: str, index: bool = False) -> None:
        if self._points is None:
            raise ValueError("No grid has been generated.")
        self._points.to_csv(filename, index=index)

    def to_excel(self, filename: str, index: bool = False) -> None:
        if self._points is None:
            raise ValueError("No grid has been generated.")
        self._points.to_excel(filename, index=index)
