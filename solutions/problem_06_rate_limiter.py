"""06. API Rate Limiter — see problems/06_api_rate_limiter.md"""

from __future__ import annotations


class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float) -> None:
        raise NotImplementedError

    def allow_request(self, user_id: str, timestamp: float) -> bool:
        raise NotImplementedError
