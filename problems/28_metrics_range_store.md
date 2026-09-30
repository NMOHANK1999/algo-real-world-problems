# 28. Live Metrics Range Store

**Concept:** Fenwick tree (Binary Indexed Tree) — or a segment tree
**Real-world:** Time-series dashboards that must both **update** a bucket
("requests in minute 1,042 changed") and answer **range totals**
("requests between minute 300 and 900") thousands of times per second.

## Problem

```python
class MetricsStore:
    def __init__(self, values: list[int]) -> None:
        """values[i] is the metric for bucket i."""

    def update(self, index: int, value: int) -> None:
        """Set bucket index to value (not add — set)."""

    def range_sum(self, left: int, right: int) -> int:
        """Sum of buckets left..right inclusive."""

    def first_bucket_reaching(self, threshold: int) -> int:
        """Smallest index i such that sum(values[0..i]) >= threshold, or -1
        if the total never reaches it. All values are non-negative for
        this method."""
```

## Requirements

- `update` and `range_sum`: O(log n) each. A plain list gives O(1)
  update but O(n) range sum; a plain prefix-sum array gives O(1) range
  sum but O(n) update. The Fenwick tree balances both.
- `__init__` in O(n) (or O(n log n) is acceptable).
- `first_bucket_reaching` in O(log n) by descending the Fenwick tree
  (binary lifting over powers of two) — not a binary search that calls
  `range_sum` O(log n) times (that's O(log² n); fine as a first pass).
- Fenwick trees are usually 1-indexed internally; the public API here is
  0-indexed.
- A test does 20,000 range queries over 100,000 buckets — O(n) queries
  will time out.

## Example

```python
m = MetricsStore([5, 2, 7, 1, 3])
m.range_sum(0, 4)            # -> 18
m.range_sum(1, 3)            # -> 10
m.update(2, 0)               # values now [5, 2, 0, 1, 3]
m.range_sum(1, 3)            # -> 3
m.first_bucket_reaching(7)   # -> 1   (5 + 2)
m.first_bucket_reaching(8)   # -> 3   (5 + 2 + 0 + 1)
m.first_bucket_reaching(99)  # -> -1
```

## Something to think about

A Fenwick tree handles sums well because subtraction lets you turn two
prefix sums into a range sum. Why can't it answer range **max** the same
way? What does a segment tree do differently that makes max/min work?
