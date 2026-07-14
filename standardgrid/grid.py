from __future__ import annotations

from typing import Tuple

import pandas as pd

from .generator import GridGenerator
from .standards import get_standard


class Grid:

    def __init__(
        self,
        standard: str,
        resolution: float,
    ) -> None:

        self._standard = get_standard(standard)
        self._resolution = resolution

        self._bbox = None
        self._points = None

        self._generator = GridGenerator(
            self._standard,
            resolution,
        )

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
    def points(self):
        return self._points

    def generate(
        self,
        bbox: Tuple[
            float,
            float,
            float,
            float,
        ],
    ) -> "Grid":

        self._bbox = bbox

        self._points = self._generator.generate(
            bbox,
        )

        return self
    
    