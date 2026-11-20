"""UUID 工具逻辑测试。"""

import re

from devtoolbox.tools.uuid_tool import logic

UUID_V4 = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")


def test_generate_v4():
    lines = logic.generate(4, 5).splitlines()
    assert len(lines) == 5
    assert all(UUID_V4.match(line) for line in lines)


def test_generate_count():
    assert len(logic.generate(4, 3).splitlines()) == 3


def test_generate_uppercase():
    assert logic.generate(4, 1, uppercase=True).isupper()


def test_generate_v1():
    assert len(logic.generate(1, 2).splitlines()) == 2


def test_generate_bad_version():
    assert "错误" in logic.generate(3)


def test_generate_bad_count():
    assert "错误" in logic.generate(4, 0)
