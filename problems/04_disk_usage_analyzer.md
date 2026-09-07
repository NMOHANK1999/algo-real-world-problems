# 04. File System Disk Usage Analyzer

**Concept:** DFS on a tree
**Real-world:** `du -sh` / storage-usage dashboards.

## Problem

Given a filesystem represented as a nested dict:

```python
node = {
    "name": "root",
    "size": 0,          # 0 for directories, own byte size for files
    "children": [ ... ]  # list of child nodes, [] for files
}
```

```python
def total_size(node: dict) -> int:
    """Total bytes used by this node and everything under it."""


def largest_n_files(node: dict, n: int) -> list[str]:
    """Names of the n largest files (not directories) anywhere in the
    tree, largest first. Ties broken by name."""
```

## Requirements

- `total_size` must correctly sum only actual file sizes (directories
  contribute 0 of their own, but their children's sizes roll up).
- `largest_n_files` only considers leaf files (`children == []`), not
  directories, even if a directory's rolled-up size is large.

## Example

```python
tree = {
    "name": "root", "size": 0, "children": [
        {"name": "a.txt", "size": 100, "children": []},
        {"name": "docs", "size": 0, "children": [
            {"name": "b.txt", "size": 300, "children": []},
            {"name": "c.txt", "size": 50, "children": []},
        ]},
    ],
}

total_size(tree)          # -> 450
largest_n_files(tree, 2)  # -> ["b.txt", "a.txt"]
```

## Something to think about

The spec says "symlinks could create cycles." If a `children` list could
reference a node that's also its own ancestor, what breaks in a naive DFS,
and what's the minimal fix?
