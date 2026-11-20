"""JSON 工具逻辑测试。"""

from devtoolbox.tools.json_tool import logic


def test_format_valid_json():
    result = logic.format_json('{"name":"Tom","age":20}')
    assert result.ok
    assert '"name": "Tom"' in result.text


def test_format_invalid_json_reports_position():
    result = logic.format_json('{"a": 1,}')
    assert not result.ok
    assert "行" in result.error and "列" in result.error


def test_format_empty_input():
    assert not logic.format_json("   ").ok


def test_minify_json():
    result = logic.minify_json('{"a": 1, "b": [2, 3]}')
    assert result.ok
    assert result.text == '{"a":1,"b":[2,3]}'


def test_validate_json():
    assert logic.validate_json("[1,2,3]").ok
    assert not logic.validate_json("not json").ok


def test_unicode_preserved():
    result = logic.format_json('{"name":"中文"}')
    assert "中文" in result.text
