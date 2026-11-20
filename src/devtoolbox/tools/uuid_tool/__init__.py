"""UUID 生成工具。"""

from devtoolbox.core.registry import ToolSpec
from devtoolbox.tools.uuid_tool.widget import UuidToolWidget

TOOL = ToolSpec(
    key="uuid",
    name="UUID 生成",
    icon="id",
    category="标识",
    factory=UuidToolWidget,
)
