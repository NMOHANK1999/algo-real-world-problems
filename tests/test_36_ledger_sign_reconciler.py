import itertools
import random

from solutions.problem_36_ledger_sign_reconciler import count_ledger_reconciliations


def test_ledger_reconciliations_examples():
    assert count_ledger_reconciliations([1, 1, 1, 1, 1], 3) == 5
    assert count_ledger_reconciliations([1, 2, 3], 10) == 0


def test_ledger_reconciliations_zeroes_and_empty_input():
    assert count_ledger_reconciliations([0, 0, 1], 1) == 4
    assert count_ledger_reconciliations([], 0) == 1
    assert count_ledger_reconciliations([], 1) == 0


def test_ledger_reconciliations_matches_brute_force():
    rng = random.Random(36)
    for _ in range(50):
        amounts = [rng.randint(0, 5) for _ in range(rng.randint(0, 10))]
        target = rng.randint(-12, 12)
        expected = sum(1 for signs in itertools.product((-1, 1), repeat=len(amounts)) if sum(sign * amount for sign, amount in zip(signs, amounts)) == target)
        assert count_ledger_reconciliations(amounts, target) == expected


def test_ledger_reconciliations_many_repeated_amounts():
    assert count_ledger_reconciliations([1] * 30, 0) == 155117520
