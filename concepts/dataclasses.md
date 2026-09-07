# Python data classes

A data class is a regular Python class used mainly to hold related data. The
`@dataclass` decorator automatically creates useful methods such as an
initializer, so you can write `Meeting("standup", 0, 30, 5)` without defining
`__init__` yourself.

`@dataclass(frozen=True)` makes instances read-only after creation. For example,
after creating a meeting, assigning a different value to `meeting.start` raises
an error. This helps prevent scheduling data from being changed accidentally.

## Problem 10 fields

`Meeting` contains:

- `name: str` — the meeting's name, used to identify it in the result.
- `start: int` — the meeting's starting time.
- `end: int` — the meeting's ending time.
- `attendees: int` — the number of people who need a room.

`Room` contains:

- `name: str` — the room's name, used to identify the assigned room.
- `capacity: int` — the maximum number of people the room can hold.

The annotations `str` and `int` describe the expected value types: `str` means
text, and `int` means a whole number.

The `start` and `end` values are minutes since an arbitrary reference point. The
exact reference does not matter as long as every meeting uses the same one.
Meeting times use `[start, end)`: the starting minute is included, but the ending
minute is excluded. Therefore, a meeting from `0` to `30` does not overlap one
from `30` to `60`, so the same room can host them back to back.
