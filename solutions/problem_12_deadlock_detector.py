"""12. Deadlock Detector — see problems/12_deadlock_detector.md"""

from __future__ import annotations


def find_deadlock(wait_for: dict[str, list[str]]) -> list[str] | None:
    raise NotImplementedError


def stuck_processes(wait_for: dict[str, list[str]]) -> set[str]:
    raise NotImplementedError
