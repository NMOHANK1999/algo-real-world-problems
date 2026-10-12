# 33. Feature Rollout Adjuster

**Concept:** Difference array + prefix sum
**Real-world:** Operations schedules bulk capacity changes: add instances to
every availability zone in a range during a staged feature rollout.

## Problem

```python
def apply_capacity_changes(
    capacities: list[int], changes: list[tuple[int, int, int]]
) -> list[int]:
    """Apply every inclusive (start, end, delta) change and return the final
    capacities. Deltas may be negative."""
```

## Requirements

- Run in O(n + q), where n is the number of zones and q is the number of
  changes. Do not update every element for every change.
- Store each change's start and its cancelling value immediately after the
  end in a difference array; one prefix pass recovers the adjustment for each
  zone.
- Return a new list and do not mutate `capacities`.
- Input ranges are inclusive and valid. `capacities` may be empty only when
  `changes` is also empty.

## Example

```python
capacities = [10, 10, 10, 10, 10]
changes = [(1, 3, 5), (0, 1, -2), (3, 4, 1)]
apply_capacity_changes(capacities, changes)
# -> [8, 13, 15, 16, 11]
```

## Something to think about

The difference array is the discrete derivative of the final adjustments.
Why does taking a prefix sum reconstruct the original values?
