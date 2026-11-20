"""JSON 工具 UI。"""

from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QPushButton

from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.tools.json_tool import logic
from devtoolbox.ui.widgets import CopyableOutput


class JsonToolWidget(BaseToolWidget):
    """JSON 格式化 / 压缩 / 校验。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        from PySide6.QtWidgets import QPlainTextEdit

        self.setWindowTitle("JSON 工具")

        actions = QHBoxLayout()
        self._action_combo = QComboBox()
        self._action_combo.addItems(["格式化", "压缩", "校验"])
        run = QPushButton("处理")
        run.setObjectName("primary")
        run.clicked.connect(self._on_run)
        actions.addWidget(QLabel("操作"))
        actions.addWidget(self._action_combo)
        actions.addWidget(run)
        actions.addStretch()

        self._input = QPlainTextEdit()
        self._input.setPlaceholderText('在此粘贴 JSON，例如：{"name": "DevToolBox"}')
        self._status = QLabel("")
        self._status.setObjectName("hint")
        self._output = CopyableOutput("处理结果")

        self.layout.addLayout(actions)
        self.layout.addWidget(QLabel("输入"))
        self.layout.addWidget(self._input, stretch=3)
        self.layout.addWidget(QLabel("输出"))
        self.layout.addWidget(self._status)
        self.layout.addWidget(self._output, stretch=2)

    def _on_run(self) -> None:
        source = self._input.toPlainText()
        action = self._action_combo.currentText()
        if action == "格式化":
            result = logic.format_json(source)
        elif action == "压缩":
            result = logic.minify_json(source)
        else:
            result = logic.validate_json(source)
        self._status.setText("✓ 成功" if result.ok else "✗ " + result.error)
        self._output.set_text(result.text if result.ok else "")

    def on_activated(self) -> None:
        self._input.setFocus()
