import pytest

from solutions.problem_20_currency_converter import CurrencyConverter


@pytest.fixture
def fx():
    c = CurrencyConverter()
    c.add_rate("USD", "EUR", 0.9)
    c.add_rate("EUR", "JPY", 160.0)
    c.add_rate("GBP", "USD", 1.25)
    return c


def test_chained_conversion(fx):
    assert fx.convert(10, "USD", "JPY") == pytest.approx(1440.0)
    assert fx.convert(1, "GBP", "EUR") == pytest.approx(1.125)


def test_reverse_conversion(fx):
    assert fx.convert(1440, "JPY", "USD") == pytest.approx(10.0)
    assert fx.convert(1.125, "EUR", "GBP") == pytest.approx(1.0)


def test_same_currency(fx):
    assert fx.convert(42, "EUR", "EUR") == pytest.approx(42)
    assert fx.convert(42, "XYZ", "XYZ") is None


def test_unknown_or_disconnected(fx):
    assert fx.convert(1, "USD", "INR") is None
    fx.add_rate("INR", "PKR", 3.3)
    assert fx.convert(1, "USD", "INR") is None
    assert fx.convert(1, "INR", "PKR") == pytest.approx(3.3)


def test_joining_two_groups(fx):
    fx.add_rate("INR", "PKR", 3.3)
    fx.add_rate("USD", "INR", 83.0)
    assert fx.convert(1, "GBP", "PKR") == pytest.approx(1.25 * 83.0 * 3.3)
    assert fx.convert(1, "PKR", "JPY") == pytest.approx(0.9 * 160.0 / (83.0 * 3.3))


def test_inconsistent_rate_raises(fx):
    with pytest.raises(ValueError):
        fx.add_rate("GBP", "JPY", 200.0)
    # state unchanged after the rejected update
    assert fx.convert(1, "GBP", "JPY") == pytest.approx(180.0)


def test_consistent_duplicate_rate_is_accepted(fx):
    fx.add_rate("GBP", "JPY", 180.0)
    fx.add_rate("JPY", "USD", 1 / 144.0)
    assert fx.convert(1, "GBP", "JPY") == pytest.approx(180.0)


def test_long_chain():
    c = CurrencyConverter()
    for i in range(5000):
        c.add_rate(f"C{i}", f"C{i + 1}", 1.001)
    assert c.convert(1, "C0", "C5000") == pytest.approx(1.001 ** 5000)
    assert c.convert(1, "C5000", "C0") == pytest.approx(1.001 ** -5000)
