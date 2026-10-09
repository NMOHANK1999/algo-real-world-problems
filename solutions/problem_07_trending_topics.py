"""07. Trending Topics Feed — see problems/07_trending_topics_feed.md"""

from __future__ import annotations
import heapq


class TrendingTracker:
    def __init__(self, decay_half_life_seconds: float) -> None:
        self.decay_half_life_seconds = decay_half_life_seconds
        self.store = {} 
        self.cache = []

    def record_event(self, topic: str, timestamp: float) -> None:
        if topic not in self.store:
            self.store[topic] = []
        self.store[topic].append(timestamp)
        # print(self.store)

    def top_k(self, k: int, now: float) -> list[str]:
        for key, val in self.store.items():
            age = 0
            for time in val:
                age -= 2 ** (-(now - time) / self.decay_half_life_seconds)
            heapq.heappush(self.cache, [age, key])
        ans = []
        for _ in range(k):
            _, key =  heapq.heappop(self.cache)
            ans.append(key)
        return ans 

    
# tt = TrendingTracker(decay_half_life_seconds=60)
# tt.record_event("python", 0)
# tt.record_event("python", 0)
# tt.record_event("rust", 0)
# print(tt.top_k(2, now=0))     # -> ["python", "rust"]   (python weight=2, rust=1)
# print(tt.top_k(2, now=60))    # weights halved: python=1.0, rust=0.5 -> same order
