# 19. Identity Resolution: Account Merger

**Concept:** Union-Find over a shared key (union items that share an
attribute)
**Real-world:** CRM de-duplication, fraud rings (accounts sharing a phone
or card), "sign in with Google" linking a legacy email account to a new
one.

## Problem

Each account is `(name, emails)`. Two accounts belong to the same person
if they share **at least one email** — and this is transitive (A shares
with B, B shares with C ⇒ A, B, C are one person).

```python
def merge_accounts(
    accounts: list[tuple[str, list[str]]],
) -> list[tuple[str, list[str]]]:
    """Merge accounts belonging to the same person. Each result is
    (name, sorted unique emails). The result list is sorted by
    (name, first email)."""
```

## Requirements

- Two different people can have the same **name** — name alone never
  links accounts. Only shared emails do.
- All accounts that get merged together are guaranteed to have the same
  name.
- An account may list the same email twice; the output has it once.
- Use Union-Find with path compression and union by rank/size. Union
  either account indices or emails — think about which is simpler.
- Should be about O(total_emails · α(n) + output sorting).

## Example

```python
accounts = [
    ("John", ["john@work.com", "john_home@mail.com"]),
    ("John", ["john@work.com", "j.smith@corp.com"]),
    ("Mary", ["mary@mail.com"]),
    ("John", ["johnny@other.com"]),
]
merge_accounts(accounts)
# -> [
#     ("John", ["j.smith@corp.com", "john@work.com", "john_home@mail.com"]),
#     ("John", ["johnny@other.com"]),
#     ("Mary", ["mary@mail.com"]),
# ]
```

## Something to think about

This is the same problem as "connected components of a bipartite graph
(accounts ↔ emails)." When would you prefer a DFS/BFS over that graph
instead of Union-Find? When is Union-Find clearly better (hint: accounts
arriving as a stream)?
