import random
import time

from solutions.problem_22_rack_power_on import segments_after_each_power_on


def brute_force(rows, cols, positions):
    on = set()
    out = []
    for p in positions:
        on.add(p)
        seen = set()
        count = 0
        for cell in on:
            if cell in seen:
                continue
            count += 1
            stack = [cell]
            seen.add(cell)
            while stack:
                r, c = stack.pop()
                for nb in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if nb in on and nb not in seen:
                        seen.add(nb)
                        stack.append(nb)
        out.append(count)
    return out


def test_example():
    assert segments_after_each_power_on(3, 3, [(0, 0), (0, 1), (1, 2), (2, 1), (1, 1)]) == [1, 1, 2, 3, 1]


def test_duplicate_power_on_is_noop():
    assert segments_after_each_power_on(2, 2, [(0, 0), (0, 0), (1, 1), (1, 1)]) == [1, 1, 2, 2]


def test_diagonal_does_not_connect():
    assert segments_after_each_power_on(2, 2, [(0, 0), (1, 1), (0, 1)]) == [1, 2, 1]


def test_empty():
    assert segments_after_each_power_on(3, 3, []) == []


def test_matches_brute_force_on_random_inputs():
    rng = random.Random(42)
    for _ in range(20):
        rows, cols = rng.randint(1, 6), rng.randint(1, 6)
        positions = [(rng.randrange(rows), rng.randrange(cols)) for _ in range(rng.randint(1, 25))]
        assert segments_after_each_power_on(rows, cols, positions) == brute_force(rows, cols, positions)


def test_large_floor_is_fast():
    n = 150
    positions = [(r, c) for r in range(n) for c in range(n)]
    random.Random(0).shuffle(positions)
    start = time.perf_counter()
    result = segments_after_each_power_on(n, n, positions)
    elapsed = time.perf_counter() - start
    assert len(result) == n * n
    assert result[-1] == 1
    assert elapsed < 3.0, f"took {elapsed:.2f}s — is this O(k * rows * cols)?"
