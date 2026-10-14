"""31. Usage Report Queries — see problems/31_usage_report_queries.md"""

from __future__ import annotations


def usage_totals(
    usage: list[int], queries: list[tuple[int, int]]
) -> list[int]:
    presum = []
    ans = []
    for ind, use in enumerate(usage):
        if ind == 0:
            presum.append(use)
        else:
            presum.append(presum[ind -1 ] + use) 

    for a, b in queries:
        if a == 0:
            ans.append(presum[b])
        else:
            ans.append(presum[b] - presum[a-1])
    return ans

def first_day_reaching(usage: list[int], threshold: int) -> int:
    presum = 0
    for ind, use in enumerate(usage):
        presum += use
        if presum >= threshold:
            return ind
    return -1

usage = [5, 2, 7, 1, 3]
assert usage_totals(usage, [(0, 4), (1, 3), (2, 2)]) == [18, 10, 7] # -> [18, 10, 7]
assert first_day_reaching(usage, 7) == 1                    # -> 1
assert first_day_reaching(usage, 8) == 2                   # -> 2
assert first_day_reaching(usage, 99) == -1                   # -> -1