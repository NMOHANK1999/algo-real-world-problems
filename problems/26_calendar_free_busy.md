# 26. Calendar Free/Busy

**Concept:** Interval merging and sweep line (sort by start; events
+1/-1)
**Real-world:** Google Calendar "find a time" for several people,
meeting-room capacity planning, merging overlapping maintenance windows.

## Problem

All intervals are half-open `[start, end)` in minutes, `start < end`.

```python
def merge_busy(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or touching intervals. Return sorted by start.
    [1,3) and [3,5) touch and merge into [1,5)."""


def common_free_slots(
    calendars: list[list[tuple[int, int]]],
    day_start: int,
    day_end: int,
    min_duration: int,
) -> list[tuple[int, int]]:
    """Slots within [day_start, day_end) when NOBODY is busy and that
    last at least min_duration. Busy intervals may extend outside the
    day. Sorted by start."""


def min_rooms_needed(meetings: list[tuple[int, int]]) -> int:
    """Minimum number of rooms so no two overlapping meetings share one.
    A meeting ending at t and one starting at t can share a room."""
```

## Requirements

- `merge_busy`: sort by start, then one pass. O(n log n).
- `common_free_slots`: flatten every calendar, merge once, then walk the
  gaps — clipping to the day window.
- `min_rooms_needed`: sweep line. Sort starts and ends separately (or
  make `(time, +1/-1)` events) and track the running max. Get the tie
  rule right: at the same timestamp, process ends before starts.
- Inputs may be unsorted. Don't mutate them.

## Example

```python
merge_busy([(9, 10), (1, 3), (2, 6), (6, 7)])
# -> [(1, 7), (9, 10)]

alice = [(540, 600), (720, 780)]        # 9-10am, 12-1pm
bob   = [(570, 660), (900, 960)]        # 9:30-11am, 3-4pm
common_free_slots([alice, bob], 480, 1020, 60)   # workday 8am-5pm
# -> [(480, 540), (660, 720), (780, 900), (960, 1020)]
#    8-9am, 11am-12pm, 1-3pm, 4-5pm

min_rooms_needed([(0, 30), (5, 10), (15, 20)])   # -> 2
min_rooms_needed([(1, 5), (5, 10)])              # -> 1
```

## Something to think about

`min_rooms_needed` tells you *how many* rooms, not *which* meeting goes
in which room. How would you produce an actual assignment (hint: a
min-heap of room end times), and how does this relate to problem 10's
backtracking approach?
