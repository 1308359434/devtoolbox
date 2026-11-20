"""正则测试器逻辑（纯 Python）。"""

import re
from dataclasses import dataclass, field


@dataclass
class MatchResult:
    """单个匹配结果。"""

    start: int
    end: int
    text: str
    groups: tuple[str, ...] = field(default_factory=tuple)


@dataclass
class RegexResult:
    """测试整体结果。"""

    ok: bool
    matches: list[MatchResult] = field(default_factory=list)
    error: str = ""


_FLAG_MAP = {
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE,
}


def test_regex(pattern: str, text: str, flags: str = "") -> RegexResult:
    """在 text 中查找 pattern 的全部匹配。flags 支持 i/m/s/x。"""
    if not pattern:
        return RegexResult(ok=False, error="正则表达式为空")
    compiled_flags = 0
    for ch in flags.lower():
        compiled_flags |= _FLAG_MAP.get(ch, 0)
    try:
        regex = re.compile(pattern, compiled_flags)
    except re.error as exc:
        return RegexResult(ok=False, error=f"表达式错误：{exc}")
    matches = []
    for match in regex.finditer(text):
        groups = tuple(g if g is not None else "" for g in match.groups())
        matches.append(MatchResult(match.start(), match.end(), match.group(0), groups))
    return RegexResult(ok=True, matches=matches)


def format_matches(result: RegexResult) -> str:
    """把匹配结果格式化为可读文本。"""
    if not result.ok:
        return result.error
    if not result.matches:
        return "没有匹配"
    lines = []
    for i, m in enumerate(result.matches, 1):
        lines.append(f"#{i}  位置 {m.start}-{m.end}  「{m.text}」")
        for j, group in enumerate(m.groups, 1):
            lines.append(f"     组{j}: {group}")
    return "\n".join(lines)
