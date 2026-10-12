import itertools
import random

from solutions.problem_35_invoice_split_checker import can_split_invoice


def test_invoice_split_examples():
    assert can_split_invoice([1, 5, 11, 5]) is True
    assert can_split_invoice([1, 2, 3, 5]) is False


def test_invoice_split_empty_single_and_odd_total():
    assert can_split_invoice([]) is True
    assert can_split_invoice([4]) is False
    assert can_split_invoice([2, 3, 4]) is False


def test_invoice_split_matches_brute_force():
    rng = random.Random(35)
    for _ in range(50):
        amounts = [rng.randint(1, 12) for _ in range(rng.randint(0, 12))]
        total = sum(amounts)
        expected = total % 2 == 0 and any(sum(combo) == total // 2 for r in range(len(amounts) + 1) for combo in itertools.combinations(amounts, r))
        assert can_split_invoice(amounts) is expected


def test_invoice_split_many_items():
    assert can_split_invoice([1] * 100) is True
