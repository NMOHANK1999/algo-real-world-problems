"""10. Meeting Room Assignment — see problems/10_room_assignment.md"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Meeting:
    name: str
    start: int
    end: int
    attendees: int


@dataclass(frozen=True)
class Room:
    name: str
    capacity: int
     
def assign_rooms(meetings: list[Meeting], rooms: list[Room]) -> dict[str, str] | None:
    result = {}

    bookingTime = {room.name: [] for room in rooms}

    #state = meetNum
    def backtrack(meetNum):

        #base condition
        if meetNum == len(meetings):
            return True
        
        meet = meetings[meetNum]

        #options
        for room in rooms:
            if room.capacity < meet.attendees:
                continue
            if not all( 
                meet.end <= bookstart or bookend <= meet.start
                for bookstart, bookend in bookingTime[room.name]
                ):
                continue
            bookingTime[room.name].append((meet.start, meet.end))
            result[meet.name] = room.name
            if backtrack(meetNum + 1):
                return True
            del result[meet.name]
            bookingTime[room.name].pop()
        return False

    return result if backtrack(0) else {}


# 1 
result = assign_rooms([], [])
print(result)
assert result == {}
print("Pass 1\n")

# 2
meetings = [
    Meeting("standup", 0, 30, 5),
    Meeting("planning", 30, 90, 8),
    Meeting("1on1", 0, 30, 2),
]
rooms = [Room("small", 3), Room("big", 10)]

result = assign_rooms(meetings, rooms)
print(result)
assert result == {"standup": "big", "planning": "big", "1on1": "small"}
print("Pass 2\n")
# 3
meetings = [
    Meeting("a", 0, 60, 5),
    Meeting("b", 0, 60, 5),
    Meeting("c", 0, 60, 5),
]
rooms = [Room("only_room", 10)]
result = assign_rooms(meetings, rooms)
print(result)
assert result == None
print("Pass 3\n")

