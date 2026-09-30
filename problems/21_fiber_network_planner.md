# 21. Fiber Network Planner

**Concept:** Minimum spanning tree — Kruskal's algorithm (sort edges +
Union-Find)
**Real-world:** Laying the cheapest set of fiber / power lines / pipes
that connects every site; clustering (stop Kruskal early and you get k
clusters).

## Problem

Sites are numbered `0..n-1`. Each candidate link is `(a, b, cost)` —
undirected, you may build it or not.

```python
def plan_network(
    n: int, candidate_links: list[tuple[int, int, int]]
) -> tuple[int, list[tuple[int, int, int]]] | None:
    """Choose links connecting all n sites at minimum total cost.
    Returns (total_cost, chosen_links) or None if the sites can't all be
    connected. chosen_links is in the order you picked them."""


def cluster_sites(
    n: int, candidate_links: list[tuple[int, int, int]], k: int
) -> list[set[int]]:
    """Group the sites into exactly k clusters so that the cheapest link
    between any two different clusters is as expensive as possible
    (single-linkage clustering). Assume the full network is connectable
    and 1 <= k <= n. Return the clusters sorted by their smallest site."""
```

## Requirements

- Kruskal: sort links by cost, add a link iff its endpoints are in
  different Union-Find sets. O(E log E).
- `n == 1` needs no links: `(0, [])`.
- Ties in cost may produce different but equally cheap trees — any
  minimum-cost answer is accepted.
- `cluster_sites` is the same loop, stopped when there are `k`
  components left.

## Example

```python
links = [
    (0, 1, 4), (0, 2, 3), (1, 2, 1),
    (1, 3, 2), (2, 3, 4), (3, 4, 2),
]
plan_network(5, links)
# -> (8, [(1, 2, 1), (1, 3, 2), (3, 4, 2), (0, 2, 3)])   (order may differ on ties)

plan_network(3, [(0, 1, 5)])   # -> None (site 2 unreachable)

cluster_sites(5, links, 2)
# -> [{0}, {1, 2, 3, 4}]
```

## Something to think about

Prim's algorithm (grow one tree with a heap) also finds an MST. When is
Prim a better choice than Kruskal? (Think dense graphs given as an
adjacency matrix vs sparse edge lists.)
