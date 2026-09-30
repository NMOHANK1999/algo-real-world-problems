# 25. Load Spike Alerts

**Concept:** Monotonic stack ("next greater element", largest rectangle
in a histogram)
**Real-world:** Monitoring dashboards: "how long until load exceeds
this hour's level?", and "what's the biggest block of guaranteed
capacity (min load × duration) we sustained?"

## Problem

`loads[i]` is the server load during hour `i`.

```python
def hours_until_higher_load(loads: list[int]) -> list[int]:
    """For each hour i, how many hours until a strictly higher load
    appears. 0 if it never does."""


def largest_sustained_block(loads: list[int]) -> int:
    """Max over all contiguous windows [i..j] of
    min(loads[i..j]) * (j - i + 1)."""
```

## Requirements

- Both in O(n) using a stack of indices whose loads are monotonic. Each
  index is pushed and popped at most once — that's the amortized
  argument.
- The O(n²) "look ahead from every index" version is fine as a first
  step, but a test with 200,000 hours needs the stack version.
- Empty input → `[]` and `0`.

## Example

```python
hours_until_higher_load([73, 74, 75, 71, 69, 72, 76, 73])
# -> [1, 1, 4, 2, 1, 1, 0, 0]

largest_sustained_block([2, 1, 5, 6, 2, 3])
# -> 10   (window [5, 6] -> min 5 * 2 hours)
```

## Something to think about

For `largest_sustained_block`, when you pop an index from the stack, what
exactly are the left and right boundaries of the widest window in which
that load is the minimum? Why does a sentinel `0` appended at the end
simplify the code?
