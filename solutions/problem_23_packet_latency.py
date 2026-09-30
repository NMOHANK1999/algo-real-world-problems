"""23. Packet Broadcast Latency — see problems/23_packet_latency.md"""

from __future__ import annotations


def broadcast_time(n: int, links: list[tuple[int, int, int]], source: int) -> int:
    raise NotImplementedError


def fastest_route(
    n: int, links: list[tuple[int, int, int]], src: int, dst: int
) -> tuple[int, list[int]] | None:
    raise NotImplementedError
