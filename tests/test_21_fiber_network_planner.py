import random

from solutions.problem_21_fiber_network_planner import cluster_sites, plan_network

LINKS = [
    (0, 1, 4), (0, 2, 3), (1, 2, 1),
    (1, 3, 2), (2, 3, 4), (3, 4, 2),
]


def assert_spanning_tree(n, chosen, candidates):
    assert len(chosen) == n - 1
    cand = {(min(a, b), max(a, b), c) for a, b, c in candidates}
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b, c in chosen:
        assert (min(a, b), max(a, b), c) in cand
        ra, rb = find(a), find(b)
        assert ra != rb, "chosen links contain a cycle"
        parent[ra] = rb


def test_plan_network():
    total, chosen = plan_network(5, LINKS)
    assert total == 8
    assert sum(c for _, _, c in chosen) == 8
    assert_spanning_tree(5, chosen, LINKS)


def test_single_site():
    assert plan_network(1, []) == (0, [])


def test_disconnected_returns_none():
    assert plan_network(3, [(0, 1, 5)]) is None


def test_ignores_expensive_redundant_links():
    links = [(0, 1, 1), (1, 2, 1), (0, 2, 100)]
    total, chosen = plan_network(3, links)
    assert total == 2
    assert (0, 2, 100) not in chosen


def test_matches_brute_force_on_random_graphs():
    rng = random.Random(7)
    for _ in range(30):
        n = rng.randint(2, 7)
        links = [(a, b, rng.randint(1, 20)) for a in range(n) for b in range(a + 1, n) if rng.random() < 0.7]
        result = plan_network(n, links)
        best = None
        m = len(links)
        for mask in range(1 << m):
            subset = [links[i] for i in range(m) if mask >> i & 1]
            if len(subset) != n - 1:
                continue
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    x = parent[x]
                return x

            ok = True
            for a, b, _ in subset:
                ra, rb = find(a), find(b)
                if ra == rb:
                    ok = False
                    break
                parent[ra] = rb
            if ok:
                cost = sum(c for _, _, c in subset)
                best = cost if best is None else min(best, cost)
        if best is None:
            assert result is None
        else:
            assert result is not None and result[0] == best


def test_cluster_sites():
    assert cluster_sites(5, LINKS, 2) == [{0}, {1, 2, 3, 4}]


def test_cluster_sites_extremes():
    assert cluster_sites(5, LINKS, 1) == [{0, 1, 2, 3, 4}]
    assert cluster_sites(5, LINKS, 5) == [{0}, {1}, {2}, {3}, {4}]


def test_cluster_sites_two_obvious_groups():
    links = [(0, 1, 1), (1, 2, 1), (3, 4, 1), (4, 5, 1), (2, 3, 50), (0, 5, 60)]
    assert cluster_sites(6, links, 2) == [{0, 1, 2}, {3, 4, 5}]
