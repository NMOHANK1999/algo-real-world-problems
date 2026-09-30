import random
import time

from solutions.problem_25_load_spike_alerts import (
    hours_until_higher_load,
    largest_sustained_block,
)


def test_hours_until_higher_load():
    assert hours_until_higher_load([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_hours_until_higher_load_equal_values_are_not_higher():
    assert hours_until_higher_load([5, 5, 5, 6]) == [3, 2, 1, 0]


def test_hours_until_higher_load_decreasing_and_empty():
    assert hours_until_higher_load([5, 4, 3]) == [0, 0, 0]
    assert hours_until_higher_load([]) == []


def test_largest_sustained_block():
    assert largest_sustained_block([2, 1, 5, 6, 2, 3]) == 10


def test_largest_sustained_block_edge_cases():
    assert largest_sustained_block([]) == 0
    assert largest_sustained_block([7]) == 7
    assert largest_sustained_block([3, 3, 3, 3]) == 12
    assert largest_sustained_block([1, 2, 3, 4, 5]) == 9


def test_matches_brute_force():
    rng = random.Random(5)
    for _ in range(50):
        loads = [rng.randint(0, 10) for _ in range(rng.randint(1, 15))]
        expected_next = []
        for i, x in enumerate(loads):
            wait = next((j - i for j in range(i + 1, len(loads)) if loads[j] > x), 0)
            expected_next.append(wait)
        assert hours_until_higher_load(loads) == expected_next
        best = max(min(loads[i:j + 1]) * (j - i + 1) for i in range(len(loads)) for j in range(i, len(loads)))
        assert largest_sustained_block(loads) == best


def test_large_input_is_fast():
    n = 200_000
    loads = list(range(n, 0, -1))
    start = time.perf_counter()
    assert hours_until_higher_load(loads) == [0] * n
    assert largest_sustained_block(loads) == (n // 2) * (n - n // 2 + 1)
    assert time.perf_counter() - start < 3.0
