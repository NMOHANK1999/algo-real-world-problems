import pytest

from solutions.problem_03_dependency_resolver import CycleError, resolve_order


def test_valid_order_respects_dependencies():
    packages = ["A", "B", "C", "D"]
    deps = [("B", "A"), ("C", "A"), ("D", "B"), ("D", "C")]
    order = resolve_order(packages, deps)

    assert set(order) == set(packages)
    pos = {pkg: i for i, pkg in enumerate(order)}
    assert pos["A"] < pos["B"]
    assert pos["A"] < pos["C"]
    assert pos["B"] < pos["D"]
    assert pos["C"] < pos["D"]


def test_isolated_package_included():
    order = resolve_order(["A", "B", "Z"], [("B", "A")])
    assert set(order) == {"A", "B", "Z"}


def test_cycle_raises():
    with pytest.raises(CycleError):
        resolve_order(["A", "B", "C"], [("A", "B"), ("B", "C"), ("C", "A")])


def test_no_deps():
    order = resolve_order(["A", "B", "C"], [])
    assert set(order) == {"A", "B", "C"}
