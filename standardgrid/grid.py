from __future__ import annotations

import pandas as pd

from .generator import GridGenerator
from .standards import GridStandard, get_standard


class Grid:
   

    """
    standardgrid.grid
    =================

    Public interface for generating standards-aligned
    reference grids.

    Parameters
    ----------
    standard : str
        API identifier of the grid standard
        (e.g. "csquares", "inspire").

    resolution : float
        Grid resolution expressed in the units of the
        selected standard.

        The resolution must be one of the supported
        resolutions for that standard.
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
        
        self._bounds = None
        self._nrows = None
        self._ncols = None
        self._npoints = None

        self._generator = GridGenerator(
            self._standard,
            resolution,
        )

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def standard(self) -> GridStandard:
        return self._standard

    @property
    def resolution(self) -> float:
        return self._resolution

    @property
    def bbox(self) -> tuple[float, float, float, float] | None:
        return self._bbox

    @property
    def bounds(self) -> tuple[float, float, float, float] | None:
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
    def shape(self) -> tuple[int, int] | None:
        if self._nrows is None:
            return None
        return (self._nrows, self._ncols)

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def generate(
        self,
        bbox: tuple[float, float, float, float],
        bbox_crs: str | None = None,
    ) -> "Grid":
        """
        Generate a reference grid within a bounding box.

        Parameters
        ----------
        bbox : tuple
            Bounding box expressed as
            (xmin, ymin, xmax, ymax).

        bbox_crs : str, optional
            Coordinate Reference System (CRS) of the
            bounding box (e.g. "EPSG:4326").
            If provided, it must match the CRS of the
            selected grid standard.

        Returns
        -------
        Grid
            The generated grid instance.
        """

        self._bbox = bbox
        self._points = self._generator.generate(
            bbox,
            bbox_crs=bbox_crs,
        )

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
