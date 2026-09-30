# 14. Network Single Points of Failure

**Concept:** Bridges and articulation points (Tarjan's low-link DFS)
**Real-world:** Finding the cables and routers whose failure would split a
datacenter / ISP network into disconnected pieces.

## Problem

Routers are numbered `0..n-1`. `links` are undirected cables. There are no
duplicate cables between the same pair and no self-loops.

```python
def critical_links(n: int, links: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Cables whose removal increases the number of connected components
    (bridges). Each returned as (smaller, larger); the list sorted."""


def critical_routers(n: int, links: list[tuple[int, int]]) -> list[int]:
    """Routers whose removal (with all their cables) increases the number
    of connected components (articulation points). Sorted ascending."""
```

## Requirements

- O(V + E) using discovery times and `low[]` values from a single DFS —
  not "remove each edge and re-check connectivity" (O(E·(V+E))).
- The network may already be disconnected; find critical links/routers in
  every component.
- The DFS root is a special case for articulation points. Know why.

## Example

```text
    0 --- 1
     \   /
      \ /
       2 --- 3 --- 4
```

```python
links = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]
critical_links(5, links)    # -> [(2, 3), (3, 4)]
critical_routers(5, links)  # -> [2, 3]
```

## Something to think about

The spec says "no duplicate cables." Real networks often have two parallel
cables between the same routers precisely for redundancy. What breaks in
the standard "skip the parent" bridge-finding code when parallel edges
exist, and how do you fix it?
