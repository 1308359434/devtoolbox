"""明暗主题 QSS 与应用逻辑。"""

from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication

LIGHT_QSS = """
QWidget { background: #f7f8fa; color: #1f2329; }
QListWidget { background: #ffffff; border: 1px solid #e5e6eb; border-radius: 6px; }
QListWidget::item { padding: 8px 10px; border-radius: 4px; }
QListWidget::item:selected { background: #e8f3ff; color: #1d6fe0; }
QLineEdit, QPlainTextEdit, QComboBox { background: #ffffff; color: #1f2329;
    border: 1px solid #dcdfe6; border-radius: 4px; padding: 5px 8px; }
QPushButton { background: #ffffff; color: #1f2329;
    border: 1px solid #dcdfe6; border-radius: 4px; padding: 6px 14px; }
QPushButton:hover { background: #f2f3f5; }
QPushButton:pressed { background: #e5e6eb; }
QPushButton#primary { background: #1d6fe0; color: #ffffff; border: none; }
QPushButton#primary:hover { background: #5b94e6; }
QLabel#hint { color: #86909c; }
QGroupBox { border: 1px solid #e5e6eb; border-radius: 6px; margin-top: 10px; }
QGroupBox::title { subcontrol-origin: margin; padding: 0 4px; }
"""

DARK_QSS = """
QWidget { background: #1e1f22; color: #e5e6eb; }
QListWidget { background: #232529; border: 1px solid #3a3d42; border-radius: 6px; }
QListWidget::item { padding: 8px 10px; border-radius: 4px; }
QListWidget::item:selected { background: #2b4a75; color: #ffffff; }
QLineEdit, QPlainTextEdit, QComboBox { background: #232529; color: #e5e6eb;
    border: 1px solid #3a3d42; border-radius: 4px; padding: 5px 8px; }
QPushButton { background: #2b2d31; color: #e5e6eb;
    border: 1px solid #3a3d42; border-radius: 4px; padding: 6px 14px; }
QPushButton:hover { background: #383b41; }
QPushButton:pressed { background: #454950; }
QPushButton#primary { background: #1d6fe0; color: #ffffff; border: none; }
QPushButton#primary:hover { background: #4a86df; }
QLabel#hint { color: #8f9298; }
QGroupBox { border: 1px solid #3a3d42; border-radius: 6px; margin-top: 10px; }
QGroupBox::title { subcontrol-origin: margin; padding: 0 4px; }
"""


def is_system_dark() -> bool:
    """根据调色板判断系统是否使用深色主题。"""
    app = QApplication.instance()
    if app is None:
        return False
    return app.palette().color(QPalette.Window).lightness() < 128


def apply_theme(mode: str) -> None:
    """应用主题。mode 为 light / dark / system。"""
    app = QApplication.instance()
    if app is None:
        return
    if mode == "system":
        mode = "dark" if is_system_dark() else "light"
    app.setStyleSheet(DARK_QSS if mode == "dark" else LIGHT_QSS)
