"""应用启动入口。"""

import os
import sys
import traceback

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMessageBox

from devtoolbox.main_window import MainWindow


def main() -> int:
    """启动应用，返回退出码。"""
    os.environ.setdefault("QT_ENABLE_HIGHDPI_SCALING", "1")
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setApplicationName("DevToolBox")
    app.setOrganizationName("DevToolBox")

    def excepthook(exc_type, exc_value, exc_tb):
        detail = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        QMessageBox.critical(None, "DevToolBox 错误", f"发生未处理的错误：\n\n{detail[:2000]}")

    sys.excepthook = excepthook

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
