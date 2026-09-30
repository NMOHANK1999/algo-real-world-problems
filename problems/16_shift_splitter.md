# 16. Two-Shift Scheduler

**Concept:** Bipartite check via DFS 2-coloring
**Real-world:** Splitting staff into two shifts so no conflicting pair
works together, assigning two frequencies to adjacent radio towers,
A/B-partitioning services that must not share a failure domain.

## Problem

Workers are numbered `0..n-1`. Each `(a, b)` in `conflicts` means `a` and
`b` must be on **different** shifts.

```python
def split_into_two_shifts(
    n: int, conflicts: list[tuple[int, int]]
) -> tuple[set[int], set[int]] | None:
    """Return (day_shift, night_shift) — disjoint sets covering all n
    workers with every conflict pair split across them. None if impossible."""


def odd_conflict_cycle(n: int, conflicts: list[tuple[int, int]]) -> list[int] | None:
    """If no valid split exists, return proof: a cycle of odd length
    [w0, w1, ..., wk] where each consecutive pair (and wk, w0) is a
    conflict. None if a valid split exists."""
```

## Requirements

- Workers with no conflicts must still be placed on some shift.
- The conflict graph may be disconnected — 2-color every component.
- A graph is bipartite **iff** it has no odd cycle. `odd_conflict_cycle`
  should use the coloring DFS itself: when you find an edge between two
  same-colored workers, the DFS tree paths back to their common ancestor
  plus that edge form an odd cycle.
- O(V + E).

## Example

```python
split_into_two_shifts(4, [(0, 1), (1, 2), (2, 3)])
# -> ({0, 2}, {1, 3})   (or the two sets swapped)

split_into_two_shifts(3, [(0, 1), (1, 2), (2, 0)])
# -> None  (triangle: someone always shares a shift with a rival)

odd_conflict_cycle(3, [(0, 1), (1, 2), (2, 0)])
# -> [0, 1, 2]  (any rotation / direction)
```

## Something to think about

With **three** shifts, the problem becomes graph 3-coloring — which is
NP-complete. Why does the "forced choice" argument that makes 2-coloring
easy (once one node's color is fixed, its neighbors' colors are forced)
break down with three colors?
