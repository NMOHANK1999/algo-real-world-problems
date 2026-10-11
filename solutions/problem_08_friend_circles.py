"""08. Social Network Friend Circles — see problems/08_friend_circles.md"""

from __future__ import annotations


class FriendCircles:

    def __repr__(self):
        return str(self.friends)


    def __init__(self) -> None:
        self.friends = {}

    def boss_friend(self, child):
        top = child
        while self.friends[top] != top:
            top = self.friends[top]
        self.friends[child] = top
        return top
        

    def add_friendship(self, a: str, b: str) -> None:
        if a not in self.friends:
            self.friends[a] = a
        if b not in self.friends:
            self.friends[b] = b

        top_a =  self.boss_friend(a)
        top_b = self.boss_friend(b)
        if self.circle_size(top_a) >= self.circle_size(top_b):
            self.friends[top_b] = top_a
        else:
            self.friends[top_a] = top_b

    def are_connected(self, a: str, b: str) -> bool:
        return self.boss_friend(a) == self.boss_friend(b)

    def circle_size(self, a: str) -> int:
        ans = 0
        boss_a = self.boss_friend(a)
        for key, _ in self.friends.items():
            # if key != a:
            if self.boss_friend(key) == a:
                ans += 1
        return ans

fc = FriendCircles()
fc.add_friendship("alice", "bob")
fc.add_friendship("bob", "carol")
fc.add_friendship("dave", "erin")

print(fc)

assert (fc.are_connected("alice", "carol") == True)  # -> True  (via bob)
assert (fc.are_connected("alice", "dave") == False)   # -> False
assert (fc.circle_size("alice") == 3)            # -> 3  (alice, bob, carol)
assert (fc.circle_size("dave") == 2)        # -> 2
