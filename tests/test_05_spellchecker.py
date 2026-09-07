from solutions.problem_05_spellchecker import suggest

DICTIONARY = ["cat", "cot", "cost", "dog", "cats"]


def test_distance_one():
    assert suggest("cat", DICTIONARY, 1) == ["cat", "cot", "cats"]


def test_distance_zero_exact_only():
    assert suggest("cat", DICTIONARY, 0) == ["cat"]


def test_no_match():
    assert suggest("xyz", DICTIONARY, 1) == []


def test_sorted_by_distance_then_alpha():
    result = suggest("cost", DICTIONARY, 2)
    assert result == sorted(
        result,
        key=lambda w: (_edit_distance("cost", w), w),
    )


def _edit_distance(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            if ca == cb:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr
    return prev[-1]
