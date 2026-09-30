from solutions.problem_16_shift_splitter import odd_conflict_cycle, split_into_two_shifts


def assert_valid_split(result, n, conflicts):
    assert result is not None
    day, night = result
    assert day | night == set(range(n))
    assert not day & night
    for a, b in conflicts:
        assert (a in day) != (b in day), f"{a} and {b} share a shift"


def assert_valid_odd_cycle(cycle, conflicts):
    assert cycle is not None
    assert len(cycle) % 2 == 1
    assert len(set(cycle)) == len(cycle)
    edges = {frozenset(c) for c in conflicts}
    for i, w in enumerate(cycle):
        assert frozenset((w, cycle[(i + 1) % len(cycle)])) in edges


def test_path_is_splittable():
    conflicts = [(0, 1), (1, 2), (2, 3)]
    result = split_into_two_shifts(4, conflicts)
    assert_valid_split(result, 4, conflicts)
    assert {frozenset(result[0]), frozenset(result[1])} == {frozenset({0, 2}), frozenset({1, 3})}


def test_triangle_is_not_splittable():
    assert split_into_two_shifts(3, [(0, 1), (1, 2), (2, 0)]) is None


def test_workers_without_conflicts_are_placed():
    result = split_into_two_shifts(5, [(0, 1)])
    assert_valid_split(result, 5, [(0, 1)])


def test_disconnected_components():
    conflicts = [(0, 1), (2, 3), (3, 4), (4, 5), (5, 2)]
    assert_valid_split(split_into_two_shifts(6, conflicts), 6, conflicts)


def test_odd_cycle_in_second_component():
    conflicts = [(0, 1), (2, 3), (3, 4), (4, 2)]
    assert split_into_two_shifts(5, conflicts) is None


def test_odd_conflict_cycle_triangle():
    conflicts = [(0, 1), (1, 2), (2, 0)]
    assert_valid_odd_cycle(odd_conflict_cycle(3, conflicts), conflicts)


def test_odd_conflict_cycle_none_when_bipartite():
    assert odd_conflict_cycle(4, [(0, 1), (1, 2), (2, 3), (3, 0)]) is None


def test_odd_conflict_cycle_pentagon_with_tail():
    conflicts = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 2)]
    cycle = odd_conflict_cycle(7, conflicts)
    assert_valid_odd_cycle(cycle, conflicts)
    assert set(cycle) == {2, 3, 4, 5, 6}


def test_large_even_ring():
    n = 4000
    conflicts = [(i, (i + 1) % n) for i in range(n)]
    assert_valid_split(split_into_two_shifts(n, conflicts), n, conflicts)
