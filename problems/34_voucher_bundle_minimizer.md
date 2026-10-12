# 34. Voucher Bundle Minimizer

**Concept:** 0/1 minimum-coin dynamic programming
**Real-world:** A checkout system has one-time credits. Find the smallest
number of distinct vouchers that covers an invoice exactly.

## Problem

```python
def minimum_vouchers_for_total(vouchers: list[int], total: int) -> int:
    """Return the fewest vouchers whose values sum exactly to total, or -1
    when no non-contiguous selection can do so. Every position is usable at
    most once, even if values repeat."""
```

## Requirements

- Use O(n * total) time and O(total) space.
- This resembles Coin Change, but it is **not** the unlimited-coin version:
  each voucher is a one-time item. Iterate totals from high to low so the
  current voucher cannot be reused in the same pass.
- Return 0 when `total` is 0. Voucher values are positive.
- A greedy choice can fail, and a test has enough vouchers to rule out
  enumerating every subsequence.

## Example

```python
minimum_vouchers_for_total([1, 3, 4, 8], 11)  # -> 2  (3 + 8)
minimum_vouchers_for_total([2, 4, 6], 5)      # -> -1
```

## Something to think about

What changes if every voucher value is available an unlimited number of
times? Which direction would the inner loop go?
