"""Hash / HMAC 工具。"""

from devtoolbox.core.registry import ToolSpec
from devtoolbox.tools.hash_tool.widget import HashToolWidget

TOOL = ToolSpec(
    key="hash",
    name="Hash / HMAC",
    icon="#",
    category="安全",
    factory=HashToolWidget,
)
