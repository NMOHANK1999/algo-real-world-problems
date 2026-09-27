# Backtracking

Backtracking is a way to search through possible choices. It builds a partial
answer one choice at a time. When a choice makes it impossible to finish, the
algorithm undoes that choice and tries another one.

The pattern is:

1. Choose an option.
2. Check whether the partial answer is still valid.
3. Recurse to make the next choice.
4. If that path fails, undo the choice.
5. Try the next option.

This is systematic trial and error. Unlike random guessing, backtracking keeps
track of where it is in the search and eventually considers every relevant
possibility.

## The decision-tree mental model

Imagine every partial answer as a node in a tree. Each branch represents one
possible next choice. Recursion moves down a branch. Returning from a recursive
call moves back up the tree.

For example, when building a two-character string from `A` and `B`, the search
tree is:

```text
             ""
           /    \
         "A"    "B"
        /  \    /  \
      "AA" "AB" "BA" "BB"
```

A constraint can cut off, or **prune**, a branch before the algorithm explores
everything below it.

## The five ingredients

Every backtracking problem has the same basic pieces:

- **State:** the partial answer built so far.
- **Choices:** the options available at the current step.
- **Constraints:** the rules that say whether a choice is allowed.
- **Base case / success case:** the condition that says the answer is complete.
- **Undo:** the operation that removes a failed choice before trying another.

Before writing code, try to identify each of these in plain language.

## Why recursion fits

Each recursive call solves the same smaller question:

> Given the choices already made, can I complete the rest of the answer?

The call returns success if one branch works. If every branch fails, it returns
failure to its caller. The caller can then undo its most recent choice and try
another option.

Here is the general shape:

```python
def search(state):
    if state_is_complete(state):
        return True

    for choice in available_choices(state):
        if not is_valid(choice, state):
            continue

        apply(choice, state)

        if search(state):
            return True

        undo(choice, state)

    return False
```

The exact state, choices, and checks change from problem to problem, but the
control flow stays similar.

## Example 1: generate binary strings

This example generates every binary string of a requested length. It has no
constraint, so no branches are pruned, but it shows the recursive decision
tree clearly.

```python
def binary_strings(length: int) -> list[str]:
    results: list[str] = []

    def build(prefix: str) -> None:
        # State: `prefix` is the partial answer built so far.

        # Base case / success case: the answer has the requested length.
        if len(prefix) == length:
            results.append(prefix)
            return

        # Choices: select either "0" or "1" as the next digit.
        # Constraints: none; both choices are always valid here.
        for digit in ("0", "1"):
            build(prefix + digit)
            # Undo: implicit. `prefix + digit` creates a new string, so the
            # caller's immutable `prefix` was never changed.

    build("")
    return results


assert binary_strings(2) == ["00", "01", "10", "11"]
```

## Example 2: choose, recurse, and undo

This version builds combinations in one shared mutable list. The `pop()` is the
undo step.

```python
def combinations(values: list[int], size: int) -> list[list[int]]:
    results: list[list[int]] = []
    current: list[int] = []

    def build(start: int) -> None:
        if len(current) == size:
            results.append(current.copy())
            return

        for index in range(start, len(values)):
            current.append(values[index])  # choose
            build(index + 1)               # recurse
            current.pop()                  # undo

    build(0)
    return results


assert combinations([1, 2, 3], 2) == [[1, 2], [1, 3], [2, 3]]
```

`current.copy()` matters. Appending `current` itself would store several
references to the same mutable list, which continues changing during the
search.

## Example 3: pruning invalid branches

The following search chooses numbers whose total must equal a target. It stops
exploring a branch as soon as its total becomes too large.

```python
def subset_with_sum(values: list[int], target: int) -> list[int] | None:
    chosen: list[int] = []

    def search(index: int, total: int) -> bool:
        if total == target:
            return True
        if index == len(values) or total > target:
            return False

        chosen.append(values[index])
        if search(index + 1, total + values[index]):
            return True
        chosen.pop()

        if search(index + 1, total):
            return True

        return False

    return chosen.copy() if search(0, 0) else None


assert subset_with_sum([3, 4, 6], 10) == [4, 6]
assert subset_with_sum([3, 4, 6], 2) is None
```

The `total > target` check is valid here because the example uses positive
numbers. If negative numbers were allowed, a later value could reduce the
total, so that pruning rule would not be correct.

## Pruning and ordering

Backtracking can be expensive because the decision tree may grow quickly.
Suppose each level has about `b` choices and the tree has depth `d`. The
worst-case running time is roughly:

```text
O(b^d)
```

Two ideas often make the real search much faster:

- **Pruning:** reject a partial answer as soon as it violates a constraint.
- **Most constrained first:** handle the item with the fewest legal choices
  first, so impossible branches tend to fail near the top of the tree.

These techniques reduce how much of the tree is explored. They usually do not
change the exponential worst case.

## Backtracking compared with related ideas

- **Greedy algorithms** make a locally attractive choice and do not undo it.
- **Brute force** may generate every complete possibility before checking it;
  backtracking can reject invalid partial answers early.
- **Depth-first search (DFS)** is a tree or graph traversal order. Backtracking
  commonly uses DFS, plus problem-specific choices, constraints, and undoing.
- **Dynamic programming** saves answers to repeated subproblems. It is useful
  when different search paths reach the same state, and it can sometimes be
  combined with backtracking.

## When to consider backtracking

Backtracking is often useful for:

- Sudoku and other constraint puzzles
- permutations and combinations
- path finding in mazes
- N-Queens
- scheduling and assignment problems
- requests to find one or all arrangements that satisfy several rules

Problem statements often hint at backtracking with phrases such as “find any
valid arrangement,” “find all possible arrangements,” or “assign every item
while obeying these constraints.”

## Common mistakes

- Forgetting to undo mutable state after a recursive call fails.
- Returning failure after the first choice fails instead of trying the rest.
- Treating a partial answer as if it reached the base case / success case.
- Checking constraints too late and exploring branches that are already invalid.
- Saving a mutable result without copying it.
- Using `return` when an invalid choice should use `continue`.
- Writing a pruning rule that is not logically safe for every allowed input.

## Questions for Problem 10

Without writing the solution yet, identify:

1. What does one level of the decision tree represent?
2. What choices are available at that level?
3. Which two constraints decide whether a choice is legal?
4. What information must the current state remember?
5. What must be undone when a deeper recursive call fails?
6. When is the assignment complete?
7. Which meeting would be “most constrained,” and why might considering it
   early reduce the amount of searching?

If these questions have precise answers, the recursive code usually becomes a
direct translation of the model.
