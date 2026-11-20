"""时间戳工具。"""

from devtoolbox.core.registry import ToolSpec
from devtoolbox.tools.timestamp_tool.widget import TimestampToolWidget

TOOL = ToolSpec(
    key="timestamp",
    name="时间戳转换",
    icon="⏱",
    category="时间",
    factory=TimestampToolWidget,
)
