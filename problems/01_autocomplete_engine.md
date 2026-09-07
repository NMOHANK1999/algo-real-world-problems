# 01. Autocomplete Engine

**Concept:** Trie
**Real-world:** Search-bar / IDE code-completion suggestions.

## Problem

Implement `AutocompleteSystem`, a class that stores a vocabulary of weighted
words and returns ranked completions for a prefix.

```python
class AutocompleteSystem:
    def insert(self, word: str, freq: int) -> None:
        """Add or update a word with a frequency/weight."""

    def search(self, prefix: str, k: int) -> list[str]:
        """Return up to k completions for prefix, ordered by:
        1) highest freq first, 2) lexicographically for ties.
        """

    def type_char(self, c: str) -> list[str]:
        """Append c to the current query buffer and return search results
        (k=5) for the buffer so far. Simulates live typing."""

    def reset_query(self) -> None:
        """Clear the current query buffer (e.g. user cleared the search box)."""
```

## Requirements

- `search` must not scan the whole vocabulary — walk the trie to the prefix
  node, then collect completions from the subtree.
- `type_char` should be efficient for interactive use (called once per
  keystroke) — don't re-walk from the root of the whole word buffer if you
  can avoid it.
- Ties broken lexicographically, not by insertion order.

## Example

```python
ac = AutocompleteSystem()
ac.insert("cat", 5)
ac.insert("car", 5)
ac.insert("care", 3)
ac.insert("dog", 10)

ac.search("ca", 2)   # -> ["car", "cat"]   (freq tie -> lexicographic)
ac.search("care", 5) # -> ["care"]
ac.search("z", 5)    # -> []

ac.type_char("c")    # -> results for "c"
ac.type_char("a")    # -> results for "ca"
ac.reset_query()
ac.type_char("d")    # -> results for "d" -> ["dog"]
```

## Something to think about

How would you extend this so `insert` increments frequency on repeated
inserts (e.g. every time a user actually clicks a suggestion, its rank
should rise)?
