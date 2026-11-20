# 参与贡献

感谢你考虑为 DevToolBox 做贡献。

## 开发环境

```bash
python -m venv .venv
source .venv/Scripts/activate      # Windows Git Bash
python -m pip install -e ".[dev]"
pytest
ruff check src tests
python -m devtoolbox
```

## 添加新工具

每个工具是一个独立包，放在 `src/devtoolbox/tools/<name>/`，包含：

- `logic.py`：纯 Python 逻辑，**禁止 import PySide6 或任何 UI 代码**，便于单元测试。
- `widget.py`：UI 层，继承 `BaseToolWidget`，调用 `logic.py` 暴露的函数。
- `__init__.py`：导出 `TOOL` 元数据与 `create_widget` 工厂函数。
- `tests/test_<name>.py`：为 `logic.py` 的每个公开函数编写测试。

在 `src/devtoolbox/core/registry.py` 中注册新工具。

## 提交规范

提交信息使用 Conventional Commits：`feat:` 新功能、`fix:` 修复、`docs:` 文档、`refactor:` 重构、`chore:` 杂项。

## 行为准则

友善沟通，尊重不同观点。报告问题请附复现步骤、系统与 Python 版本。
