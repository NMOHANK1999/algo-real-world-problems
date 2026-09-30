"""28. Live Metrics Range Store — see problems/28_metrics_range_store.md"""

from __future__ import annotations


class MetricsStore:
    def __init__(self, values: list[int]) -> None:
        raise NotImplementedError

    def update(self, index: int, value: int) -> None:
        raise NotImplementedError

    def range_sum(self, left: int, right: int) -> int:
        raise NotImplementedError

    def first_bucket_reaching(self, threshold: int) -> int:
        raise NotImplementedError
