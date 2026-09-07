from solutions.problem_10_room_assignment import Meeting, Room, assign_rooms


def overlaps(m1: Meeting, m2: Meeting) -> bool:
    return m1.start < m2.end and m2.start < m1.end


def validate(meetings, rooms, assignment):
    room_by_name = {r.name: r for r in rooms}
    meeting_by_name = {m.name: m for m in meetings}
    assert set(assignment.keys()) == {m.name for m in meetings}

    for name, room_name in assignment.items():
        m = meeting_by_name[name]
        r = room_by_name[room_name]
        assert r.capacity >= m.attendees

    for a_name, a_room in assignment.items():
        for b_name, b_room in assignment.items():
            if a_name == b_name:
                continue
            if a_room == b_room and overlaps(
                meeting_by_name[a_name], meeting_by_name[b_name]
            ):
                raise AssertionError(f"{a_name} and {b_name} clash in {a_room}")


def test_feasible_assignment():
    meetings = [
        Meeting("standup", 0, 30, 5),
        Meeting("planning", 30, 90, 8),
        Meeting("1on1", 0, 30, 2),
    ]
    rooms = [Room("small", 3), Room("big", 10)]

    result = assign_rooms(meetings, rooms)
    assert result is not None
    validate(meetings, rooms, result)


def test_touching_endpoints_do_not_overlap():
    meetings = [
        Meeting("first", 0, 30, 5),
        Meeting("second", 30, 60, 5),
    ]
    rooms = [Room("only", 10)]
    result = assign_rooms(meetings, rooms)
    assert result == {"first": "only", "second": "only"}


def test_over_constrained_returns_none():
    meetings = [
        Meeting("a", 0, 60, 5),
        Meeting("b", 0, 60, 5),
        Meeting("c", 0, 60, 5),
    ]
    rooms = [Room("only_room", 10)]
    assert assign_rooms(meetings, rooms) is None


def test_meeting_too_big_for_any_room():
    meetings = [Meeting("huge", 0, 30, 100)]
    rooms = [Room("small", 3), Room("big", 10)]
    assert assign_rooms(meetings, rooms) is None


def test_requires_actual_backtracking():
    # Greedily filling "shared" first for "a" blocks "b", which only fits
    # in "shared". A correct solver must backtrack "a" onto "big" instead.
    meetings = [
        Meeting("a", 0, 30, 5),
        Meeting("b", 0, 30, 5),
    ]
    rooms = [Room("shared", 10), Room("big", 10)]
    result = assign_rooms(meetings, rooms)
    assert result is not None
    validate(meetings, rooms, result)
