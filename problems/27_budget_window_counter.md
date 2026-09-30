# 27. Budget Window Counter

**Concept:** Prefix sums + hash map (count / find subarrays by their sum)
**Real-world:** Billing analytics: "how many contiguous date ranges cost
exactly our budget?" (with refunds as negative entries), and "longest
period where inbound and outbound traffic were perfectly balanced."

## Problem

```python
def count_windows_with_total(costs: list[int], target: int) -> int:
    """Number of contiguous, non-empty windows whose costs sum exactly to
    target. Costs may be negative (refunds) or zero."""


def longest_balanced_window(events: list[str]) -> int:
    """events[i] is "in" or "out". Length of the longest contiguous window
    with equally many "in" and "out" events. 0 if none."""
```

## Requirements

- O(n) each. The key identity: `sum(i..j) = prefix[j+1] - prefix[i]`, so
  "windows ending at j that sum to target" = "earlier prefixes equal to
  `prefix[j+1] - target`" — look them up in a dict of counts.
- A sliding window (problem 06) does **not** work here: with negative
  numbers, growing the window doesn't monotonically increase the sum.
- For `longest_balanced_window`, map `"in"` → +1, `"out"` → -1 and store
  the **first** index at which each prefix value appears.
- Don't forget the empty prefix (sum 0 before index 0).

## Example

```python
count_windows_with_total([1, 1, 1], 2)            # -> 2
count_windows_with_total([3, 4, 7, 2, -3, 1, 4, 2], 7)  # -> 4
count_windows_with_total([0, 0, 0], 0)            # -> 6

longest_balanced_window(["in", "out", "in", "in", "out", "out", "in"])  # -> 6
longest_balanced_window(["in", "in"])                                  # -> 0
```

## Something to think about

Extend `count_windows_with_total` to a 2D grid: count sub-rectangles that
sum to `target`. Fixing a pair of rows reduces it to the 1D problem —
what's the resulting complexity for an R x C grid?
