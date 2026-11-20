"""Base64 与 URL 编解码逻辑。"""

import base64
import urllib.parse


def b64_encode(text: str) -> str:
    """Base64 编码（UTF-8）。"""
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def b64_decode(text: str) -> str:
    """Base64 解码。失败时返回错误说明。"""
    try:
        return base64.b64decode(text, validate=True).decode("utf-8")
    except Exception as exc:
        return f"[解码失败] {exc}"


def url_encode(text: str) -> str:
    """URL 编码。"""
    return urllib.parse.quote(text, safe="")


def url_decode(text: str) -> str:
    """URL 解码。"""
    return urllib.parse.unquote(text)


OPERATIONS = {
    "Base64 编码": b64_encode,
    "Base64 解码": b64_decode,
    "URL 编码": url_encode,
    "URL 解码": url_decode,
}
