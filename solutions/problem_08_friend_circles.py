"""08. Social Network Friend Circles — see problems/08_friend_circles.md"""

from __future__ import annotations


class FriendCircles:
    def __init__(self) -> None:
        raise NotImplementedError

    def add_friendship(self, a: str, b: str) -> None:
        raise NotImplementedError

    def are_connected(self, a: str, b: str) -> bool:
        raise NotImplementedError

    def circle_size(self, a: str) -> int:
        raise NotImplementedError
