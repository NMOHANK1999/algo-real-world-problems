# 11. Land Parcel Mapper

**Concept:** DFS on a grid (flood fill / connected regions)
**Real-world:** Satellite-image land segmentation, the "paint bucket" tool
in image editors, counting contiguous occupied regions on a map.

## Problem

A satellite pass returns a grid where `"1"` is land and `"0"` is water.
Two land cells belong to the same parcel if they touch **horizontally or
vertically** (not diagonally).

```python
def count_parcels(grid: list[list[str]]) -> int:
    """Number of distinct land parcels."""


def largest_parcel(grid: list[list[str]]) -> int:
    """Area (cell count) of the largest parcel, 0 if there is no land."""


def fill_region(
    image: list[list[int]], row: int, col: int, new_color: int
) -> list[list[int]]:
    """Paint-bucket: recolor the region connected to (row, col) that shares
    its original color. Returns a NEW grid; the input must not be mutated."""
```

## Requirements

- None of the functions may mutate their input. (Counting parcels by
  overwriting `"1"` with `"0"` is a common trick — do it on a copy, or use
  a visited set.)
- Handle an empty grid (`[]`) and grids with empty rows gracefully.
- Must work on a 300x300 all-land grid. Python's default recursion limit
  is ~1000, so a naive recursive DFS will crash — use an explicit stack
  (or justify raising the limit and know why that's risky).
- `fill_region` with `new_color` equal to the original color returns an
  unchanged copy (and must not loop forever).

## Example

```python
grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"],
]
count_parcels(grid)   # -> 2
largest_parcel(grid)  # -> 3

image = [
    [1, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
]
fill_region(image, 0, 0, 7)
# -> [[7, 7, 0],
#     [7, 0, 0],
#     [7, 7, 7]]
```

## Something to think about

If the grid is too big to fit in memory and arrives one row at a time
(streaming), you can't DFS over it. How would you count parcels using only
the previous row plus a Union-Find?
