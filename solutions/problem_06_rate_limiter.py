"""06. API Rate Limiter — see problems/06_api_rate_limiter.md"""

from __future__ import annotations
from collections import deque

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.time_calls = {}

    def allow_request(self, user_id: str, timestamp: float) -> bool:
        if user_id not in self.time_calls:
            self.time_calls[user_id] = deque()

        while self.time_calls[user_id] and self.time_calls[user_id][0] <= timestamp - self.window_seconds:
            # print("popped ", self.time_calls[user_id] ,"for", user_id)
            self.time_calls[user_id].popleft()
            # print("popped ", self.time_calls[user_id] ,"for", user_id)

        if len(self.time_calls[user_id]) < self.max_requests:
            self.time_calls[user_id].append(timestamp)
            return True
        else:
            return False

rl = RateLimiter(max_requests=3, window_seconds=10)

assert rl.allow_request("u1", 0)    # True  (1/3)
assert rl.allow_request("u1", 1)    # True  (2/3)
# print(rl.allow_request("u1", 2))
assert rl.allow_request("u1", 2)    # True  (3/3)
assert not rl.allow_request("u1", 3)    # False (still 3 requests in [-7, 3])
assert rl.allow_request("u1", 11)   # True  (t=0 has aged out of the window (1, 11])
assert rl.allow_request("u2", 1)    # True  (separate user, separate budget)