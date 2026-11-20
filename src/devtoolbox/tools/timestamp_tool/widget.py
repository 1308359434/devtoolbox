"""时间戳工具 UI。"""

from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox

from devtoolbox.core.base_tool import BaseToolWidget
from devtoolbox.tools.timestamp_tool import logic
from devtoolbox.ui.widgets import CopyableOutput


class TimestampToolWidget(BaseToolWidget):
    """Unix 时间戳与可读时间互转。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("时间戳转换")

        tz_row = QHBoxLayout()
        self._tz = QSpinBox()
        self._tz.setRange(-12, 14)
        self._tz.setValue(8)
        tz_row.addWidget(QLabel("时区偏移 (UTC)"))
        tz_row.addWidget(self._tz)
        tz_row.addStretch()

        self._input = QLineEdit()
        self._input.setPlaceholderText("输入时间戳或时间文本，如 1700000000 或 2024-01-01 12:00:00")
        self._input.returnPressed.connect(self._on_to_datetime)

        btn_row = QHBoxLayout()
        to_dt = QPushButton("时间戳 → 时间")
        to_dt.setObjectName("primary")
        to_dt.clicked.connect(self._on_to_datetime)
        to_ts = QPushButton("时间 → 时间戳")
        to_ts.clicked.connect(self._on_to_timestamp)
        now_btn = QPushButton("当前时间")
        now_btn.clicked.connect(self._on_now)
        for b in (to_dt, to_ts, now_btn):
            btn_row.addWidget(b)
        btn_row.addStretch()

        self._output = CopyableOutput("结果")

        self.layout.addLayout(tz_row)
        self.layout.addWidget(QLabel("输入"))
        self.layout.addWidget(self._input)
        self.layout.addLayout(btn_row)
        self.layout.addWidget(self._output, stretch=1)

    def _on_to_datetime(self) -> None:
        self._output.set_text(logic.to_datetime(self._input.text(), self._tz.value()))

    def _on_to_timestamp(self) -> None:
        self._output.set_text(logic.to_timestamp(self._input.text()))

    def _on_now(self) -> None:
        self._output.set_text(logic.now(self._tz.value()))

    def on_activated(self) -> None:
        self._input.setFocus()
