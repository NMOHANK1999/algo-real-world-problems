# 15. Org Chart Queries

**Concept:** DFS on a tree — parent pointers, depths, lowest common
ancestor (LCA), subtree sizes
**Real-world:** HR systems ("who's the closest manager both of these people
report to?"), approval-chain routing, permissions inherited down a
hierarchy.

## Problem

```python
class OrgChart:
    def __init__(self, reports: dict[str, list[str]], ceo: str) -> None:
        """reports[m] = direct reports of manager m. Everyone is reachable
        from ceo. People with no reports may be missing as keys."""

    def closest_common_manager(self, a: str, b: str) -> str:
        """Lowest person who is (a or a manager of a) AND (b or a manager
        of b). If a manages b (directly or transitively), returns a."""

    def chain_of_command(self, employee: str) -> list[str]:
        """[ceo, ..., employee] — the path from the top down."""

    def team_size(self, manager: str) -> int:
        """Number of people who report to manager directly or
        transitively (not counting the manager)."""
```

## Requirements

- Do the tree walk **once** in `__init__` (record parent, depth, and
  subtree size for everyone). After that:
  - `team_size` is O(1).
  - `closest_common_manager` is O(depth) — walk the deeper person up until
    depths match, then walk both up together.
- Unknown employee names raise `KeyError`.
- The org can be deep (think a 5000-level chain in a test) — don't
  recurse in `__init__`.

## Example

```text
            ceo
          /     \
       cto       cfo
      /   \        \
   eng1   eng2     acct1
    |
  intern
```

```python
org = OrgChart(
    {"ceo": ["cto", "cfo"], "cto": ["eng1", "eng2"],
     "cfo": ["acct1"], "eng1": ["intern"]},
    ceo="ceo",
)
org.closest_common_manager("intern", "eng2")   # -> "cto"
org.closest_common_manager("intern", "acct1")  # -> "ceo"
org.closest_common_manager("cto", "intern")    # -> "cto"
org.chain_of_command("intern")                 # -> ["ceo", "cto", "eng1", "intern"]
org.team_size("cto")                           # -> 3
org.team_size("eng2")                          # -> 0
```

## Something to think about

If you had to answer millions of `closest_common_manager` queries on a
very deep org chart, O(depth) per query might be too slow. Look up
*binary lifting*: precompute each person's 1st, 2nd, 4th, 8th, ... manager.
What does that buy you per query, and what does it cost up front?
