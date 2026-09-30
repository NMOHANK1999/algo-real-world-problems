"""17. Config Tree Snapshotter — see problems/17_config_snapshot.md"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ConfigNode:
    key: str
    children: list[ConfigNode] = field(default_factory=list)


def serialize(root: ConfigNode | None) -> str:
    raise NotImplementedError


def deserialize(data: str) -> ConfigNode | None:
    raise NotImplementedError
