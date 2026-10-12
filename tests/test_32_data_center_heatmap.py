import random
import time

from solutions.problem_32_data_center_heatmap import HeatmapTotals


def test_rectangle_totals_example():
    heatmap = HeatmapTotals([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5]])
    assert heatmap.rectangle_total(0, 0, 2, 4) == 36
    assert heatmap.rectangle_total(1, 1, 2, 3) == 14


def test_rectangle_totals_edges_and_single_cell():
    heatmap = HeatmapTotals([[2, -1], [4, 3]])
    assert heatmap.rectangle_total(0, 0, 0, 1) == 1
    assert heatmap.rectangle_total(0, 0, 1, 0) == 6
    assert heatmap.rectangle_total(1, 1, 1, 1) == 3


def test_rectangle_totals_match_brute_force():
    rng = random.Random(32)
    readings = [[rng.randint(-5, 10) for _ in range(9)] for _ in range(8)]
    heatmap = HeatmapTotals(readings)
    for _ in range(100):
        top = rng.randrange(8)
        bottom = rng.randrange(top, 8)
        left = rng.randrange(9)
        right = rng.randrange(left, 9)
        expected = sum(sum(row[left:right + 1]) for row in readings[top:bottom + 1])
        assert heatmap.rectangle_total(top, left, bottom, right) == expected


def test_many_large_rectangle_queries_are_fast():
    readings = [[1] * 500 for _ in range(500)]
    start = time.perf_counter()
    heatmap = HeatmapTotals(readings)
    assert all(heatmap.rectangle_total(0, 0, 499, 499) == 250_000 for _ in range(20_000))
    assert time.perf_counter() - start < 2.0
