"""26. Calendar Free/Busy — see problems/26_calendar_free_busy.md"""

from __future__ import annotations


def merge_busy(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    raise NotImplementedError


def common_free_slots(
    calendars: list[list[tuple[int, int]]],
    day_start: int,
    day_end: int,
    min_duration: int,
) -> list[tuple[int, int]]:
    raise NotImplementedError


def min_rooms_needed(meetings: list[tuple[int, int]]) -> int:
    raise NotImplementedError
