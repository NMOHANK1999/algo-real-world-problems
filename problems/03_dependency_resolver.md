# 03. Dependency Resolver / Build System

**Concept:** Topological sort (BFS Kahn's algorithm, or DFS)
**Real-world:** `npm install`, Makefile target ordering, microservice deploy
ordering.

## Problem

```python
class CycleError(Exception):
    """Raised when the dependency graph contains a cycle."""


def resolve_order(packages: list[str], deps: list[tuple[str, str]]) -> list[str]:
    """
    packages: all package names that must appear in the output.
    deps: list of (package, depends_on) pairs meaning `package` requires
          `depends_on` to be installed first.

    Returns a valid install order (a topological sort). Raises CycleError
    if the graph has a cycle.
    """
```

## Requirements

- Output must place every dependency before the packages that need it.
- Must detect cycles and raise `CycleError` rather than looping forever or
  silently dropping packages.
- Isolated packages (no deps, nothing depends on them) still appear in the
  output.

## Example

```python
packages = ["A", "B", "C", "D"]
deps = [("B", "A"), ("C", "A"), ("D", "B"), ("D", "C")]
resolve_order(packages, deps)
# valid outputs: ["A", "B", "C", "D"] or ["A", "C", "B", "D"]
# (A must come first, D must come last, B/C order between them is free)

resolve_order(["A", "B", "C"], [("A", "B"), ("B", "C"), ("C", "A")])
# raises CycleError
```

## Something to think about

If two valid orderings exist, does your implementation return a
deterministic one? What would you change to make it always prefer
alphabetical order among packages with no remaining constraints?
