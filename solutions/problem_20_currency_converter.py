"""20. Currency Converter — see problems/20_currency_converter.md"""

from __future__ import annotations


class CurrencyConverter:
    def __init__(self) -> None:
        raise NotImplementedError

    def add_rate(self, src: str, dst: str, rate: float) -> None:
        raise NotImplementedError

    def convert(self, amount: float, src: str, dst: str) -> float | None:
        raise NotImplementedError
