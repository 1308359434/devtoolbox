"""JSON 工具。"""

from devtoolbox.core.registry import ToolSpec
from devtoolbox.tools.json_tool.widget import JsonToolWidget

TOOL = ToolSpec(
    key="json",
    name="JSON 格式化",
    icon="{ }",
    category="文本",
    factory=JsonToolWidget,
)
