"""工具基类：所有工具控件继承此类，统一接口。"""

from PySide6.QtWidgets import QVBoxLayout, QWidget


class BaseToolWidget(QWidget):
    """工具控件的抽象基类。

    子类需要在 __init__ 中构建自己的 UI，并设置 windowTitle。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(12, 12, 12, 12)

    @property
    def layout(self):
        """返回主布局，子类可向其添加控件。"""
        return self._layout

    def on_activated(self):
        """工具被切换显示时调用。子类可覆写以聚焦输入框等。"""

    def on_deactivated(self):
        """工具被切走时调用。子类可覆写以清理临时状态。"""
