"""通用 UI 组件。"""

from PySide6.QtWidgets import QHBoxLayout, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class CopyableOutput(QWidget):
    """带复制按钮的只读文本输出框。"""

    def __init__(self, placeholder: str = "", parent=None):
        super().__init__(parent)
        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText(placeholder)
        self.copy_button = QPushButton("复制")
        self.copy_button.clicked.connect(self._copy)

        row = QHBoxLayout()
        row.addWidget(self.text_edit)
        side = QVBoxLayout()
        side.addWidget(self.copy_button)
        side.addStretch()
        row.addLayout(side)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(row)

    def set_text(self, text: str) -> None:
        """设置输出文本。"""
        self.text_edit.setPlainText(text)

    def clear(self) -> None:
        """清空输出。"""
        self.text_edit.clear()

    def _copy(self) -> None:
        from PySide6.QtWidgets import QApplication

        clipboard = QApplication.clipboard()
        if clipboard is not None:
            clipboard.setText(self.text_edit.toPlainText())
            self.copy_button.setText("已复制")
            from PySide6.QtCore import QTimer

            QTimer.singleShot(1200, lambda: self.copy_button.setText("复制"))
