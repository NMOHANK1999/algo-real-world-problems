"""32. Data Center Heatmap — see problems/32_data_center_heatmap.md"""

from __future__ import annotations


class HeatmapTotals:
    def __init__(self, readings: list[list[int]]) -> None:
        raise NotImplementedError

    def rectangle_total(self, top: int, left: int, bottom: int, right: int) -> int:
        raise NotImplementedError
