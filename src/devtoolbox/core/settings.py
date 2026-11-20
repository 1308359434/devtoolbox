"""设置持久化：基于 QSettings。"""

from PySide6.QtCore import QSettings

_SETTINGS = QSettings("DevToolBox", "DevToolBox")

THEME_KEY = "appearance/theme"
WINDOW_GEOMETRY_KEY = "window/geometry"


def get_theme() -> str:
    """返回主题：light 或 dark。默认跟随系统。"""
    value = _SETTINGS.value(THEME_KEY, "system", type=str)
    return value if value in {"light", "dark", "system"} else "system"


def set_theme(theme: str) -> None:
    """保存主题设置。"""
    if theme not in {"light", "dark", "system"}:
        raise ValueError(f"未知主题: {theme}")
    _SETTINGS.setValue(THEME_KEY, theme)
    _SETTINGS.sync()


def save_geometry(data: bytes) -> None:
    """保存窗口位置与大小。"""
    _SETTINGS.setValue(WINDOW_GEOMETRY_KEY, data)
    _SETTINGS.sync()


def load_geometry() -> bytes | None:
    """读取窗口位置与大小，未设置时返回 None。"""
    value = _SETTINGS.value(WINDOW_GEOMETRY_KEY)
    return value if isinstance(value, bytes) else None
