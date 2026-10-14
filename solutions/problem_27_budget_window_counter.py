"""27. Budget Window Counter — see problems/27_budget_window_counter.md"""

from __future__ import annotations

def count_windows_with_total(costs: list[int], target: int) -> int:
    map_costs = {0:1}
    prefixSum = 0
    ans = 0
    for cost in costs:
        prefixSum += cost
        ans += map_costs.get(prefixSum - target, 0)
        map_costs[prefixSum]  = map_costs.get(prefixSum, 0) + 1
    return ans

def longest_balanced_window(events: list[str]) -> int:
    sumpos = {0:[0]}
    prefixSum = 0
    maxDist = 0

    for ind, event in enumerate(events):
        print(ind)
        if event == "in":
            prefixSum += 1
        else:
            prefixSum -= 1
        if prefixSum in sumpos:
            maxDist = max(maxDist, ind - min(sumpos[prefixSum]))
        if prefixSum not in sumpos:
            sumpos[prefixSum] = []
        sumpos[prefixSum].append(ind)
    return maxDist

if __name__ == "__main__":
    assert count_windows_with_total([1, 1, 1], 2) == 2 , "❌ test 1"          # -> 2
    print("✅")
    assert count_windows_with_total([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4  , "❌ test 1"# -> 4
    print("✅")
    assert count_windows_with_total([0, 0, 0], 0)  == 6  , "❌ test 1"         # -> 6
    print("✅")
    assert longest_balanced_window(["in", "out", "in", "in", "out", "out", "in"]) == 6, "value is {}".format(longest_balanced_window(["in", "out", "in", "in", "out", "out", "in"]))  # -> 6
    print("✅")
    assert longest_balanced_window(["in", "in"]) == 0                                 # -> 0
    print("✅")