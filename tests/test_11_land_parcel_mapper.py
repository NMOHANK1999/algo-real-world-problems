import copy

from solutions.problem_11_land_parcel_mapper import (
    count_parcels,
    fill_region,
    largest_parcel,
)

GRID = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"],
]


def test_count_parcels():
    assert count_parcels(GRID) == 2


def test_diagonal_cells_are_separate_parcels():
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ]
    assert count_parcels(grid) == 5
    assert largest_parcel(grid) == 1


def test_largest_parcel():
    assert largest_parcel(GRID) == 3


def test_empty_and_all_water():
    assert count_parcels([]) == 0
    assert largest_parcel([]) == 0
    assert count_parcels([[]]) == 0
    assert count_parcels([["0", "0"], ["0", "0"]]) == 0
    assert largest_parcel([["0", "0"], ["0", "0"]]) == 0


def test_does_not_mutate_grid():
    grid = copy.deepcopy(GRID)
    count_parcels(grid)
    largest_parcel(grid)
    assert grid == GRID


def test_large_grid_does_not_hit_recursion_limit():
    grid = [["1"] * 300 for _ in range(300)]
    assert count_parcels(grid) == 1
    assert largest_parcel(grid) == 90_000


def test_fill_region():
    image = [
        [1, 1, 0],
        [1, 0, 0],
        [1, 1, 1],
    ]
    original = copy.deepcopy(image)
    result = fill_region(image, 0, 0, 7)
    assert result == [
        [7, 7, 0],
        [7, 0, 0],
        [7, 7, 7],
    ]
    assert image == original


def test_fill_region_same_color_is_noop():
    image = [[2, 2], [2, 0]]
    assert fill_region(image, 0, 0, 2) == [[2, 2], [2, 0]]


def test_fill_region_only_touches_connected_cells():
    image = [
        [5, 0, 5],
        [0, 0, 0],
        [5, 0, 5],
    ]
    assert fill_region(image, 1, 1, 9) == [
        [5, 9, 5],
        [9, 9, 9],
        [5, 9, 5],
    ]
