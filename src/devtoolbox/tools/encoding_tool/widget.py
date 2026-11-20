"""编解码工具 UI。"""

from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QPlainTextEdit, QPushButton

from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.tools.encoding_tool import logic
from devtoolbox.ui.widgets import CopyableOutput


class EncodingToolWidget(BaseToolWidget):
    """Base64 / URL 编解码。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("编解码工具")

        row = QHBoxLayout()
        self._op = QComboBox()
        self._op.addItems(list(logic.OPERATIONS))
        convert = QPushButton("转换")
        convert.setObjectName("primary")
        convert.clicked.connect(self._on_run)
        swap = QPushButton("⇅ 交换")
        swap.clicked.connect(self._on_swap)
        row.addWidget(QLabel("操作"))
        row.addWidget(self._op)
        row.addWidget(convert)
        row.addWidget(swap)
        row.addStretch()

        self._input = QPlainTextEdit()
        self._input.setPlaceholderText("输入文本")
        self._output = CopyableOutput("转换结果")

        self.layout.addLayout(row)
        self.layout.addWidget(QLabel("输入"))
        self.layout.addWidget(self._input, stretch=3)
        self.layout.addWidget(QLabel("输出"))
        self.layout.addWidget(self._output, stretch=2)

    def _on_run(self) -> None:
        func = logic.OPERATIONS[self._op.currentText()]
        self._output.set_text(func(self._input.toPlainText()))

    def _on_swap(self) -> None:
        self._input.setPlainText(self._output.text_edit.toPlainText())

    def on_activated(self) -> None:
        self._input.setFocus()
