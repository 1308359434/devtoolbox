# workbuddy-github-demo

一个由 WorkBuddy 创建的示例项目，用于演示本地工作区与 GitHub 仓库的绑定与推送。

## 功能

一个零依赖的命令行待办清单（Todo CLI），仅使用 Python 标准库。

## 使用

```bash
python main.py add "写下第一行代码"
python main.py list
python main.py done 1
python main.py clear
```

待办数据保存在当前目录的 `todos.json` 中。

## 项目结构

- `main.py` — CLI 入口与命令实现
- `.gitignore` — 忽略运行时生成的数据与缓存
