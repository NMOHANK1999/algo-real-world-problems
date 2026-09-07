# 02. LRU Cache Layer

**Concept:** Hash map + doubly linked list
**Real-world:** In-memory cache for a web service (Redis-style eviction).

## Problem

```python
class LRUCache:
    def __init__(self, capacity: int) -> None:
        """Cache holding at most `capacity` key/value pairs."""

    def get(self, key) -> object:
        """Return the value for key, or -1 if absent. Marks key as
        most-recently-used."""

    def put(self, key, value) -> None:
        """Insert or update key. If inserting a new key would exceed
        capacity, evict the least-recently-used entry first."""
```

## Requirements

- `get` and `put` must both be **O(1)** — no scanning a list to find the LRU
  entry.
- `put` on an existing key updates its value and marks it most-recently-used.

## Example

```python
cache = LRUCache(2)
cache.put(1, "a")
cache.put(2, "b")
cache.get(1)        # -> "a"   (1 is now most-recently-used)
cache.put(3, "c")   # evicts 2 (least-recently-used)
cache.get(2)        # -> -1
cache.put(4, "d")   # evicts 1
cache.get(1)        # -> -1
cache.get(3)        # -> "c"
cache.get(4)        # -> "d"
```

## Stretch (not covered by the tests — try it once the base case is green)

Add `get_with_ttl(key, now_timestamp)` where entries also expire after N
seconds regardless of recency. You'll need to combine the LRU list with a
way to find expired entries without scanning everything — think about what
a min-heap of expirations buys you here.
