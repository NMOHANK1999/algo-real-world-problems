from solutions.problem_06_rate_limiter import RateLimiter


def test_allows_up_to_limit():
    rl = RateLimiter(max_requests=3, window_seconds=10)
    assert rl.allow_request("u1", 0) is True
    assert rl.allow_request("u1", 1) is True
    assert rl.allow_request("u1", 2) is True


def test_blocks_over_limit():
    rl = RateLimiter(max_requests=3, window_seconds=10)
    for t in (0, 1, 2):
        rl.allow_request("u1", t)
    assert rl.allow_request("u1", 3) is False


def test_window_slides():
    rl = RateLimiter(max_requests=3, window_seconds=10)
    for t in (0, 1, 2):
        rl.allow_request("u1", t)
    assert rl.allow_request("u1", 3) is False
    assert rl.allow_request("u1", 11) is True  # t=0 aged out of (1, 11]


def test_users_independent():
    rl = RateLimiter(max_requests=1, window_seconds=10)
    assert rl.allow_request("u1", 0) is True
    assert rl.allow_request("u2", 0) is True
    assert rl.allow_request("u1", 1) is False
