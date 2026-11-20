"""主窗口：侧栏工具列表、搜索框、工具容器。"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from devtoolbox.core import settings
from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.core.registry import ToolSpec, all_tools, load_builtin_tools
from devtoolbox.ui import theme


class MainWindow(QMainWindow):
    """应用主窗口。"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DevToolBox - 离线开发者工具箱")
        self.resize(1080, 720)
        self._widgets: dict[str, BaseToolWidget] = {}
        self._specs: list[ToolSpec] = []

        load_builtin_tools()
        self._build_ui()
        self._build_menu()
        self._populate_tools("")
        self._restore_geometry()

        mode = settings.get_theme()
        theme.apply_theme(mode)
        theme_labels = {"light": "浅色", "dark": "深色", "system": "跟随系统"}
        self._theme_combo.setCurrentText(theme_labels[mode])

        if self._tool_list.count() > 0:
            self._tool_list.setCurrentRow(0)

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)

        # 左侧栏
        sidebar = QVBoxLayout()
        self._search = QLineEdit()
        self._search.setPlaceholderText("搜索工具 (Ctrl+K)")
        self._search.textChanged.connect(self._populate_tools)
        self._tool_list = QListWidget()
        self._tool_list.currentItemChanged.connect(self._on_tool_changed)

        self._theme_combo = QComboBox()
        self._theme_combo.addItems(["跟随系统", "浅色", "深色"])
        self._theme_combo.currentTextChanged.connect(self._on_theme_changed)
        theme_row = QHBoxLayout()
        theme_row.addWidget(QLabel("主题"))
        theme_row.addWidget(self._theme_combo)

        sidebar.addWidget(self._search)
        sidebar.addWidget(self._tool_list, stretch=1)
        sidebar.addLayout(theme_row)

        # 右侧工具区
        self._stack = QStackedWidget()
        root.addLayout(sidebar, stretch=1)
        root.addWidget(self._stack, stretch=4)

    def _build_menu(self) -> None:
        menubar = self.menuBar()
        file_menu = menubar.addMenu("文件")
        quit_action = QAction("退出", self)
        quit_action.setShortcut(QKeySequence.Quit)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        view_menu = menubar.addMenu("视图")
        focus_search = QAction("搜索工具", self)
        focus_search.setShortcut(QKeySequence("Ctrl+K"))
        focus_search.triggered.connect(lambda: self._search.setFocus())
        view_menu.addAction(focus_search)

    def _populate_tools(self, keyword: str) -> None:
        keyword = keyword.strip().lower()
        previous = self._tool_list.currentItem()
        previous_key = previous.data(Qt.UserRole) if previous else None

        self._tool_list.clear()
        self._specs = [
            s for s in all_tools()
            if keyword in s.name.lower() or keyword in s.key.lower()
        ]
        for spec in self._specs:
            from PySide6.QtWidgets import QListWidgetItem

            item = QListWidgetItem(f"{spec.icon}  {spec.name}")
            item.setData(Qt.UserRole, spec.key)
            self._tool_list.addItem(item)

        if previous_key:
            for i in range(self._tool_list.count()):
                if self._tool_list.item(i).data(Qt.UserRole) == previous_key:
                    self._tool_list.setCurrentRow(i)
                    return

    def _on_tool_changed(self, current, previous) -> None:
        if current is None:
            return
        key = current.data(Qt.UserRole)
        if key not in self._widgets:
            spec = next(s for s in self._specs if s.key == key)
            widget = spec.factory()
            self._widgets[key] = widget
            self._stack.addWidget(widget)
        else:
            widget = self._widgets[key]
        old_key = previous.data(Qt.UserRole) if previous else None
        if old_key and old_key in self._widgets:
            self._widgets[old_key].on_deactivated()
        self._stack.setCurrentWidget(widget)
        widget.on_activated()

    def _on_theme_changed(self, text: str) -> None:
        mapping = {"浅色": "light", "深色": "dark", "跟随系统": "system"}
        mode = mapping.get(text, "system")
        settings.set_theme(mode)
        theme.apply_theme(mode)

    def _restore_geometry(self) -> None:
        data = settings.load_geometry()
        if data:
            self.restoreGeometry(data)

    def closeEvent(self, event) -> None:
        settings.save_geometry(bytes(self.saveGeometry()))
        super().closeEvent(event)
