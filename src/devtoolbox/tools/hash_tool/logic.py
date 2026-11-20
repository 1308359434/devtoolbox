"""Hash / HMAC 计算逻辑。"""

import hashlib
import hmac

ALGORITHMS = ["MD5", "SHA-1", "SHA-256", "SHA-512"]


def hash_text(text: str, algorithm: str) -> str:
    """计算文本哈希。"""
    name = algorithm.lower().replace("-", "")
    data = text.encode("utf-8")
    try:
        return hashlib.new(name, data).hexdigest()
    except ValueError:
        return f"[不支持的算法] {algorithm}"


def hmac_text(text: str, key: str, algorithm: str) -> str:
    """计算 HMAC。"""
    name = algorithm.lower().replace("-", "")
    try:
        digest = hmac.new(key.encode("utf-8"), text.encode("utf-8"), name)
        return digest.hexdigest()
    except ValueError:
        return f"[不支持的算法] {algorithm}"


def hash_file(path: str, algorithm: str, chunk_size: int = 1024 * 1024) -> str:
    """分块计算文件哈希，避免大文件占满内存。"""
    name = algorithm.lower().replace("-", "")
    try:
        digest = hashlib.new(name)
    except ValueError:
        return f"[不支持的算法] {algorithm}"
    try:
        with open(path, "rb") as f:
            while chunk := f.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        return f"[读取失败] {exc}"
    return digest.hexdigest()
