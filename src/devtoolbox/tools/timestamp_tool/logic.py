"""时间戳转换逻辑（纯 Python，无第三方依赖）。"""

from datetime import datetime, timedelta, timezone


def to_datetime(timestamp: float | str, tz_offset: int = 0) -> str:
    """Unix 时间戳转本地可读时间。tz_offset 为小时偏移，如 8 表示 UTC+8。"""
    try:
        value = float(timestamp)
    except (ValueError, TypeError):
        return "[错误] 时间戳必须是数字"
    tz = timezone(timedelta(hours=tz_offset))
    try:
        dt = datetime.fromtimestamp(value, tz=tz)
    except (ValueError, OSError, OverflowError) as exc:
        return f"[错误] {exc}"
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z")


def to_timestamp(text: str) -> str:
    """可读时间转 Unix 时间戳。支持 YYYY-MM-DD HH:MM:SS 等格式。"""
    text = text.strip()
    if not text:
        return "[错误] 输入为空"
    if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
        return text
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y/%m/%d %H:%M:%S"):
        try:
            dt = datetime.strptime(text, fmt)
            return str(int(dt.replace(tzinfo=timezone.utc).timestamp()))
        except ValueError:
            continue
    return "[错误] 无法识别的时间格式"


def now(tz_offset: int = 0) -> str:
    """返回当前时间的秒级与毫秒级时间戳。"""
    tz = timezone(timedelta(hours=tz_offset))
    current = datetime.now(tz)
    return f"秒级: {int(current.timestamp())}\n毫秒: {int(current.timestamp() * 1000)}"
