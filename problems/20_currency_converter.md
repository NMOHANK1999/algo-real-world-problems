# 20. Currency Converter

**Concept:** Weighted Union-Find (each node stores its ratio to its
parent; path compression multiplies ratios along the way)
**Real-world:** FX conversion from a sparse set of quoted pairs, unit
conversion systems, detecting arbitrage / inconsistent price feeds.

## Problem

```python
class CurrencyConverter:
    def add_rate(self, src: str, dst: str, rate: float) -> None:
        """Record that 1 unit of src == rate units of dst (rate > 0).
        Raises ValueError if this contradicts rates already implied by
        earlier calls (relative difference > 1e-9)."""

    def convert(self, amount: float, src: str, dst: str) -> float | None:
        """Convert amount of src into dst using any chain of known rates.
        None if either currency is unknown or they aren't connected."""
```

## Requirements

- Near-O(1) amortized per call. Don't BFS the rate graph on every
  `convert`.
- Store, for every currency `x`, `weight[x]` = value of 1 `x` measured in
  units of its parent. Then `find(x)` returns `(root, ratio_of_x_to_root)`
  and compresses the path by multiplying ratios.
- When unioning two roots, work out the new edge's weight algebraically
  from `rate` and the two ratios-to-root. Draw it out.
- `convert(a, "X", "X")` returns `a` if X is known, None otherwise.
- Re-adding a rate that's consistent with what's already known is fine
  (no error, no change).

## Example

```python
fx = CurrencyConverter()
fx.add_rate("USD", "EUR", 0.9)
fx.add_rate("EUR", "JPY", 160.0)
fx.add_rate("GBP", "USD", 1.25)

fx.convert(10, "USD", "JPY")   # -> 1440.0   (10 * 0.9 * 160)
fx.convert(1, "GBP", "EUR")    # -> 1.125
fx.convert(1440, "JPY", "USD") # -> 10.0
fx.convert(1, "USD", "INR")    # -> None

fx.add_rate("GBP", "JPY", 200.0)  # ValueError — implied rate is 180.0
```

## Something to think about

In a real market, rates *are* slightly inconsistent — that's arbitrage.
To find a profitable cycle you take `-log(rate)` as edge weights and look
for a negative cycle. Which shortest-path algorithm detects negative
cycles, and why can't Dijkstra?
