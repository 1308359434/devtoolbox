# DevToolBox

**离线优先、零遥测、跨平台的开发者工具箱。**

常用文本、编码、哈希与调试小工具，全部本地运行——不联网、不登录、不上传。

> 本项目为开发中的开源作品，当前处于 MVP 阶段（v0.1.0）。

## 功能

- **JSON 格式化 / 压缩 / 校验** —— 显示错误行列位置，保留中文
- **正则测试器** —— 实时匹配、捕获组、支持 i/m/s/x 标志
- **Base64 / URL 编解码** —— 文本互转，支持一键交换
- **Hash / HMAC** —— MD5、SHA-1/256/512，支持文本文件与 HMAC 密钥
- **时间戳转换** —— Unix 时间戳 ↔ 可读时间，自定义时区，毫秒级当前时间
- **UUID 生成** —— v1 / v4，批量生成，大小写可选
- 全局工具搜索（`Ctrl+K`）、明暗主题、窗口状态记忆

## 下载与运行

从 [Releases](https://github.com/1308359434/devtoolbox/releases) 下载 Windows 版，zip 解压后双击 `DevToolBox.exe` 即可运行——单文件，无需安装依赖。

`DevToolBox.exe` 为 PyInstaller onefile 产物：首次启动会解压到临时目录，约需数秒；运行时不联网、不写注册表。许可与第三方声明随 zip 附带。

源码运行：

```bash
python -m venv .venv
source .venv/Scripts/activate       # Windows Git Bash
pip install -e ".[dev]"
python -m devtoolbox
```

## 快捷键

| 快捷键 | 功能 |
| --- | --- |
| `Ctrl+K` | 聚焦工具搜索框 |

## 开发

```bash
pytest                 # 单元测试
ruff check src tests   # 代码检查
powershell -ExecutionPolicy Bypass -File scripts/build_win.ps1   # Windows 打包
```

欢迎贡献，见 [CONTRIBUTING.md](CONTRIBUTING.md)。每个工具的逻辑层（`logic.py`）不依赖 Qt，可独立测试。

## 许可

应用代码：[MIT](LICENSE) · 依赖组件：[第三方声明](THIRD_PARTY_NOTICES.md)

PySide6/Qt 采用 LGPLv3/GPLv3 双许可；本应用以动态链接方式使用 Qt，未静态链接。
