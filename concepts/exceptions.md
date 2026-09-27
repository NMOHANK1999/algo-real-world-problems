# Exceptions and error handling

An **exception** is Python's signal that normal execution cannot continue. For
example, converting `"five"` to an integer raises `ValueError`, and indexing
past the end of a list raises `IndexError`.

## Raising an exception

Use `raise` when your function detects invalid input that it cannot handle
correctly on its own.

```python
def minutes_between(start: int, end: int) -> int:
    if end < start:
        raise ValueError("end must not be before start")
    return end - start


assert minutes_between(10, 30) == 20
```

`raise ValueError(...)` immediately stops the function and sends the exception
to its caller. If nothing catches it, Python prints a traceback and ends the
program.

Use an exception when input violates a function's requirements. For an
expected outcome that is part of the problem's contract, a normal return value
can be clearer. Problem 10 asks for `None` when no complete assignment exists;
that is an expected search result, not necessarily a programming error.

## Catching a specific exception

Use `try` for the line that may fail and `except` for the exact error you know
how to handle.

```python
def parse_attendee_count(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


assert parse_attendee_count("12") == 12
assert parse_attendee_count("twelve") is None
```

Only `ValueError` is handled here. A different bug, such as `NameError`, is not
hidden; Python still reports it so you can fix it.

## Different errors need different handling

One `try` block can have several `except` clauses. Each handles its matching
error type.

```python
def describe_lookup(values: list[int], index_text: str) -> str:
    try:
        index = int(index_text)
        return str(values[index])
    except ValueError:
        return "The index must be a whole number."
    except IndexError:
        return "That index is outside the list."


assert describe_lookup([10, 20], "1") == "20"
assert describe_lookup([10, 20], "first") == "The index must be a whole number."
assert describe_lookup([10, 20], "5") == "That index is outside the list."
```

`int(index_text)` can raise `ValueError`; `values[index]` can raise
`IndexError`. The responses differ because the user can correct the two issues
in different ways.

## Order matters with related exception types

Exception classes form a hierarchy. A broad exception type must come after its
more specific types, or it will catch them first.

```python
try:
    number = int("not a number")
except ValueError:
    print("Please enter a number.")
except Exception:
    print("An unexpected error occurred.")
```

This works because `ValueError` is checked before the broader `Exception`.
Avoid a bare `except:` in normal application code: it can catch interrupts and
system-exit signals that should usually be allowed through.

## `else` and `finally`

- `else` runs only when the `try` block succeeds.
- `finally` runs whether the `try` block succeeds or fails. It is useful for
  cleanup, such as closing a file or releasing a resource.

```python
def read_first_line(path: str) -> str | None:
    file = None
    try:
        file = open(path, encoding="utf-8")
        return file.readline().rstrip("\n")
    except FileNotFoundError:
        return None
    finally:
        if file is not None:
            file.close()
```

For files, `with open(...) as file:` is usually simpler because Python closes
the file automatically. `finally` remains useful when cleanup must happen even
if a larger operation fails.

## Re-raising after adding context

Sometimes you want to log or add information but still let the caller decide
how to recover. Use a bare `raise` inside an `except` block to re-raise the same
exception.

```python
def load_count(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print("Could not load attendee count")
        raise
```

## Custom exception types

Create a custom exception when callers need to distinguish a domain-specific
error from ordinary Python errors.

```python
class InvalidMeetingTimeError(ValueError):
    pass


def validate_time_range(start: int, end: int) -> None:
    if end < start:
        raise InvalidMeetingTimeError("end must not be before start")


try:
    validate_time_range(60, 30)
except InvalidMeetingTimeError as error:
    assert str(error) == "end must not be before start"
```

In a small exercise, built-in exceptions such as `ValueError` are often enough.
Create custom types only when the distinction helps a caller respond
differently.

## Practical rules

- Catch the narrowest exception type you can handle correctly.
- Keep the `try` block small, so you know which line may have failed.
- Do not use exceptions to hide programming mistakes.
- Use `raise` when invalid input violates a function's requirements.
- Return a normal value such as `None` when failure is an expected result in the
  function's documented contract.
- Include a useful message when raising an exception.
