# 05. Typeahead Spell-Checker

**Concept:** Dynamic programming (edit distance / Levenshtein distance)
**Real-world:** "Did you mean...?" in a search engine.

## Problem

```python
def suggest(word: str, dictionary: list[str], max_dist: int) -> list[str]:
    """Return every dictionary word within `max_dist` edits (insert,
    delete, substitute) of `word`, sorted by distance ascending, then
    alphabetically for ties."""
```

## Requirements

- Implement edit distance yourself with DP (no library shortcuts) —
  `dp[i][j]` = edit distance between `word[:i]` and `candidate[:j]`.
- Only return words with distance `<= max_dist`, in the sorted order
  described above.

## Example

```python
dictionary = ["cat", "cot", "cost", "dog", "cats"]
suggest("cat", dictionary, 1)   # -> ["cat", "cot", "cats"]
suggest("cat", dictionary, 0)   # -> ["cat"]
suggest("xyz", dictionary, 1)   # -> []
```

## Stretch (not covered by the tests)

Brute-force DP against every dictionary word is O(len(word) * len(candidate))
per word. For a dictionary of a million words this is too slow to run on
every keystroke. Look up **BK-trees** (built on the triangle inequality of
edit distance) and sketch how you'd restructure `suggest` around one instead
of iterating the whole dictionary.
