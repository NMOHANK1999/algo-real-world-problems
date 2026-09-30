import random
import time

from solutions.problem_27_budget_window_counter import (
    count_windows_with_total,
    longest_balanced_window,
)


def test_count_windows_examples():
    assert count_windows_with_total([1, 1, 1], 2) == 2
    assert count_windows_with_total([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4


def test_count_windows_zeros():
    assert count_windows_with_total([0, 0, 0], 0) == 6


def test_count_windows_none_and_empty():
    assert count_windows_with_total([1, 2, 3], 100) == 0
    assert count_windows_with_total([], 0) == 0


def test_count_windows_matches_brute_force():
    rng = random.Random(11)
    for _ in range(100):
        costs = [rng.randint(-5, 5) for _ in range(rng.randint(0, 12))]
        target = rng.randint(-6, 6)
        expected = sum(
            1 for i in range(len(costs)) for j in range(i, len(costs)) if sum(costs[i:j + 1]) == target
        )
        assert count_windows_with_total(costs, target) == expected


def test_longest_balanced_window():
    assert longest_balanced_window(["in", "out", "in", "in", "out", "out", "in"]) == 6


def test_longest_balanced_window_none():
    assert longest_balanced_window(["in", "in"]) == 0
    assert longest_balanced_window([]) == 0


def test_longest_balanced_window_whole_list():
    assert longest_balanced_window(["out", "in", "in", "out"]) == 4


def test_large_inputs_are_fast():
    n = 200_000
    costs = [1] * n
    start = time.perf_counter()
    assert count_windows_with_total(costs, 1) == n
    assert longest_balanced_window(["in", "out"] * (n // 2)) == n
    assert time.perf_counter() - start < 3.0
