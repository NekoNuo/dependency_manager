"""
国际化功能测试
"""

import pytest
from pathlib import Path

from depx.i18n import I18nManager, get_text, set_language, get_current_language


class TestI18nManager:
    """国际化管理器测试"""

    def setup_method(self):
        """测试前设置"""
        self.i18n = I18nManager()

    def test_default_language(self):
        """测试默认语言"""
        assert self.i18n.get_current_language() == "en"

    def test_set_language(self):
        """测试设置语言"""
        # 设置为中文
        result = self.i18n.set_language("zh")
        assert result is True
        assert self.i18n.get_current_language() == "zh"

        # 设置为英文
        result = self.i18n.set_language("en")
        assert result is True
        assert self.i18n.get_current_language() == "en"

        # 设置不支持的语言
        result = self.i18n.set_language("fr")
        assert result is False
        assert self.i18n.get_current_language() == "en"  # 保持原语言

    def test_get_text_english(self):
        """测试获取英文文本"""
        self.i18n.set_language("en")
        
        # 测试简单键
        text = self.i18n.get_text("cli.main.description")
        assert "Depx - Local Multi-language Dependency Manager" in text

        # 测试嵌套键
        text = self.i18n.get_text("cli.scan.help")
        assert "Scan specified directory" in text

    def test_get_text_chinese(self):
        """测试获取中文文本"""
        self.i18n.set_language("zh")
        
        # 测试简单键
        text = self.i18n.get_text("cli.main.description")
        assert "本地多语言依赖统一管理器" in text

        # 测试嵌套键
        text = self.i18n.get_text("cli.scan.help")
        assert "扫描指定目录" in text

    def test_get_text_with_formatting(self):
        """测试带格式化的文本"""
        self.i18n.set_language("en")
        
        text = self.i18n.get_text("messages.scanning", path="/test/path")
        assert "/test/path" in text

    def test_get_text_fallback(self):
        """测试文本回退机制"""
        # 测试不存在的键
        text = self.i18n.get_text("nonexistent.key")
        assert text == "nonexistent.key"

    def test_auto_detect_language(self):
        """测试自动检测语言"""
        detected = self.i18n.auto_detect_language()
        assert detected in ["en", "zh"]


class TestGlobalFunctions:
    """全局函数测试"""

    def test_global_functions(self):
        """测试全局便捷函数"""
        # 测试设置语言
        result = set_language("zh")
        assert result is True
        assert get_current_language() == "zh"

        # 测试获取文本
        text = get_text("cli.main.description")
        assert "本地多语言依赖统一管理器" in text

        # 切换回英文
        set_language("en")
        text = get_text("cli.main.description")
        assert "Local Multi-language Dependency Manager" in text


class TestLanguageFiles:
    """语言文件测试"""

    def test_language_files_exist(self):
        """测试语言文件是否存在"""
        i18n_dir = Path(__file__).parent.parent / "depx" / "i18n"
        
        assert (i18n_dir / "en.yaml").exists()
        assert (i18n_dir / "zh.yaml").exists()

    def test_language_file_structure(self):
        """测试语言文件结构"""
        i18n = I18nManager()
        
        # 测试必要的键是否存在
        required_keys = [
            "cli.main.description",
            "cli.scan.help",
            "cli.analyze.help",
            "messages.scanning",
            "tables.projects.title",
        ]
        
        for lang in ["en", "zh"]:
            i18n.set_language(lang)
            for key in required_keys:
                text = i18n.get_text(key)
                assert text != key, f"Missing translation for {key} in {lang}"


if __name__ == "__main__":
    pytest.main([__file__])
