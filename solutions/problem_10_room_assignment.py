"""10. Meeting Room Assignment — see problems/10_room_assignment.md"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Meeting:
    name: str
    start: int
    end: int
    attendees: int


@dataclass(frozen=True)
class Room:
    name: str
    capacity: int


def assign_rooms(
    meetings: list[Meeting], rooms: list[Room]
) -> dict[str, str] | None:
    raise NotImplementedError


assign_rooms([], [])