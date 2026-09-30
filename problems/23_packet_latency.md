# 23. Packet Broadcast Latency

**Concept:** Dijkstra's shortest paths (non-negative weights, min-heap)
**Real-world:** How long until a config push / gossip message reaches
every node in a cluster; OSPF link-state routing; lowest-latency path
selection in a CDN.

## Problem

Nodes are `0..n-1`. Each link `(u, v, ms)` is **directed**: a packet
takes `ms` milliseconds to go from `u` to `v`.

```python
def broadcast_time(n: int, links: list[tuple[int, int, int]], source: int) -> int:
    """Time until every node has received a packet broadcast from source
    (each node forwards immediately on receipt). -1 if some node never
    receives it."""


def fastest_route(
    n: int, links: list[tuple[int, int, int]], src: int, dst: int
) -> tuple[int, list[int]] | None:
    """(total_ms, [src, ..., dst]) along a minimum-latency path,
    or None if dst is unreachable."""
```

## Requirements

- O((V + E) log V) with `heapq`. Skip stale heap entries (the "lazy
  deletion" pattern: if the popped distance is larger than the best
  known, ignore it).
- Weights are `>= 0` (zero-latency links exist). Parallel links between
  the same pair may appear — the cheaper one matters.
- Reconstruct the route with a `prev[]` array, not by storing whole paths
  in the heap.

## Example

```python
links = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
broadcast_time(4, links, 0)   # -> 4   (node 3 is last, via 0->2->1->3)
fastest_route(4, links, 0, 3) # -> (4, [0, 2, 1, 3])
broadcast_time(3, [(0, 1, 1)], 0)  # -> -1 (node 2 unreachable)
```

## Something to think about

Problem 09 (Route Planner) also used a heap, but a plain "visited" set
broke it. Why is it safe here to finalize a node the first time it's
popped? What single assumption about edge weights does that rely on?
