# 08. Social Network Friend Circles

**Concept:** Union-Find (Disjoint Set Union)
**Real-world:** "People you may know" / connected components in a social
graph.

## Problem

```python
class FriendCircles:
    def add_friendship(self, a: str, b: str) -> None:
        """Record that a and b are friends (undirected)."""

    def are_connected(self, a: str, b: str) -> bool:
        """True if a and b are in the same friend circle (directly or
        transitively connected)."""

    def circle_size(self, a: str) -> int:
        """Number of people in a's friend circle, including a."""
```

## Requirements

- Use union by rank/size **and** path compression — both, not just one.
  Near-O(1) amortized per operation.
- A person mentioned only via `add_friendship` and never explicitly
  "added" separately still works — no separate `add_person` call needed.
- `are_connected(a, a)` is `True`; `circle_size` of someone never mentioned
  should behave sensibly (define and document what you chose — 1, or an
  error, are both defensible; be explicit about which).

## Example

```python
fc = FriendCircles()
fc.add_friendship("alice", "bob")
fc.add_friendship("bob", "carol")
fc.add_friendship("dave", "erin")

fc.are_connected("alice", "carol")  # -> True  (via bob)
fc.are_connected("alice", "dave")   # -> False
fc.circle_size("alice")             # -> 3  (alice, bob, carol)
fc.circle_size("dave")              # -> 2
```

## Something to think about

The spec asks you to also sketch (not implement, unless you want to)
`remove_friendship(a, b)`. Union-Find can't undo a union efficiently —
why not? What data structure *would* support efficient add and remove of
edges while still answering "are these connected"?
