# 13. Service Cluster Finder

**Concept:** Strongly connected components (Tarjan's or Kosaraju's
algorithm — both are DFS-based)
**Real-world:** Finding groups of microservices that call each other in a
loop (they must be deployed / versioned together), module import cycles,
"circular dependency" reports in build tools.

## Problem

`calls[s]` lists the services that service `s` calls directly.

```python
def service_clusters(calls: dict[str, list[str]]) -> list[set[str]]:
    """Partition every service into strongly connected components: two
    services are in the same cluster iff each can reach the other."""


def deploy_order(calls: dict[str, list[str]]) -> list[set[str]]:
    """The same clusters, ordered so that if any service in cluster X calls
    a service in cluster Y (X != Y), then Y comes before X — callees are
    deployed before their callers."""
```

## Requirements

- Every service appears in exactly one cluster, including services that
  only appear as call targets and services in no cycle (a cluster of 1).
- O(V + E). Running a reachability search from every node (O(V·(V+E)))
  is too slow for the spirit of the problem.
- Order of clusters in `service_clusters` doesn't matter.

## Example

```python
calls = {
    "api":     ["auth", "orders"],
    "auth":    ["users"],
    "users":   ["auth"],           # auth <-> users loop
    "orders":  ["billing"],
    "billing": ["ledger"],
    "ledger":  ["orders"],         # orders -> billing -> ledger -> orders
}
service_clusters(calls)
# -> [{"api"}, {"auth", "users"}, {"orders", "billing", "ledger"}]  (any order)

deploy_order(calls)
# -> [{"auth", "users"}, {"orders", "billing", "ledger"}, {"api"}]
#    (the first two may be swapped; "api" must come last)
```

## Something to think about

Tarjan's algorithm emits SCCs in *reverse* topological order of the
condensed graph "for free." Why? And what does the condensed graph (one
node per SCC) always look like — can it ever have a cycle?
