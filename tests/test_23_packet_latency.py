import random
import time

from solutions.problem_23_packet_latency import broadcast_time, fastest_route

LINKS = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]


def test_broadcast_time():
    assert broadcast_time(4, LINKS, 0) == 4


def test_broadcast_unreachable():
    assert broadcast_time(3, [(0, 1, 1)], 0) == -1


def test_broadcast_single_node():
    assert broadcast_time(1, [], 0) == 0


def test_links_are_directed():
    assert broadcast_time(2, [(1, 0, 1)], 0) == -1


def test_parallel_links_and_zero_weights():
    links = [(0, 1, 10), (0, 1, 3), (1, 2, 0)]
    assert broadcast_time(3, links, 0) == 3
    assert fastest_route(3, links, 0, 2) == (3, [0, 1, 2])


def test_fastest_route():
    assert fastest_route(4, LINKS, 0, 3) == (4, [0, 2, 1, 3])


def test_fastest_route_to_self():
    assert fastest_route(4, LINKS, 2, 2) == (0, [2])


def test_fastest_route_unreachable():
    assert fastest_route(4, LINKS, 3, 0) is None


def test_large_graph_is_fast():
    rng = random.Random(1)
    n = 20_000
    links = [(i, i + 1, rng.randint(1, 10)) for i in range(n - 1)]
    links += [(rng.randrange(n), rng.randrange(n), rng.randint(1, 100)) for _ in range(80_000)]
    start = time.perf_counter()
    t = broadcast_time(n, links, 0)
    elapsed = time.perf_counter() - start
    assert t > 0
    assert elapsed < 3.0, f"took {elapsed:.2f}s"
    total, path = fastest_route(n, links, 0, n - 1)
    weight = {}
    for u, v, w in links:
        weight[(u, v)] = min(w, weight.get((u, v), w))
    assert sum(weight[(a, b)] for a, b in zip(path, path[1:])) == total
