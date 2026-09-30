# 22. Datacenter Rack Power-On

**Concept:** Online Union-Find on a grid (dynamic connectivity, adding
only — "Number of Islands II")
**Real-world:** Racks come online one at a time during a datacenter
bring-up; adjacent powered racks share a network segment. Ops wants the
number of isolated segments after every power-on event, in real time.

## Problem

```python
def segments_after_each_power_on(
    rows: int, cols: int, positions: list[tuple[int, int]]
) -> list[int]:
    """The floor is a rows x cols grid, initially all off. positions[i]
    is the rack powered on at step i. Powered racks that touch
    horizontally or vertically form one segment. Return the number of
    segments after each step."""
```

## Requirements

- Re-running a flood fill / DFS after every step is O(k · rows · cols)
  — too slow. Use Union-Find: each power-on adds one set, then unions
  with up to 4 powered neighbors, adjusting a running count.
- Powering on an already-on rack is a no-op (count unchanged).
- Map `(r, c)` to a single index `r * cols + c`, or key a dict by tuple.
- A test powers on every rack of a 150x150 floor (22,500 events) and
  expects the answer in well under a few seconds.

## Example

```python
segments_after_each_power_on(3, 3, [(0, 0), (0, 1), (1, 2), (2, 1), (1, 1)])
# -> [1, 1, 2, 3, 1]
```

```text
step 0     step 1     step 2     step 3     step 4
X . .      X X .      X X .      X X .      X X .
. . .      . . .      . . X      . . X      . X X
. . .      . . .      . . .      . X .      . X .
```

## Something to think about

Now suppose racks can also be **powered off**. Union-Find can't split
sets. One classic trick for offline problems: process the events in
*reverse*, so removals become additions. When does that trick apply, and
when doesn't it?
