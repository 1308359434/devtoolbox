#!/usr/bin/env python3
"""一个零依赖的命令行待办清单。"""

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


def add(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"已添加: {text}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("暂无待办事项。")
        return
    for i, item in enumerate(todos, 1):
        mark = "x" if item["done"] else " "
        print(f"[{mark}] {i}. {item['text']}")


def done(index):
    todos = load_todos()
    if not 1 <= index <= len(todos):
        print("无效的序号。")
        return
    todos[index - 1]["done"] = True
    save_todos(todos)
    print(f"已完成: {todos[index - 1]['text']}")


def clear():
    save_todos([])
    print("已清空全部待办。")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__.strip())
        print("\n可用命令: add <内容> | list | done <序号> | clear")
        return
    command, *rest = args
    if command == "add" and rest:
        add(" ".join(rest))
    elif command == "list":
        list_todos()
    elif command == "done" and rest and rest[0].isdigit():
        done(int(rest[0]))
    elif command == "clear":
        clear()
    else:
        print("未知命令或参数不足。")


if __name__ == "__main__":
    main()
