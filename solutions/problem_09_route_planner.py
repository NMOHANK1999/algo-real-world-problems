"""09. Route Planner with a Stop Limit — see problems/09_route_planner.md"""

from __future__ import annotations


def cheapest_route(
    graph: dict[str, list[tuple[str, int]]],
    src: str,
    dst: str,
    max_stops: int,
) -> int:
    minCost = float("inf")
    def dfs(src, costSoFar, stops, track):
        nonlocal minCost
        if src == dst:
            # ans_string  = "->".join(track)
            # print(ans_string)
            minCost = min(minCost, costSoFar)
            return None
        for dst_, cost in graph[src]:
            if stops <= max_stops:
                dfs(dst_, costSoFar + cost, stops + 1, track + [dst_])
    dfs(src, 0, 0, [src])
    if minCost == float("inf"):
        return -1
    return minCost

if __name__ == "__main__":
    graph = {
        "A": [("B", 100), ("C", 500)],
        "B": [("C", 100)],
        "C": [],
    }
    assert cheapest_route(graph, "A", "C", max_stops=0) == 500  # -> 500 (A->C direct)
    print('✅')
    assert cheapest_route(graph, "A", "C", max_stops=1) == 200  # -> 200 (A->B->C)
    print('✅')
    assert cheapest_route(graph, "A", "C", max_stops=-1) == -1 # invalid input, define behavior
    print('✅')
    assert cheapest_route(graph, "A", "Z", max_stops=5) == -1  # -> -1 (Z doesn't exist)
    print('✅')
