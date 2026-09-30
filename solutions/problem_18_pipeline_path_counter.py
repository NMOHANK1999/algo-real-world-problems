"""18. Build Pipeline Paths — see problems/18_pipeline_path_counter.md"""

from __future__ import annotations


def count_paths(dag: dict[str, list[str]], src: str, dst: str) -> int:
    raise NotImplementedError


def critical_path(
    dag: dict[str, list[str]], durations: dict[str, int], src: str, dst: str
) -> tuple[int, list[str]] | None:
    raise NotImplementedError
