# 35. Invoice Split Checker

**Concept:** Equal-partition subset sum
**Real-world:** Two teams need to divide indivisible invoice line items into
two groups with exactly the same total. A group's line items form a
non-contiguous selection from the original invoice.

## Problem

```python
def can_split_invoice(amounts: list[int]) -> bool:
    """Return whether the line items can be partitioned into two groups with
    equal totals. Each amount belongs to exactly one group."""
```

## Requirements

- Run in O(n * total) time, where `total` is the sum of all amounts, and
  use O(total) or O(total / 2) space.
- If the total is odd, return `False` immediately. Otherwise determine if a
  non-contiguous subset reaches `total // 2`.
- Every amount is a positive integer and usable only once. Update reachable
  totals from high to low to avoid reusing a line item.
- Empty input can be split into two empty groups.

## Example

```python
can_split_invoice([1, 5, 11, 5])  # -> True   ([11] and [1, 5, 5])
can_split_invoice([1, 2, 3, 5])   # -> False
```

## Something to think about

Why is it enough to find just one group totaling half the invoice rather
than explicitly constructing both groups?
