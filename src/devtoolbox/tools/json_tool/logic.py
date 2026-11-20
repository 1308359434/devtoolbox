"""JSON 格式化、压缩与校验（纯逻辑，无 Qt 依赖）。"""

import json
from dataclasses import dataclass


@dataclass
class JsonResult:
    """处理结果。"""

    ok: bool
    text: str
    error: str = ""


def format_json(source: str, indent: int = 2) -> JsonResult:
    """格式化 JSON，失败时返回带有行列信息的错误。"""
    if not source.strip():
        return JsonResult(ok=False, text="", error="输入为空")
    try:
        data = json.loads(source)
    except json.JSONDecodeError as exc:
        return JsonResult(
            ok=False,
            text="",
            error=f"第 {exc.lineno} 行第 {exc.colno} 列：{exc.msg}",
        )
    text = json.dumps(data, ensure_ascii=False, indent=indent)
    return JsonResult(ok=True, text=text)


def minify_json(source: str) -> JsonResult:
    """压缩 JSON 为单行。"""
    result = format_json(source)
    if not result.ok:
        return result
    data = json.loads(source)
    return JsonResult(ok=True, text=json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def validate_json(source: str) -> JsonResult:
    """仅校验 JSON 是否合法。"""
    result = format_json(source)
    if result.ok:
        return JsonResult(ok=True, text="✓ 合法 JSON")
    return result
