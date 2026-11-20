"""编解码工具逻辑测试。"""

from devtoolbox.tools.encoding_tool import logic


def test_base64_roundtrip():
    assert logic.b64_decode(logic.b64_encode("hello 世界")) == "hello 世界"


def test_base64_known_value():
    assert logic.b64_encode("hello") == "aGVsbG8="


def test_base64_invalid():
    assert "解码失败" in logic.b64_decode("!!!not-base64!!!")


def test_url_roundtrip():
    text = "你好 world&key=值"
    assert logic.url_decode(logic.url_encode(text)) == text


def test_url_encode_known_value():
    assert logic.url_encode("a b") == "a%20b"


def test_operations_registry():
    assert set(logic.OPERATIONS) == {"Base64 编码", "Base64 解码", "URL 编码", "URL 解码"}
