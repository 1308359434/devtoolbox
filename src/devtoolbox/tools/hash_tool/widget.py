"""Hash / HMAC 工具 UI。"""

from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
)

from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.tools.hash_tool import logic
from devtoolbox.ui.widgets import CopyableOutput


class HashToolWidget(BaseToolWidget):
    """文本与文件哈希计算。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hash / HMAC")

        algo_row = QHBoxLayout()
        self._algorithm = QComboBox()
        self._algorithm.addItems(logic.ALGORITHMS)
        algo_row.addWidget(QLabel("算法"))
        algo_row.addWidget(self._algorithm)
        algo_row.addStretch()

        self._text = QPlainTextEdit()
        self._text.setPlaceholderText("输入文本")
        self._key = QLineEdit()
        self._key.setPlaceholderText("HMAC 密钥（留空则只算普通哈希）")

        btn_row = QHBoxLayout()
        text_btn = QPushButton("计算文本")
        text_btn.setObjectName("primary")
        text_btn.clicked.connect(self._on_text)
        file_btn = QPushButton("选择文件…")
        file_btn.clicked.connect(self._on_file)
        btn_row.addWidget(text_btn)
        btn_row.addWidget(file_btn)
        btn_row.addStretch()

        self._output = CopyableOutput("哈希结果")

        self.layout.addLayout(algo_row)
        self.layout.addWidget(QLabel("文本"))
        self.layout.addWidget(self._text, stretch=2)
        self.layout.addWidget(QLabel("HMAC 密钥"))
        self.layout.addWidget(self._key)
        self.layout.addLayout(btn_row)
        self.layout.addWidget(self._output, stretch=1)

    def _on_text(self) -> None:
        text = self._text.toPlainText()
        key = self._key.text()
        algo = self._algorithm.currentText()
        result = logic.hmac_text(text, key, algo) if key else logic.hash_text(text, algo)
        self._output.set_text(result)

    def _on_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "选择文件")
        if path:
            self._output.set_text(logic.hash_file(path, self._algorithm.currentText()))

    def on_activated(self) -> None:
        self._text.setFocus()
