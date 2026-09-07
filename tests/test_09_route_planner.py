from solutions.problem_09_route_planner import cheapest_route

GRAPH = {
    "A": [("B", 100), ("C", 500)],
    "B": [("C", 100)],
    "C": [],
}


def test_direct_route_only():
    assert cheapest_route(GRAPH, "A", "C", max_stops=0) == 500


def test_route_with_one_stop_is_cheaper():
    assert cheapest_route(GRAPH, "A", "C", max_stops=1) == 200


def test_unreachable_destination():
    assert cheapest_route(GRAPH, "A", "Z", max_stops=5) == -1


def test_src_equals_dst():
    assert cheapest_route(GRAPH, "A", "A", max_stops=0) == 0


def test_not_enough_stops():
    graph = {
        "A": [("B", 1)],
        "B": [("C", 1)],
        "C": [("D", 1)],
        "D": [],
    }
    # A->B->C->D needs 2 intermediate stops
    assert cheapest_route(graph, "A", "D", max_stops=1) == -1
    assert cheapest_route(graph, "A", "D", max_stops=2) == 3
