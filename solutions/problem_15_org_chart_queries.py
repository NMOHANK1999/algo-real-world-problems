"""15. Org Chart Queries — see problems/15_org_chart_queries.md"""

from __future__ import annotations


class OrgChart:
    def __init__(self, reports: dict[str, list[str]], ceo: str) -> None:
        raise NotImplementedError

    def closest_common_manager(self, a: str, b: str) -> str:
        raise NotImplementedError

    def chain_of_command(self, employee: str) -> list[str]:
        raise NotImplementedError

    def team_size(self, manager: str) -> int:
        raise NotImplementedError
