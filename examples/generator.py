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

    @property
    def standard(self) -> GridStandard:
        return self._standard

    @property
    def resolution(self) -> float:
        return self._resolution

    def generate(
        self,
        bbox: Tuple[float, float, float, float],
    ) -> pd.DataFrame:
        raise NotImplementedError

    def _snap_down(
        self,
        value: float,
        origin: float,
    ) -> float:
        return (
            math.floor((value - origin) / self._resolution)
            * self._resolution
            + origin
        )

    def _snap_up(
        self,
        value: float,
        origin: float,
    ) -> float:
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
        raise NotImplementedError

    def _generate_axis(
        self,
        minimum: float,
        maximum: float,
        origin: float,
    ) -> np.ndarray:
        raise NotImplementedError

    def _build_dataframe(
        self,
        xs: np.ndarray,
        ys: np.ndarray,
    ) -> pd.DataFrame:
        raise NotImplementedError
