"""时间戳工具逻辑测试。"""

from devtoolbox.tools.timestamp_tool import logic


def test_to_datetime_utc():
    result = logic.to_datetime(0, 0)
    assert "1970-01-01" in result and "UTC" in result


def test_to_datetime_timezone():
    result = logic.to_datetime(0, 8)
    assert "1970-01-01 08:00:00" in result


def test_to_datetime_invalid():
    assert "错误" in logic.to_datetime("abc")


def test_to_timestamp_roundtrip():
    assert logic.to_timestamp("1970-01-01 00:00:00") == "0"


def test_to_timestamp_digits_passthrough():
    assert logic.to_timestamp("1700000000") == "1700000000"


def test_to_timestamp_bad_format():
    assert "错误" in logic.to_timestamp("not a date")


def test_now_format():
    result = logic.now(8)
    assert "秒级:" in result and "毫秒:" in result
