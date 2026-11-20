"""工具注册表：集中登记所有工具及其工厂函数。"""

from dataclasses import dataclass
from typing import Callable

from devtoolbox.core.base_tool import BaseToolWidget


@dataclass(frozen=True)
class ToolSpec:
    """工具元数据。"""

    key: str
    name: str
    icon: str
    category: str
    factory: Callable[[], BaseToolWidget]


_REGISTRY: list[ToolSpec] = []


def register(spec: ToolSpec) -> None:
    """注册一个工具。重复 key 会被拒绝。"""
    if any(item.key == spec.key for item in _REGISTRY):
        raise ValueError(f"工具 key 重复: {spec.key}")
    _REGISTRY.append(spec)


def all_tools() -> list[ToolSpec]:
    """返回全部已注册工具（按注册顺序）。"""
    return list(_REGISTRY)


def load_builtin_tools() -> None:
    """注册所有内置工具。此函数只调用一次。"""
    if _REGISTRY:
        return

    from devtoolbox.tools.encoding_tool import TOOL as ENCODING
    from devtoolbox.tools.hash_tool import TOOL as HASH
    from devtoolbox.tools.json_tool import TOOL as JSON
    from devtoolbox.tools.regex_tool import TOOL as REGEX
    from devtoolbox.tools.timestamp_tool import TOOL as TIMESTAMP
    from devtoolbox.tools.uuid_tool import TOOL as UUID

    for spec in (JSON, REGEX, ENCODING, HASH, TIMESTAMP, UUID):
        register(spec)
