"""18. Build Pipeline Paths — see problems/18_pipeline_path_counter.md"""

from __future__ import annotations


def count_paths(dag: dict[str, list[str]], src: str, dst: str) -> int:
    ans = 0 
    if src == dst:
        return 1
    for child in dag[src]:
        ans += count_paths(dag, child, dst)
    return ans


def critical_path(
    dag: dict[str, list[str]], durations: dict[str, int], src: str, dst: str
) -> tuple[int, list[str]] | None:
    all_durations = []
    def dfs(sum_, src, dst):
        if src == dst:
            all_durations.append(sum_ + durations[dst])
            return
        for child in dag[src]:
            dfs(sum_ + durations[src], child, dst)
    dfs(0, src, dst)
    return max(all_durations)

dag = {
    "checkout": ["build"],
    "build": ["test_unit", "test_integ"],
    "test_unit": ["deploy"],
    "test_integ": ["deploy"],
}
durations = {"checkout": 1, "build": 5, "test_unit": 2, "test_integ": 10, "deploy": 3}

print(count_paths(dag, "checkout", "deploy"))
# -> 2
print(critical_path(dag, durations, "checkout", "deploy"))
# -> (19, ["checkout", "build", "test_integ", "deploy"])    