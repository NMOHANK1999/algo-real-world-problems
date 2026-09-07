# 10. Meeting Room Assignment

**Concept:** Backtracking / constraint satisfaction
**Real-world:** A scheduling assistant assigning meetings to rooms without
double-booking or exceeding capacity.

## Problem

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Meeting:
    name: str
    start: int          # minutes since some epoch
    end: int
    attendees: int

@dataclass(frozen=True)
class Room:
    name: str
    capacity: int

def assign_rooms(
    meetings: list[Meeting], rooms: list[Room]
) -> dict[str, str] | None:
    """
    Return a mapping {meeting.name: room.name} such that:
      - every meeting is assigned a room with capacity >= attendees
      - no room is assigned two meetings whose time ranges overlap
    Return None if no valid assignment exists for every meeting.
    """
```

## Requirements

- Time ranges `[start, end)` — meetings touching at an endpoint (one ends
  exactly when another starts) do **not** overlap.
- Must actually backtrack: a greedy "assign the first room that fits" will
  fail on inputs where an earlier greedy choice blocks a later meeting that
  had no alternative. Your solution needs to be able to undo a choice and
  try a different room.
- If it's genuinely impossible (e.g. more overlapping meetings than rooms,
  or a meeting too big for every room), return `None` rather than raising.

## Example

```python
meetings = [
    Meeting("standup", 0, 30, 5),
    Meeting("planning", 30, 90, 8),
    Meeting("1on1", 0, 30, 2),
]
rooms = [Room("small", 3), Room("big", 10)]

result = assign_rooms(meetings, rooms)
# one valid result: {"standup": "big", "planning": "big", "1on1": "small"}
# (standup and 1on1 overlap in time so they need different rooms;
#  planning can reuse "big" since it starts exactly when standup ends)
```

```python
meetings = [
    Meeting("a", 0, 60, 5),
    Meeting("b", 0, 60, 5),
    Meeting("c", 0, 60, 5),
]
rooms = [Room("only_room", 10)]
assign_rooms(meetings, rooms)  # -> None (3 overlapping meetings, 1 room)
```

## Something to think about

What ordering heuristic on `meetings` (e.g. most-constrained-first) would
make your backtracking search fail fast on impossible inputs instead of
exploring dead ends? You don't have to implement it — just be able to
explain the idea (this is the same principle behind constraint propagation
in Sudoku solvers).
