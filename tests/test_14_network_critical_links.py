from solutions.problem_14_network_critical_links import critical_links, critical_routers

LINKS = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]


def test_critical_links():
    assert critical_links(5, LINKS) == [(2, 3), (3, 4)]


def test_critical_routers():
    assert critical_routers(5, LINKS) == [2, 3]


def test_ring_has_no_single_point_of_failure():
    ring = [(i, (i + 1) % 6) for i in range(6)]
    assert critical_links(6, ring) == []
    assert critical_routers(6, ring) == []


def test_links_normalized_to_smaller_first():
    assert critical_links(2, [(1, 0)]) == [(0, 1)]
    assert critical_routers(2, [(1, 0)]) == []


def test_star_center_is_critical():
    star = [(0, 1), (0, 2), (0, 3)]
    assert critical_routers(4, star) == [0]
    assert critical_links(4, star) == [(0, 1), (0, 2), (0, 3)]


def test_disconnected_network():
    links = [(0, 1), (1, 2), (3, 4), (4, 5), (5, 3)]
    assert critical_links(7, links) == [(0, 1), (1, 2)]
    assert critical_routers(7, links) == [1]


def test_two_rings_sharing_a_router():
    links = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2)]
    assert critical_links(5, links) == []
    assert critical_routers(5, links) == [2]


def test_long_path_does_not_hit_recursion_limit():
    n = 3000
    links = [(i, i + 1) for i in range(n - 1)]
    assert len(critical_links(n, links)) == n - 1
    assert critical_routers(n, links) == list(range(1, n - 1))
