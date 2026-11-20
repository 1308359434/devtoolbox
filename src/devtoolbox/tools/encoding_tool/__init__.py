"""编解码工具。"""

from devtoolbox.core.registry import ToolSpec
from devtoolbox.tools.encoding_tool.widget import EncodingToolWidget

TOOL = ToolSpec(
    key="encoding",
    name="Base64 / URL 编解码",
    icon="⇄",
    category="编码",
    factory=EncodingToolWidget,
)
