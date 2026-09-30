"""21. Fiber Network Planner — see problems/21_fiber_network_planner.md"""

from __future__ import annotations


def plan_network(
    n: int, candidate_links: list[tuple[int, int, int]]
) -> tuple[int, list[tuple[int, int, int]]] | None:
    raise NotImplementedError


def cluster_sites(
    n: int, candidate_links: list[tuple[int, int, int]], k: int
) -> list[set[int]]:
    raise NotImplementedError
