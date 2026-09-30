# 17. Config Tree Snapshotter

**Concept:** Tree serialization / deserialization with DFS (pre-order
traversal + a self-delimiting encoding)
**Real-world:** Saving a hierarchical config (feature flags, a DOM, a UI
component tree, a filesystem manifest) to a string and restoring it
exactly — the core of every snapshot / undo / caching system.

## Problem

```python
@dataclass
class ConfigNode:
    key: str
    children: list[ConfigNode] = field(default_factory=list)


def serialize(root: ConfigNode | None) -> str:
    """Encode the whole tree as a single string."""


def deserialize(data: str) -> ConfigNode | None:
    """Rebuild the exact tree: deserialize(serialize(t)) == t."""
```

`ConfigNode` is already defined in the stub. Because it's a dataclass,
`==` compares key and children recursively (see
`concepts/dataclasses.md`).

## Requirements

- Keys may contain **any** characters: commas, brackets, spaces, quotes,
  newlines, digits, the empty string, emoji. Whatever delimiter you pick
  will show up inside some key, so you need either escaping or
  length-prefixing (e.g. `"5:hello"`).
- Child order matters and must be preserved.
- `serialize(None)` must round-trip back to `None`.
- Don't use `json`, `pickle`, `repr`/`eval`, or similar — the point is to
  design the encoding yourself.
- Pre-order DFS works naturally: write a node's key and child count, then
  recurse into each child. Reading it back is the same walk.

## Example

```python
tree = ConfigNode("root", [
    ConfigNode("db", [ConfigNode("host=localhost"), ConfigNode("port=5432")]),
    ConfigNode("flags", [ConfigNode("dark_mode")]),
])
data = serialize(tree)          # e.g. "4:root2|2:db2|14:host=localhost0|..."
deserialize(data) == tree       # -> True
deserialize(serialize(None))    # -> None
```

## Something to think about

A 10,000-level-deep tree (a long linked chain) will blow Python's recursion
limit in both directions. How do you serialize and deserialize with an
explicit stack while keeping the exact same output format?
