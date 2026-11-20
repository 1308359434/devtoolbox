"""正则测试器。"""

from devtoolbox.core.registry import ToolSpec
from devtoolbox.tools.regex_tool.widget import RegexToolWidget

TOOL = ToolSpec(
    key="regex",
    name="正则测试器",
    icon=".*",
    category="文本",
    factory=RegexToolWidget,
)
