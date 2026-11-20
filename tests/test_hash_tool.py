"""Hash / HMAC 工具逻辑测试。"""

from devtoolbox.tools.hash_tool import logic


def test_md5_known_value():
    assert logic.hash_text("abc", "MD5") == "900150983cd24fb0d6963f7d28e17f72"


def test_sha256_known_value():
    assert logic.hash_text("abc", "SHA-256") == (
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )


def test_hmac_known_value():
    result = logic.hmac_text("hello", "key", "SHA-256")
    assert len(result) == 64 and all(c in "0123456789abcdef" for c in result)


def test_unsupported_algorithm():
    assert "不支持" in logic.hash_text("abc", "INVALID")


def test_hash_file(tmp_path):
    f = tmp_path / "data.txt"
    f.write_text("abc", encoding="utf-8")
    assert logic.hash_file(str(f), "MD5") == "900150983cd24fb0d6963f7d28e17f72"


def test_hash_file_missing(tmp_path):
    assert "读取失败" in logic.hash_file(str(tmp_path / "none"), "MD5")
