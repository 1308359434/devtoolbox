"""UUID 生成逻辑。"""

import uuid


def generate(version: int = 4, count: int = 1, uppercase: bool = False) -> str:
    """批量生成 UUID。version 支持 1 或 4。"""
    if version not in (1, 4):
        return "[错误] 仅支持 UUID v1 与 v4"
    if not 1 <= count <= 1000:
        return "[错误] 数量须在 1 到 1000 之间"
    factory = uuid.uuid1 if version == 1 else uuid.uuid4
    values = [str(factory()) for _ in range(count)]
    if uppercase:
        values = [v.upper() for v in values]
    return "\n".join(values)
