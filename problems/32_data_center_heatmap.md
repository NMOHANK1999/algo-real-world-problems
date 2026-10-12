# 32. Data Center Heatmap

**Concept:** 2D prefix sums
**Real-world:** A monitoring heatmap records rack temperature or power draw in
a grid. Operators repeatedly ask for totals inside rectangular zones.

## Problem

```python
class HeatmapTotals:
    def __init__(self, readings: list[list[int]]) -> None:
        """readings[row][column] is a (possibly negative) measurement."""

    def rectangle_total(
        self, top: int, left: int, bottom: int, right: int
    ) -> int:
        """Return the inclusive total in rows top..bottom and columns
        left..right."""
```

## Requirements

- Precompute a 2D prefix-sum table in O(rows * columns).
- Each `rectangle_total` call must run in O(1), using inclusion-exclusion on
  four prefix-table corners.
- The grid is non-empty and rectangular. Do not mutate it.
- A test makes many full-grid queries; scanning each rectangle will time out.

## Example

```python
readings = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
]
heatmap = HeatmapTotals(readings)
heatmap.rectangle_total(0, 0, 2, 4)  # -> 36
heatmap.rectangle_total(1, 1, 2, 3)  # -> 14
```

## Something to think about

Why does padding the prefix table with a zero row and zero column eliminate
special cases for rectangles touching the top or left edge?
