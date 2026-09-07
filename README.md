# Algo → Real World

Ten practice problems that take core algorithms/data-structure concepts (the
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
