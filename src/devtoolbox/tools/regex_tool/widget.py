"""正则测试器 UI。"""

from PySide6.QtWidgets import QHBoxLayout, QLabel, QPlainTextEdit

from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.tools.regex_tool import logic
from devtoolbox.ui.widgets import CopyableOutput


class RegexToolWidget(BaseToolWidget):
    """实时正则匹配与高亮。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("正则测试器")

        pattern_row = QHBoxLayout()
        self._pattern = QPlainTextEdit()
        self._pattern.setPlaceholderText("正则表达式，例如：\\d{4}-\\d{2}-\\d{2}")
        self._pattern.setFixedHeight(60)
        self._flags = QPlainTextEdit()
        self._flags.setPlaceholderText("标志")
        self._flags.setFixedHeight(60)
        self._flags.setFixedWidth(80)
        pattern_row.addWidget(self._pattern, stretch=4)
        pattern_row.addWidget(self._flags)

        self._text = QPlainTextEdit()
        self._text.setPlaceholderText("在此输入待匹配文本")
        self._status = QLabel("")
        self._status.setObjectName("hint")
        self._output = CopyableOutput("匹配结果")

        self._pattern.textChanged.connect(self._on_run)
        self._flags.textChanged.connect(self._on_run)
        self._text.textChanged.connect(self._on_run)

        self.layout.addWidget(QLabel("正则表达式"))
        self.layout.addLayout(pattern_row)
        self.layout.addWidget(QLabel("测试文本"))
        self.layout.addWidget(self._text, stretch=3)
        self.layout.addWidget(QLabel("匹配结果"))
        self.layout.addWidget(self._status)
        self.layout.addWidget(self._output, stretch=2)

    def _on_run(self) -> None:
        result = logic.test_regex(
            self._pattern.toPlainText().strip(),
            self._text.toPlainText(),
            self._flags.toPlainText().strip(),
        )
        if result.ok:
            self._status.setText(f"✓ {len(result.matches)} 处匹配")
        else:
            self._status.setText("✗ " + result.error)
        self._output.set_text(logic.format_matches(result))

    def on_activated(self) -> None:
        self._pattern.setFocus()
