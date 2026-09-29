"""04. Disk Usage Analyzer — see problems/04_disk_usage_analyzer.md"""

from __future__ import annotations


def total_size(node: dict) -> int:
    if len(node['children']) == 0:
        return node['size']
    total = 0
    for child in node['children']:
        total += total_size(child)
    return total

import heapq

def largest_n_files(node: dict, n: int) -> list[str]:
    files = []

    def dfs(curr):
        if not curr["children"]:
            files.append((curr["size"], curr["name"]))
            return

        for child in curr["children"]:
            dfs(child)

    dfs(node)
    files.sort(key=lambda x: (-x[0], x[1]))  # largest size, then name
    return [name for _, name in files[:n]]


tree = {
    "name": "root", "size": 0, "children": [
        {"name": "a.txt", "size": 100, "children": []},
        {"name": "docs", "size": 0, "children": [
            {"name": "b.txt", "size": 300, "children": []},
            {"name": "c.txt", "size": 50, "children": []},
        ]},
    ],
}

print(total_size(tree))
# assert total_size(tree) == 450         # -> 450
print(largest_n_files(tree, 2))  # -> ["b.txt", "a.txt"]