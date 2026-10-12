# 31. Usage Report Queries

**Concept:** 1D prefix sums and binary search
**Real-world:** A static dashboard answers many questions such as "how much
usage occurred between two dates?" without rescanning all raw events.

## Problem

`usage[i]` is the non-negative usage recorded on day `i`.

```python
def usage_totals(
    usage: list[int], queries: list[tuple[int, int]]
) -> list[int]:
    """For every inclusive (start, end) query, return the total usage."""


def first_day_reaching(usage: list[int], threshold: int) -> int:
    """Return the smallest day whose inclusive cumulative usage is at least
    threshold, or -1 if it is never reached."""
```

## Requirements

- Build one prefix-sum array so `usage_totals` runs in O(n + q), where q is
  the number of queries. Do not call `sum` for every query.
- `first_day_reaching` must run in O(n) or O(n log n). Since usage is
  non-negative, cumulative totals are sorted and can be binary searched.
- A threshold of 0 is reached on day 0 when `usage` is non-empty. Empty input
  always returns -1.
- Do not mutate either input.

## Example

```python
usage = [5, 2, 7, 1, 3]
usage_totals(usage, [(0, 4), (1, 3), (2, 2)])  # -> [18, 10, 7]
first_day_reaching(usage, 7)                    # -> 1
first_day_reaching(usage, 8)                    # -> 2
first_day_reaching(usage, 99)                   # -> -1
```

## Something to think about

A prefix-sum array makes reads fast but updating one day expensive. Which
previous problem is designed for the version with both updates and queries?
