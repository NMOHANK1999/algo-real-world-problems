import random
import time

from solutions.problem_33_feature_rollout_adjuster import apply_capacity_changes


def test_capacity_changes_example():
    assert apply_capacity_changes([10, 10, 10, 10, 10], [(1, 3, 5), (0, 1, -2), (3, 4, 1)]) == [8, 13, 15, 16, 11]


def test_capacity_changes_empty_and_single_zone():
    assert apply_capacity_changes([], []) == []
    assert apply_capacity_changes([4], [(0, 0, -3), (0, 0, 10)]) == [11]


def test_capacity_changes_match_direct_updates():
    rng = random.Random(33)
    for _ in range(50):
        capacities = [rng.randint(-10, 10) for _ in range(rng.randint(1, 30))]
        changes = []
        expected = list(capacities)
        for _ in range(30):
            start = rng.randrange(len(capacities))
            end = rng.randrange(start, len(capacities))
            delta = rng.randint(-5, 5)
            changes.append((start, end, delta))
            for index in range(start, end + 1):
                expected[index] += delta
        assert apply_capacity_changes(capacities, changes) == expected


def test_many_overlapping_changes_are_fast():
    capacities = [0] * 100_000
    changes = [(0, 99_999, 1)] * 100_000
    start = time.perf_counter()
    assert apply_capacity_changes(capacities, changes)[50_000] == 100_000
    assert time.perf_counter() - start < 2.0
