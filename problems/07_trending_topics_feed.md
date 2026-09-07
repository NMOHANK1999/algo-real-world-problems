# 07. Trending Topics Feed

**Concept:** Heap / priority queue
**Real-world:** Twitter/X "What's happening", a live leaderboard.

## Problem

```python
class TrendingTracker:
    def __init__(self, decay_half_life_seconds: float) -> None:
        """Events lose half their weight every decay_half_life_seconds."""

    def record_event(self, topic: str, timestamp: float) -> None:
        """Record one mention of `topic` at `timestamp`."""

    def top_k(self, k: int, now: float) -> list[str]:
        """Return the k topics with the highest decayed weight as of
        `now`, highest first, ties broken alphabetically."""
```

## Requirements

- A topic's weight is the sum over all its recorded events of
  `2 ** (-(now - event_timestamp) / decay_half_life_seconds)` — i.e. each
  event's contribution halves every half-life.
- `top_k` must not be a full re-sort of every topic that ever existed if
  you're ingesting a high-throughput stream — keep this in mind for the
  "something to think about" below, but for the tests, correctness matters
  more than micro-optimizing the heap usage.
- `record_event` can be called far more often than `top_k`.

## Example

```python
tt = TrendingTracker(decay_half_life_seconds=60)
tt.record_event("python", 0)
tt.record_event("python", 0)
tt.record_event("rust", 0)
tt.top_k(2, now=0)     # -> ["python", "rust"]   (python weight=2, rust=1)
tt.top_k(2, now=60)    # weights halved: python=1.0, rust=0.5 -> same order
```

## Something to think about

Recomputing every topic's decayed weight on every `top_k` call is fine at
small scale. At Twitter scale (millions of topics, `top_k` called every
second for a live dashboard), what would you change? Think about
maintaining a heap incrementally vs. bucketing events into time windows.
