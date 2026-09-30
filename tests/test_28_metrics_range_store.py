import random
import time

from solutions.problem_28_metrics_range_store import MetricsStore


def test_example():
    m = MetricsStore([5, 2, 7, 1, 3])
    assert m.range_sum(0, 4) == 18
    assert m.range_sum(1, 3) == 10
    m.update(2, 0)
    assert m.range_sum(1, 3) == 3
    assert m.first_bucket_reaching(7) == 1
    assert m.first_bucket_reaching(8) == 3
    assert m.first_bucket_reaching(99) == -1


def test_single_bucket_range():
    m = MetricsStore([4, 9, 1])
    assert m.range_sum(1, 1) == 9
    m.update(1, -3)
    assert m.range_sum(0, 2) == 2


def test_update_is_set_not_add():
    m = MetricsStore([1, 1, 1])
    m.update(0, 10)
    m.update(0, 10)
    assert m.range_sum(0, 0) == 10


def test_first_bucket_reaching_edges():
    m = MetricsStore([0, 0, 3, 0, 4])
    assert m.first_bucket_reaching(0) == 0
    assert m.first_bucket_reaching(1) == 2
    assert m.first_bucket_reaching(3) == 2
    assert m.first_bucket_reaching(7) == 4
    assert m.first_bucket_reaching(8) == -1


def test_matches_naive_under_random_operations():
    rng = random.Random(9)
    for n in (1, 2, 7, 16, 33):
        values = [rng.randint(0, 20) for _ in range(n)]
        m = MetricsStore(list(values))
        for _ in range(200):
            op = rng.random()
            if op < 0.4:
                i = rng.randrange(n)
                values[i] = rng.randint(0, 20)
                m.update(i, values[i])
            elif op < 0.8:
                left = rng.randrange(n)
                right = rng.randrange(left, n)
                assert m.range_sum(left, right) == sum(values[left:right + 1])
            else:
                t = rng.randint(0, sum(values) + 5)
                running, expected = 0, -1
                for i, v in enumerate(values):
                    running += v
                    if running >= t:
                        expected = i
                        break
                assert m.first_bucket_reaching(t) == expected


def test_large_workload_is_fast():
    rng = random.Random(0)
    n = 100_000
    values = [rng.randint(0, 1000) for _ in range(n)]
    start = time.perf_counter()
    m = MetricsStore(values)
    total = 0
    for _ in range(20_000):
        m.update(rng.randrange(n), rng.randint(0, 1000))
        total += m.range_sum(0, n - 1)
        m.first_bucket_reaching(rng.randint(0, 1000 * n // 2))
    elapsed = time.perf_counter() - start
    assert total > 0
    assert elapsed < 5.0, f"took {elapsed:.2f}s — are range queries O(n)?"
