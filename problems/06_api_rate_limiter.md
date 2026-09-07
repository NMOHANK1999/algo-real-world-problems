# 06. API Rate Limiter

**Concept:** Sliding window
**Real-world:** Request throttling on an API gateway (Stripe/GitHub-style).

## Problem

```python
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float) -> None:
        """Allow at most max_requests per user in any rolling
        window_seconds-wide window."""

    def allow_request(self, user_id: str, timestamp: float) -> bool:
        """Return True and record the request if it's allowed under the
        limit; return False (and do NOT record it) otherwise."""
```

## Requirements

- The window is **rolling**, not fixed-bucket: a request at t=10.5 with a
  10s window looks back to t=0.5, not to the start of a fixed 10s bucket.
- Each `user_id` is limited independently.
- `timestamp` values arrive in non-decreasing order per user (you don't
  need to handle out-of-order timestamps).

## Example

```python
rl = RateLimiter(max_requests=3, window_seconds=10)
rl.allow_request("u1", 0)    # True  (1/3)
rl.allow_request("u1", 1)    # True  (2/3)
rl.allow_request("u1", 2)    # True  (3/3)
rl.allow_request("u1", 3)    # False (still 3 requests in [-7, 3])
rl.allow_request("u1", 11)   # True  (t=0 has aged out of the window (1, 11])
rl.allow_request("u2", 1)    # True  (separate user, separate budget)
```

## Something to think about

Implement it with a sliding-window **log** (store every timestamp) first.
Then think through a fixed-bucket-counter approximation — what accuracy do
you give up, and what do you gain in memory/CPU? When would each be the
right choice for a real gateway handling millions of users?
