# 18. Build Pipeline Paths

**Concept:** DFS + memoization on a DAG (counting paths, longest path)
**Real-world:** CI/CD pipelines and build graphs: "how many distinct
execution paths reach the deploy step?" and "what's the critical path —
the chain of steps that determines total pipeline duration?"

## Problem

`dag[step]` lists the steps that can run after `step`. The graph is
guaranteed acyclic.

```python
def count_paths(dag: dict[str, list[str]], src: str, dst: str) -> int:
    """Number of distinct paths from src to dst (src == dst counts as 1)."""


def critical_path(
    dag: dict[str, list[str]], durations: dict[str, int], src: str, dst: str
) -> tuple[int, list[str]] | None:
    """The src->dst path with the largest total duration (sum of
    durations of every step on it, both endpoints included).
    Returns (total, [src, ..., dst]), or None if dst is unreachable."""
```

## Requirements

- **Memoize.** The number of paths can be exponential in the number of
  steps (a chain of 40 "diamonds" has 2^40 paths). Enumerating paths one
  by one will never finish; `count(node) = sum(count(next))` with a cache
  is O(V + E).
- Steps that only appear as targets have no outgoing edges.
- `critical_path`: if several paths tie for the max, return any of them.
- Unknown `src` / unreachable `dst` → `count_paths` returns 0,
  `critical_path` returns None.

## Example

```text
checkout -> build -> test_unit ---> deploy
              \                     ^
               +--> test_integ -----+
```

```python
dag = {
    "checkout": ["build"],
    "build": ["test_unit", "test_integ"],
    "test_unit": ["deploy"],
    "test_integ": ["deploy"],
}
durations = {"checkout": 1, "build": 5, "test_unit": 2, "test_integ": 10, "deploy": 3}

count_paths(dag, "checkout", "deploy")
# -> 2
critical_path(dag, durations, "checkout", "deploy")
# -> (19, ["checkout", "build", "test_integ", "deploy"])
```

## Something to think about

Longest path is NP-hard on general graphs but linear on a DAG. What
property of DAGs makes the memoized recursion valid — and what exactly
goes wrong with the same code if there's a cycle?
