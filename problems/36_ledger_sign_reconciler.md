# 36. Ledger Sign Reconciler

**Concept:** Target-sum dynamic programming
**Real-world:** A reconciliation tool receives absolute transaction amounts
and must decide whether each was a charge or credit. Count the distinct sign
assignments that produce a requested ending balance.

## Problem

```python
def count_ledger_reconciliations(amounts: list[int], target: int) -> int:
    """Return the number of ways to put a '+' or '-' before every amount so
    the signed total equals target. Equal amounts at different positions are
    distinct transactions."""
```

## Requirements

- Use dynamic programming, not all 2^n sign assignments. O(n * sum(amounts))
  time is acceptable.
- You may keep a mapping from reachable signed totals to their number of
  ways, or transform the problem into a subset-counting problem.
- Zeros double the number of assignments because both signs are distinct.
- Return 0 when the target cannot be reached. Amounts are non-negative.

## Example

```python
count_ledger_reconciliations([1, 1, 1, 1, 1], 3)  # -> 5
count_ledger_reconciliations([1, 2, 3], 10)       # -> 0
```

## Something to think about

If P is the sum of the amounts assigned '+', how can you express P using
the total of all amounts and the requested target?
