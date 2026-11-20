# 第三方组件声明

DevToolBox 自身代码采用 MIT 许可证（见 `LICENSE`）。以下第三方组件按其各自许可证分发。

## PySide6 (Qt for Python)

- 许可证：LGPLv3 或 GPLv3（双许可，任选其一）
- 项目主页：https://qt-project.org/
- 源码获取：https://code.qt.io/cgit/pyside/pyside-setup.git/
- PyPI：https://pypi.org/project/PySide6/

本应用以动态链接方式使用 Qt 库，未修改 Qt 源码。分发包中 Qt 动态链接库保持为独立文件（PyInstaller onedir 模式），未与应用程序代码静态链接。

LGPLv3 许可证全文：https://www.gnu.org/licenses/lgpl-3.0.txt
GPLv3 许可证全文：https://www.gnu.org/licenses/gpl-3.0.txt

使用 LGPL 的权利与义务说明：https://www.qt.io/licensing/open-source-lgpl-obligations

## Python 标准库

应用中 `json`、`re`、`hashlib`、`hmac`、`base64`、`urllib`、`datetime`、`uuid` 等模块来自 CPython 标准库，采用 Python Software Foundation License。

## 其余开发依赖

`pytest`、`ruff`、`pyinstaller` 仅用于开发与构建，不随最终安装包分发。
