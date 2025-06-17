"""
国际化模块

提供多语言支持功能
"""

from .i18n_manager import (
    I18nManager,
    get_text,
    set_language,
    get_current_language,
    auto_detect_and_set_language,
    get_language_detection_info
)

__all__ = [
    "I18nManager",
    "get_text",
    "set_language",
    "get_current_language",
    "auto_detect_and_set_language",
    "get_language_detection_info"
]
