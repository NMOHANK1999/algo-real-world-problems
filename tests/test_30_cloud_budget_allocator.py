import itertools
import random

from solutions.problem_30_cloud_budget_allocator import best_allocation, ways_to_spend_exactly

PROJECTS = [
    ("observability", 3, 40),
    ("ci_speedup", 4, 50),
    ("db_upgrade", 2, 30),
    ("new_region", 5, 70),
]


def assert_valid_allocation(result, projects, budget, expected_value):
    value, names = result
    assert value == expected_value
    by_name = {p[0]: p for p in projects}
    order = [p[0] for p in projects]
    assert names == sorted(names, key=order.index), "names must be in input order"
    assert len(set(names)) == len(names)
    assert sum(by_name[n][1] for n in names) <= budget
    assert sum(by_name[n][2] for n in names) == value


def test_best_allocation_example():
    assert best_allocation(PROJECTS, 7) == (100, ["db_upgrade", "new_region"])


def test_best_allocation_zero_budget_and_empty():
    assert best_allocation(PROJECTS, 0) == (0, [])
    assert best_allocation([], 10) == (0, [])


def test_best_allocation_everything_fits():
    assert best_allocation(PROJECTS, 100) == (190, [p[0] for p in PROJECTS])


def test_best_allocation_greedy_by_ratio_fails():
    # Best value/cost ratio is "a", but taking it blocks the optimal pair.
    projects = [("a", 6, 65), ("b", 5, 50), ("c", 5, 50)]
    assert_valid_allocation(best_allocation(projects, 10), projects, 10, 100)


def test_best_allocation_matches_brute_force():
    rng = random.Random(2)
    for _ in range(40):
        projects = [(f"p{i}", rng.randint(1, 8), rng.randint(0, 30)) for i in range(rng.randint(1, 8))]
        budget = rng.randint(0, 25)
        best = 0
        for r in range(len(projects) + 1):
            for combo in itertools.combinations(projects, r):
                if sum(p[1] for p in combo) <= budget:
                    best = max(best, sum(p[2] for p in combo))
        assert_valid_allocation(best_allocation(projects, budget), projects, budget, best)


def test_best_allocation_many_projects():
    rng = random.Random(8)
    projects = [(f"p{i}", rng.randint(1, 50), rng.randint(1, 100)) for i in range(60)]
    value, names = best_allocation(projects, 500)
    assert_valid_allocation((value, names), projects, 500, value)
    assert value > 0


def test_ways_to_spend_exactly():
    assert ways_to_spend_exactly([2, 3, 5, 5], 10) == 3


def test_ways_to_spend_exactly_zero_budget():
    assert ways_to_spend_exactly([1, 2], 0) == 1
    assert ways_to_spend_exactly([], 0) == 1
    assert ways_to_spend_exactly([], 5) == 0


def test_ways_to_spend_exactly_duplicates_count_separately():
    assert ways_to_spend_exactly([1, 1, 1], 2) == 3


def test_ways_to_spend_exactly_large():
    assert ways_to_spend_exactly([1] * 60, 30) == 118264581564861424
