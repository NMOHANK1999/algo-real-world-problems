"""07. Trending Topics Feed — see problems/07_trending_topics_feed.md"""

from __future__ import annotations


class TrendingTracker:
    def __init__(self, decay_half_life_seconds: float) -> None:
        raise NotImplementedError

    def record_event(self, topic: str, timestamp: float) -> None:
        raise NotImplementedError

    def top_k(self, k: int, now: float) -> list[str]:
        raise NotImplementedError
