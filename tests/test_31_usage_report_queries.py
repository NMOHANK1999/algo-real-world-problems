import random
import time

from solutions.problem_31_usage_report_queries import first_day_reaching, usage_totals


def test_usage_totals_example():
    usage = [5, 2, 7, 1, 3]
    assert usage_totals(usage, [(0, 4), (1, 3), (2, 2)]) == [18, 10, 7]


def test_usage_totals_single_days_and_empty_queries():
    assert usage_totals([4, 0, 6], [(0, 0), (1, 1), (2, 2)]) == [4, 0, 6]
    assert usage_totals([], []) == []


def test_first_day_reaching_edges():
    assert first_day_reaching([5, 2, 7, 1, 3], 0) == 0
    assert first_day_reaching([5, 2, 7, 1, 3], 7) == 1
    assert first_day_reaching([5, 2, 7, 1, 3], 8) == 2
    assert first_day_reaching([5, 2, 7, 1, 3], 99) == -1
    assert first_day_reaching([], 0) == -1


def test_usage_totals_matches_sum():
    rng = random.Random(31)
    for _ in range(50):
        usage = [rng.randint(0, 20) for _ in range(rng.randint(1, 30))]
        queries = []
        for _ in range(30):
            start = rng.randrange(len(usage))
            end = rng.randrange(start, len(usage))
            queries.append((start, end))
        assert usage_totals(usage, queries) == [sum(usage[a:b + 1]) for a, b in queries]


def test_many_queries_are_fast():
    usage = [1] * 100_000
    queries = [(0, 99_999)] * 100_000
    start = time.perf_counter()
    assert usage_totals(usage, queries)[-1] == 100_000
    assert time.perf_counter() - start < 2.0
