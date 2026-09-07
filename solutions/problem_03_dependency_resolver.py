"""03. Dependency Resolver — see problems/03_dependency_resolver.md"""

from __future__ import annotations


class CycleError(Exception):
    """Raised when the dependency graph contains a cycle."""


def resolve_order(packages: list[str], deps: list[tuple[str, str]]) -> list[str]:
    raise NotImplementedError
