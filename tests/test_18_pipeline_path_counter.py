from solutions.problem_18_pipeline_path_counter import count_paths, critical_path

DAG = {
    "checkout": ["build"],
    "build": ["test_unit", "test_integ"],
    "test_unit": ["deploy"],
    "test_integ": ["deploy"],
}
DURATIONS = {"checkout": 1, "build": 5, "test_unit": 2, "test_integ": 10, "deploy": 3}


def diamond_chain(k):
    """k diamonds in a row: 2**k paths from n0 to n{k}."""
    dag = {}
    for i in range(k):
        dag[f"n{i}"] = [f"l{i}", f"r{i}"]
        dag[f"l{i}"] = [f"n{i + 1}"]
        dag[f"r{i}"] = [f"n{i + 1}"]
    return dag


def test_count_paths():
    assert count_paths(DAG, "checkout", "deploy") == 2


def test_count_paths_src_equals_dst():
    assert count_paths(DAG, "build", "build") == 1


def test_count_paths_unreachable():
    assert count_paths(DAG, "deploy", "checkout") == 0
    assert count_paths(DAG, "missing", "deploy") == 0


def test_count_paths_exponential_needs_memoization():
    assert count_paths(diamond_chain(40), "n0", "n40") == 2 ** 40


def test_critical_path():
    assert critical_path(DAG, DURATIONS, "checkout", "deploy") == (
        19,
        ["checkout", "build", "test_integ", "deploy"],
    )


def test_critical_path_single_step():
    assert critical_path(DAG, DURATIONS, "deploy", "deploy") == (3, ["deploy"])


def test_critical_path_unreachable():
    assert critical_path(DAG, DURATIONS, "deploy", "checkout") is None


def test_critical_path_on_large_dag():
    dag = diamond_chain(40)
    durations = {node: 1 for node in dag}
    durations["n40"] = 1
    durations["r7"] = 100
    total, path = critical_path(dag, durations, "n0", "n40")
    assert total == 81 + 99
    assert path[0] == "n0" and path[-1] == "n40"
    assert "r7" in path
    assert sum(durations[p] for p in path) == total
    for a, b in zip(path, path[1:]):
        assert b in dag[a]
