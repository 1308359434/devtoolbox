"""正则测试器逻辑测试。"""

from devtoolbox.tools.regex_tool import logic


def test_find_all_matches():
    result = logic.test_regex(r"\d+", "a1b22c333")
    assert result.ok
    assert [m.text for m in result.matches] == ["1", "22", "333"]
    assert result.matches[1].start == 3


def test_capture_groups():
    result = logic.test_regex(r"(\w+)@(\w+)", "a@b.com")
    assert result.ok
    assert result.matches[0].groups == ("a", "b")


def test_ignore_case_flag():
    result = logic.test_regex("hello", "HELLO", "i")
    assert result.ok and len(result.matches) == 1


def test_invalid_pattern():
    result = logic.test_regex("[", "text")
    assert not result.ok
    assert "错误" in result.error


def test_empty_pattern():
    assert not logic.test_regex("", "text").ok


def test_no_matches():
    result = logic.test_regex(r"\d+", "abc")
    assert result.ok and result.matches == []
    assert logic.format_matches(result) == "没有匹配"
