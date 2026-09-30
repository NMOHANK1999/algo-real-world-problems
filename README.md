# Algo → Real World

Practice problems that take core algorithms/data-structure concepts (the
kind that show up across LeetCode 75-style lists) and frame them as the
production systems they actually power — autocomplete, caches, rate
limiters, dependency resolvers, and so on.

Each problem has three parts:

- `problems/NN_name.md` — the spec: real-world framing, requirements,
  signature, and examples.
- `solutions/problem_NN_name.py` — a stub with the class/function signature
  and docstring, raising `NotImplementedError`. Fill this in.
- `tests/test_NN_name.py` — pytest cases from the spec's examples. Red until
  you implement the solution.

## Concepts covered

| # | Problem | Concept | Real-world analogue |
|---|---------|---------|----------------------|
| 01 | Autocomplete Engine | Trie | Search-bar / IDE suggestions |
| 02 | LRU Cache Layer | Hash map + doubly linked list | In-memory cache (Redis-style eviction) |
| 03 | Dependency Resolver | Topological sort (BFS/DFS) | `npm install`, build/deploy ordering |
| 04 | Disk Usage Analyzer | DFS on a tree | `du -sh` |
| 05 | Typeahead Spell-Checker | Dynamic programming (edit distance) | "Did you mean...?" |
| 06 | API Rate Limiter | Sliding window | Request throttling / API gateway |
| 07 | Trending Topics Feed | Heap / priority queue | Live trending / leaderboard |
| 08 | Friend Circles | Union-Find | Connected components in a social graph |
| 09 | Route Planner | Graph search with constraints | Cheapest route with a stop limit |
| 10 | Room Assignment | Backtracking / CSP | Meeting-room scheduling |

### DFS deep-dive

| # | Problem | Concept | Real-world analogue |
|---|---------|---------|----------------------|
| 11 | Land Parcel Mapper | Grid DFS / flood fill (iterative) | Satellite segmentation, paint bucket |
| 12 | Deadlock Detector | Directed cycle detection (3-color DFS) | Lock manager wait-for graph |
| 13 | Service Cluster Finder | Strongly connected components (Tarjan/Kosaraju) | Circular microservice dependencies |
| 14 | Network Single Points of Failure | Bridges & articulation points (low-link) | Critical cables / routers |
| 15 | Org Chart Queries | Tree DFS, LCA, subtree sizes | Closest common manager, approval chains |
| 16 | Two-Shift Scheduler | Bipartite check (2-coloring) + odd-cycle proof | Conflict-free shift splitting |
| 17 | Config Tree Snapshotter | Tree serialize/deserialize (pre-order) | Config / DOM snapshots |
| 18 | Build Pipeline Paths | DFS + memoization on a DAG | CI path counting, critical path |

### Union-Find deep-dive

| # | Problem | Concept | Real-world analogue |
|---|---------|---------|----------------------|
| 19 | Account Merger | Union-Find over shared keys | CRM de-duplication, identity resolution |
| 20 | Currency Converter | Weighted Union-Find | FX conversion, inconsistent-rate detection |
| 21 | Fiber Network Planner | MST (Kruskal) + single-linkage clustering | Cheapest network layout |
| 22 | Datacenter Rack Power-On | Online Union-Find on a grid | Live segment count during bring-up |

### More core patterns

| # | Problem | Concept | Real-world analogue |
|---|---------|---------|----------------------|
| 23 | Packet Broadcast Latency | Dijkstra | Gossip / config-push latency, OSPF |
| 24 | Capacity Planner | Binary search on the answer | Right-sizing throughput for an SLA |
| 25 | Load Spike Alerts | Monotonic stack | "Next higher load", sustained capacity |
| 26 | Calendar Free/Busy | Interval merge + sweep line | "Find a time", room counts |
| 27 | Budget Window Counter | Prefix sums + hash map | Billing windows with refunds |
| 28 | Live Metrics Range Store | Fenwick tree (BIT) | Time-series range totals with updates |
| 29 | Malware Spread Simulator | Multi-source BFS | Infection spread, nearest-facility maps |
| 30 | Cloud Budget Allocator | 0/1 knapsack + subset-sum counting | Funding projects under a budget |

Several tests (11-16, 22-25, 28-29) include large inputs that catch
recursion-limit crashes or asymptotically slow solutions, not just
wrong answers.

## Workflow

1. Read the spec in `problems/`.
2. Run the matching test file — it should fail (`NotImplementedError`).
3. Implement the stub in `solutions/`.
4. Re-run the test until it's green, then think about complexity and edge
   cases before moving on.

## Setup

```bash
pip install -r requirements.txt
pytest tests/                 # run everything
pytest tests/test_01_autocomplete.py   # run one problem
```
