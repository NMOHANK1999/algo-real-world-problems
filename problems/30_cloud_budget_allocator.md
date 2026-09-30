# 30. Cloud Budget Allocator

**Concept:** 0/1 knapsack dynamic programming (+ reconstructing the
chosen items) and subset-sum counting
**Real-world:** Picking which projects / reserved instances / features to
fund under a fixed budget to maximize value; counting how many bundles of
line items hit an invoice total exactly (reconciliation).

## Problem

```python
def best_allocation(
    projects: list[tuple[str, int, int]], budget: int
) -> tuple[int, list[str]]:
    """projects[i] = (name, cost, value). Each project is funded at most
    once, and total cost must be <= budget. Return (max_total_value,
    names of chosen projects in input order)."""


def ways_to_spend_exactly(costs: list[int], budget: int) -> int:
    """Number of subsets of costs (by position — equal costs at different
    positions are different items) whose sum is exactly budget. The empty
    subset counts when budget == 0."""
```

## Requirements

- O(n · budget) time for both. Trying all 2^n subsets won't pass a test
  with 60 projects.
- `best_allocation` must return the actual project names, so either keep
  the full 2D table `dp[i][b]` and walk it backwards, or record choices.
  (Bonus: do the value computation in a 1D array of size `budget + 1` —
  and understand why you iterate `b` from high to low.)
- If several selections tie on value, any one of them is accepted.
- Costs are positive integers; values are non-negative.

## Example

```python
projects = [
    ("observability", 3, 40),
    ("ci_speedup",    4, 50),
    ("db_upgrade",    2, 30),
    ("new_region",    5, 70),
]
best_allocation(projects, 7)
# -> (100, ["db_upgrade", "new_region"])      2 + 5 = 7, 30 + 70 = 100

ways_to_spend_exactly([2, 3, 5, 5], 10)
# -> 3   {5a, 5b}, {2, 3, 5a}, {2, 3, 5b}
```

## Something to think about

What changes if each project can be funded **any number of times**
(unbounded knapsack)? Look at the 1D loop — which single change in the
iteration direction switches between 0/1 and unbounded?
