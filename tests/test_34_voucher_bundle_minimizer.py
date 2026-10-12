import itertools
import random

from solutions.problem_34_voucher_bundle_minimizer import minimum_vouchers_for_total


def test_minimum_vouchers_examples():
    assert minimum_vouchers_for_total([1, 3, 4, 8], 11) == 2
    assert minimum_vouchers_for_total([2, 4, 6], 5) == -1


def test_minimum_vouchers_zero_and_duplicate_values():
    assert minimum_vouchers_for_total([2, 3], 0) == 0
    assert minimum_vouchers_for_total([5, 5, 9], 10) == 2
    assert minimum_vouchers_for_total([], 3) == -1


def test_minimum_vouchers_matches_brute_force():
    rng = random.Random(34)
    for _ in range(50):
        vouchers = [rng.randint(1, 10) for _ in range(rng.randint(0, 10))]
        total = rng.randint(0, 25)
        lengths = [len(combo) for r in range(len(vouchers) + 1) for combo in itertools.combinations(vouchers, r) if sum(combo) == total]
        expected = min(lengths, default=-1)
        assert minimum_vouchers_for_total(vouchers, total) == expected


def test_minimum_vouchers_does_not_reuse_one_voucher():
    assert minimum_vouchers_for_total([3, 7], 6) == -1
