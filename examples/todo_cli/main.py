#!/usr/bin/env python3
"""归档：最初的零依赖命令行待办清单（项目起源，不再维护）。"""

import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__.strip())
        return
    command, *rest = args
    todos = load_todos()
    if command == "add" and rest:
        todos.append({"text": " ".join(rest), "done": False})
        save_todos(todos)
        print("已添加")
    elif command == "list":
        for i, item in enumerate(todos, 1):
            mark = "x" if item["done"] else " "
            print(f"[{mark}] {i}. {item['text']}")
    elif command == "done" and rest and rest[0].isdigit():
        idx = int(rest[0])
        if 1 <= idx <= len(todos):
            todos[idx - 1]["done"] = True
            save_todos(todos)
    elif command == "clear":
        save_todos([])
    else:
        print("未知命令")


if __name__ == "__main__":
    main()
