"""UUID 生成工具 UI。"""

from PySide6.QtWidgets import QCheckBox, QComboBox, QHBoxLayout, QLabel, QPushButton, QSpinBox

from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.tools.uuid_tool import logic
from devtoolbox.ui.widgets import CopyableOutput


class UuidToolWidget(BaseToolWidget):
    """批量生成 UUID。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("UUID 生成")

        row = QHBoxLayout()
        self._version = QComboBox()
        self._version.addItems(["v4 (随机)", "v1 (基于时间)"])
        self._count = QSpinBox()
        self._count.setRange(1, 1000)
        self._count.setValue(10)
        self._upper = QCheckBox("大写")
        generate = QPushButton("生成")
        generate.setObjectName("primary")
        generate.clicked.connect(self._on_generate)
        row.addWidget(QLabel("版本"))
        row.addWidget(self._version)
        row.addWidget(QLabel("数量"))
        row.addWidget(self._count)
        row.addWidget(self._upper)
        row.addWidget(generate)
        row.addStretch()

        self._output = CopyableOutput("生成的 UUID")
        self.layout.addLayout(row)
        self.layout.addWidget(self._output, stretch=1)

    def _on_generate(self) -> None:
        version = 4 if self._version.currentIndex() == 0 else 1
        self._output.set_text(logic.generate(version, self._count.value(), self._upper.isChecked()))
