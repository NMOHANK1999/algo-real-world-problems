import pytest

from solutions.problem_04_disk_usage import largest_n_files, total_size


@pytest.fixture
def tree():
    return {
        "name": "root", "size": 0, "children": [
            {"name": "a.txt", "size": 100, "children": []},
            {"name": "docs", "size": 0, "children": [
                {"name": "b.txt", "size": 300, "children": []},
                {"name": "c.txt", "size": 50, "children": []},
            ]},
        ],
    }


def test_total_size(tree):
    assert total_size(tree) == 450


def test_total_size_empty_dir():
    empty = {"name": "root", "size": 0, "children": []}
    assert total_size(empty) == 0


def test_largest_n_files(tree):
    assert largest_n_files(tree, 2) == ["b.txt", "a.txt"]


def test_largest_n_files_more_than_exist(tree):
    result = largest_n_files(tree, 10)
    assert result == ["b.txt", "a.txt", "c.txt"]
