from solutions.problem_12_deadlock_detector import find_deadlock, stuck_processes

WAIT_FOR = {
    "T1": ["T2"],
    "T2": ["T3"],
    "T3": ["T1"],
    "T4": ["T1"],
    "T5": ["T6"],
}


def assert_valid_cycle(cycle, wait_for):
    assert cycle, "expected a non-empty cycle"
    assert len(set(cycle)) == len(cycle), "cycle must not repeat processes"
    for i, proc in enumerate(cycle):
        nxt = cycle[(i + 1) % len(cycle)]
        assert nxt in wait_for.get(proc, []), f"{proc} does not wait on {nxt}"


def test_finds_cycle():
    cycle = find_deadlock(WAIT_FOR)
    assert_valid_cycle(cycle, WAIT_FOR)
    assert set(cycle) == {"T1", "T2", "T3"}


def test_no_cycle_returns_none():
    assert find_deadlock({"A": ["B"], "B": []}) is None
    assert find_deadlock({}) is None


def test_diamond_is_not_a_cycle():
    # A reaches D via two paths; D is "finished", not "on the current path".
    wait_for = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert find_deadlock(wait_for) is None
    assert stuck_processes(wait_for) == set()


def test_self_loop():
    assert find_deadlock({"A": ["A"]}) == ["A"]


def test_cycle_not_reachable_from_first_key():
    wait_for = {"A": ["B"], "B": [], "X": ["Y"], "Y": ["Z"], "Z": ["X"]}
    cycle = find_deadlock(wait_for)
    assert_valid_cycle(cycle, wait_for)
    assert set(cycle) == {"X", "Y", "Z"}


def test_stuck_processes():
    assert stuck_processes(WAIT_FOR) == {"T1", "T2", "T3", "T4"}


def test_long_chain_into_cycle():
    wait_for = {f"P{i}": [f"P{i + 1}"] for i in range(2000)}
    wait_for["P2000"] = ["P1999"]
    stuck = stuck_processes(wait_for)
    assert stuck == {f"P{i}" for i in range(2001)}
    cycle = find_deadlock(wait_for)
    assert_valid_cycle(cycle, wait_for)
    assert set(cycle) == {"P1999", "P2000"}
