"""01. Autocomplete Engine — see problems/01_autocomplete_engine.md"""

from __future__ import annotations


class AutocompleteSystem:
    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, word: str, freq: int) -> None:
        raise NotImplementedError

    def search(self, prefix: str, k: int) -> list[str]:
        raise NotImplementedError

    def type_char(self, c: str) -> list[str]:
        raise NotImplementedError

    def reset_query(self) -> None:
        raise NotImplementedError
