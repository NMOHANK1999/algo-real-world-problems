from solutions.problem_26_calendar_free_busy import (
    common_free_slots,
    merge_busy,
    min_rooms_needed,
)


def test_merge_busy():
    assert merge_busy([(9, 10), (1, 3), (2, 6), (6, 7)]) == [(1, 7), (9, 10)]


def test_merge_busy_nested_and_empty():
    assert merge_busy([(1, 10), (2, 3), (4, 5)]) == [(1, 10)]
    assert merge_busy([]) == []


def test_merge_busy_does_not_mutate():
    data = [(5, 6), (1, 2)]
    merge_busy(data)
    assert data == [(5, 6), (1, 2)]


def test_common_free_slots():
    alice = [(540, 600), (720, 780)]
    bob = [(570, 660), (900, 960)]
    assert common_free_slots([alice, bob], 480, 1020, 60) == [
        (480, 540), (660, 720), (780, 900), (960, 1020),
    ]


def test_common_free_slots_min_duration_filters():
    alice = [(540, 600), (720, 780)]
    bob = [(570, 660), (900, 960)]
    assert common_free_slots([alice, bob], 480, 1020, 90) == [(780, 900)]


def test_common_free_slots_busy_outside_day_is_clipped():
    cal = [(0, 500), (1000, 2000)]
    assert common_free_slots([cal], 480, 1020, 1) == [(500, 1000)]


def test_common_free_slots_nobody_busy():
    assert common_free_slots([[], []], 0, 100, 10) == [(0, 100)]


def test_common_free_slots_fully_booked():
    assert common_free_slots([[(0, 50)], [(50, 100)]], 0, 100, 1) == []


def test_min_rooms_needed():
    assert min_rooms_needed([(0, 30), (5, 10), (15, 20)]) == 2


def test_min_rooms_back_to_back_share_room():
    assert min_rooms_needed([(1, 5), (5, 10)]) == 1
    assert min_rooms_needed([(5, 10), (1, 5), (10, 15)]) == 1


def test_min_rooms_all_overlap_and_empty():
    assert min_rooms_needed([(1, 10), (2, 9), (3, 8), (4, 7)]) == 4
    assert min_rooms_needed([]) == 0
