"""
standardgrid.generator
======================

Core engine for generating standard-aligned reference grid centroids.
"""

from __future__ import annotations

import math
from typing import Tuple

import numpy as np
import pandas as pd

from .standards import GridStandard


class GridGenerator:
    """
    Generate centroid coordinates aligned to an official spatial
    reference grid.
    """

    def __init__(
        self,
        standard: GridStandard,
        resolution: float,
    ) -> None:

        self._standard = standard
        self._resolution = resolution
        self._origin = standard.origin

        # Metadata generated with the grid
        self._bounds = None
        self._nrows = None
        self._ncols = None
        self._npoints = None

    @property
    def standard(self) -> GridStandard:
        return self._standard

    @property
    def resolution(self) -> float:
        return self._resolution
        
    @property
    def bounds(self):
        """
        Bounding box aligned to the reference grid.
        """
        return self._bounds


    @property
    def nrows(self) -> int:
        """
        Number of grid rows.
        """
        return self._nrows


    @property
    def ncols(self) -> int:
        """
        Number of grid columns.
        """
        return self._ncols


    @property
    def npoints(self) -> int:
        """
        Number of generated centroids.
        """
        return self._npoints


    def generate(
        self,
        bbox: Tuple[float, float, float, float],
    ) -> pd.DataFrame:
        """
        Generate centroid coordinates inside a bounding box.

        Parameters
        ----------
        bbox : tuple
            (xmin, ymin, xmax, ymax)

        Returns
        -------
        pandas.DataFrame
            DataFrame with x and y coordinates.
        """

        xmin, ymin, xmax, ymax = self._snap_bbox(bbox)

        xs = self._generate_axis(
            xmin,
            xmax,
            self._origin[0],
        )

        ys = self._generate_axis(
            ymin,
            ymax,
            self._origin[1],
        )

        df = self._build_dataframe(
            xs,
            ys,
        )

        # Store metadata
        self._bounds = (
            xmin,
            ymin,
            xmax,
            ymax,
        )

        self._nrows = len(ys)
        self._ncols = len(xs)
        self._npoints = len(df)

        return df

    # ------------------------------------------------------------------
    # Snapping helpers
    # ------------------------------------------------------------------

    def _snap_down(self, value: float, origin: float) -> float:
        return (
            math.floor((value - origin) / self._resolution)
            * self._resolution
            + origin
        )

    def _snap_up(self, value: float, origin: float) -> float:
        """
        Snap a coordinate up to the next grid line.
        """
        return (
            math.ceil((value - origin) / self._resolution)
            * self._resolution
            + origin
        )

    def _snap_bbox(
        self,
        bbox: Tuple[float, float, float, float],
    ) -> Tuple[float, float, float, float]:

        xmin, ymin, xmax, ymax = bbox

        if xmin >= xmax:
            raise ValueError("xmin must be smaller than xmax.")
        if ymin >= ymax:
            raise ValueError("ymin must be smaller than ymax.")

        xmin = self._snap_down(xmin, self._origin[0])
        ymin = self._snap_down(ymin, self._origin[1])
        xmax = self._snap_up(xmax, self._origin[0])
        ymax = self._snap_up(ymax, self._origin[1])

        return xmin, ymin, xmax, ymax

    # ------------------------------------------------------------------
    # Axis generation
    # ------------------------------------------------------------------

    def _generate_axis(
        self,
        minimum: float,
        maximum: float,
        origin: float,
    ) -> np.ndarray:
        """
        Generate centroid coordinates for one axis.

        Parameters
        ----------
        minimum : float
            Minimum snapped coordinate.
        maximum : float
            Maximum snapped coordinate.
        origin : float
            Grid origin.

        Returns
        -------
        numpy.ndarray
            Centroid coordinates.
        """
        
        start = self._snap_down(minimum, origin) + self._resolution / 2
        stop = self._snap_up(maximum, origin)

        values = np.arange(
            start,
            stop,
            self._resolution,
            dtype=float,
        )

        return np.round(
            values,
            self._centroid_decimals(),
        )


# ------------------------------------------------------------------
    # 
    # ------------------------------------------------------------------
    def _centroid_decimals(self) -> int:
        """
        Number of decimal places required to represent
        centroid coordinates.
        """
        text = f"{self._resolution / 2:.10f}".rstrip("0")

        if "." in text:
            return len(text.split(".")[1])

        return 0



    # ------------------------------------------------------------------
    # DataFrame builder
    # ------------------------------------------------------------------

    def _build_dataframe(
        self,
        xs: np.ndarray,
        ys: np.ndarray,
    ) -> pd.DataFrame:
        """
        Build a DataFrame containing all centroid coordinates.
        """
        xx, yy = np.meshgrid(xs, ys, indexing="xy")

        return pd.DataFrame({"x": xx.ravel(), "y": yy.ravel()})
