import random
import time

from solutions.problem_24_capacity_planner import min_batch_capacity, min_drain_rate


def test_min_batch_capacity_examples():
    assert min_batch_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert min_batch_capacity([3, 2, 2, 4, 1, 4], 3) == 6


def test_min_batch_capacity_bounds():
    jobs = [7, 2, 5, 10, 8]
    assert min_batch_capacity(jobs, 1) == sum(jobs)
    assert min_batch_capacity(jobs, len(jobs)) == max(jobs)
    assert min_batch_capacity(jobs, 100) == max(jobs)


def test_min_batch_capacity_empty():
    assert min_batch_capacity([], 3) == 0


def test_min_drain_rate_examples():
    assert min_drain_rate([3, 6, 7, 11], 8) == 4
    assert min_drain_rate([30, 11, 23, 4, 20], 5) == 30
    assert min_drain_rate([30, 11, 23, 4, 20], 6) == 23


def test_min_drain_rate_edge_cases():
    assert min_drain_rate([], 5) == 0
    assert min_drain_rate([1], 1) == 1
    assert min_drain_rate([10], 100) == 1


def test_large_inputs_are_fast():
    rng = random.Random(3)
    jobs = [rng.randint(1, 10**9) for _ in range(100_000)]
    start = time.perf_counter()
    cap = min_batch_capacity(jobs, 50)
    rate = min_drain_rate(jobs, 250_000)
    elapsed = time.perf_counter() - start
    assert max(jobs) <= cap <= sum(jobs)
    assert 1 <= rate <= max(jobs)
    assert elapsed < 5.0, f"took {elapsed:.2f}s"

    def batches_needed(c):
        count, cur = 1, 0
        for j in jobs:
            if cur + j > c:
                count, cur = count + 1, 0
            cur += j
        return count

    assert batches_needed(cap) <= 50 < batches_needed(cap - 1)
    hours = lambda r: sum(-(-q // r) for q in jobs)  # noqa: E731
    assert hours(rate) <= 250_000 < hours(rate - 1)
