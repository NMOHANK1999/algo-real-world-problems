"""03. Dependency Resolver — see problems/03_dependency_resolver.md"""

from __future__ import annotations
from collections import defaultdict


class CycleError(Exception):
    """Raised when the dependency graph contains a cycle."""


def resolve_order(packages: list[str], deps: list[tuple[str, str]]) -> list[str]:
    prereqs = defaultdict(list)
    postreqs = defaultdict(list)
    ans = []
    bfs = []

    for pack, deps in deps:
        prereqs[pack].append(deps)
        postreqs[deps].append(pack)

    for pack in packages:
        if len(prereqs[pack]) == 0:
            bfs.append(pack)

    while bfs:
        course = bfs.pop()
        ans.append(course)
        for pack in postreqs[course]:
            prereqs[pack].remove(course)
            if len(prereqs[pack]) == 0:
                del prereqs[pack]
                bfs.append(pack)

    if len(packages) != len(ans):
        return CycleError # or you can do CycleError()
    else:
        return ans

        
packages = ["A", "B", "C", "D"]
deps = [("B", "A"), ("C", "A"), ("D", "B"), ("D", "C")]

test1 = resolve_order(packages, deps)
assert ( test1 == ["A", "B", "C", "D"] or test1 == ["A", "C", "B", "D"]) 
# valid outputs: ["A", "B", "C", "D"] or ["A", "C", "B", "D"]
# (A must come first, D must come last, B/C order between them is free)

try:
    resolve_order(["A", "B", "C"], [("A", "B"), ("B", "C"), ("C", "A")])
except CycleError:
    pass