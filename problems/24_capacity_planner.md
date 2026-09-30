# 24. Capacity Planner

**Concept:** Binary search on the answer (monotonic feasibility check)
**Real-world:** "What's the smallest instance size / throughput / batch
limit that still meets the SLA?" — right-sizing infra without trying
every value.

## Problem

```python
def min_batch_capacity(job_sizes: list[int], max_batches: int) -> int:
    """Jobs must be shipped IN ORDER in consecutive batches. Each batch's
    total size must be <= capacity. Return the smallest capacity that
    ships everything in at most max_batches batches."""


def min_drain_rate(queue_depths: list[int], hours: int) -> int:
    """A worker drains one queue per hour, up to `rate` messages from that
    queue (if fewer remain, the rest of the hour is wasted). Return the
    smallest integer rate that empties all queues within `hours` hours.
    Assume len(queue_depths) <= hours."""
```

## Requirements

- Both answers are **monotonic**: if capacity `c` works, `c + 1` works.
  Binary search over the answer range with an O(n) feasibility check:
  O(n log(range)).
- Pick your bounds carefully:
  - capacity is at least `max(job_sizes)` and at most `sum(job_sizes)`.
  - rate is at least 1 and at most `max(queue_depths)`.
- Tests use 10^5 jobs with sizes up to 10^9 — linear scanning of
  candidate capacities will time out.
- Empty `job_sizes` → 0. Empty `queue_depths` → 0.

## Example

```python
min_batch_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
# -> 15   batches: [1..5] [6,7] [8] [9] [10]

min_batch_capacity([3, 2, 2, 4, 1, 4], 3)
# -> 6    batches: [3,2] [2,4] [1,4]

min_drain_rate([3, 6, 7, 11], 8)
# -> 4    hours needed: 1 + 2 + 2 + 3 = 8
```

## Something to think about

The feasibility check for `min_batch_capacity` is greedy: pack each batch
as full as possible. Prove to yourself that greedy packing never uses
more batches than an optimal packing for the same capacity.
