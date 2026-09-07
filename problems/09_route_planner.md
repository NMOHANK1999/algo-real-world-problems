# 09. Route Planner with a Stop Limit

**Concept:** Graph search with a constraint dimension (BFS/Dijkstra
variant — plain BFS/Dijkstra isn't enough on its own)
**Real-world:** Ride-share / delivery routing; "cheapest flight with at
most K stops."

## Problem

```python
def cheapest_route(
    graph: dict[str, list[tuple[str, int]]],
    src: str,
    dst: str,
    max_stops: int,
) -> int:
    """
    graph: adjacency list, graph[node] = [(neighbor, cost), ...]
    Returns the cheapest cost to get from src to dst using at most
    max_stops intermediate stops (i.e. at most max_stops + 1 edges).
    Returns -1 if unreachable within that limit.
    """
```

## Requirements

- This is a **weighted** graph, so plain BFS by itself doesn't give you
  cheapest cost — but plain Dijkstra by itself doesn't respect the stop
  limit either (it would happily take a cheap path with too many hops).
  Your state needs to track both "current node" and "stops used so far."
- `max_stops = 0` means direct edges only.

## Example

```python
graph = {
    "A": [("B", 100), ("C", 500)],
    "B": [("C", 100)],
    "C": [],
}
cheapest_route(graph, "A", "C", max_stops=0)  # -> 500 (A->C direct)
cheapest_route(graph, "A", "C", max_stops=1)  # -> 200 (A->B->C)
cheapest_route(graph, "A", "C", max_stops=-1) # invalid input, define behavior
cheapest_route(graph, "A", "Z", max_stops=5)  # -> -1 (Z doesn't exist)
```

## Something to think about

Why doesn't a visited-set (marking a node "done" the first time you pop it,
like classic Dijkstra) work here? What has to change about what "visited"
means once stop-count is part of the state?
