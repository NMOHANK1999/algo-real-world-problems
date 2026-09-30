# 12. Deadlock Detector

**Concept:** Cycle detection in a directed graph (three-color DFS)
**Real-world:** Database lock managers and OS schedulers build a
*wait-for graph* and look for cycles to detect deadlocks.

## Problem

`wait_for[p]` lists the processes that `p` is blocked waiting on. A cycle
means those processes are deadlocked; anything that (transitively) waits on
a deadlocked process is stuck too.

```python
def find_deadlock(wait_for: dict[str, list[str]]) -> list[str] | None:
    """Return one cycle as [p0, p1, ..., pk] where p0 waits on p1, p1 waits
    on p2, ..., and pk waits on p0. Return None if there is no cycle."""


def stuck_processes(wait_for: dict[str, list[str]]) -> set[str]:
    """All processes that can never finish: those on a cycle, plus those
    that can reach a cycle by following wait-for edges."""
```

## Requirements

- A process may appear only as a *target* (never as a key) — treat it as
  waiting on nothing.
- A self-loop (`"A": ["A"]`) is a cycle of length 1: `["A"]`.
- Use white/gray/black (unvisited / on current path / finished) coloring.
  A plain visited set can't tell "on my current path" (cycle!) apart from
  "finished earlier via another branch" (no cycle).
- Each process should be fully explored at most once — O(V + E) overall.
- Wait chains can be thousands of processes long; don't rely on
  Python's default recursion limit (~1000).

## Example

```python
wait_for = {
    "T1": ["T2"],
    "T2": ["T3"],
    "T3": ["T1"],   # T1 -> T2 -> T3 -> T1 deadlock
    "T4": ["T1"],   # T4 is stuck behind the deadlock
    "T5": ["T6"],   # T5 waits on T6, which is free
}
find_deadlock(wait_for)    # -> ["T1", "T2", "T3"] (any rotation is fine)
stuck_processes(wait_for)  # -> {"T1", "T2", "T3", "T4"}

find_deadlock({"A": ["B"], "B": []})  # -> None
```

## Something to think about

Real lock managers don't rerun a full DFS every time a lock is requested.
When a single new edge `p -> q` is added to an acyclic wait-for graph, what
is the cheapest check that tells you whether it just created a cycle?
