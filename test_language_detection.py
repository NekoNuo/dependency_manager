#!/usr/bin/env python3
"""
智能语言检测测试脚本

测试 Depx 的智能语言检测功能
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from depx.i18n import get_language_detection_info, auto_detect_and_set_language, get_current_language
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def test_current_environment():
    """测试当前环境的语言检测"""
    console.print("\n🔍 [bold blue]当前环境语言检测[/bold blue]")
    
    # 获取检测信息
    info = get_language_detection_info()
    
    # 创建信息表格
    table = Table(title="语言检测详情")
    table.add_column("检测项目", style="cyan")
    table.add_column("检测结果", style="yellow")
    
    table.add_row("DEPX_LANG 环境变量", info["DEPX_LANG"])
    table.add_row("LANG 环境变量", info["LANG"])
    table.add_row("LC_ALL 环境变量", info["LC_ALL"])
    table.add_row("系统 Locale", info["system_locale"])
    table.add_row("检测到的语言", info["detected_language"])
    table.add_row("当前使用语言", info["current_language"])
    
    console.print(table)
    
    # 显示终端 locale 信息
    if "terminal_locale" in info and info["terminal_locale"] != "检测失败":
        console.print(f"\n📟 [bold green]终端 Locale 信息:[/bold green]")
        console.print(Panel(info["terminal_locale"], border_style="green"))


def test_different_scenarios():
    """测试不同场景下的语言检测"""
    console.print("\n🧪 [bold blue]不同场景测试[/bold blue]")
    
    # 保存原始环境变量
    original_depx_lang = os.environ.get("DEPX_LANG")
    original_lang = os.environ.get("LANG")
    original_lc_all = os.environ.get("LC_ALL")
    
    scenarios = [
        {
            "name": "场景1: 明确设置 DEPX_LANG=zh",
            "env": {"DEPX_LANG": "zh"},
            "expected": "zh"
        },
        {
            "name": "场景2: 明确设置 DEPX_LANG=en", 
            "env": {"DEPX_LANG": "en"},
            "expected": "en"
        },
        {
            "name": "场景3: 中文系统环境 (LANG=zh_CN.UTF-8)",
            "env": {"DEPX_LANG": None, "LANG": "zh_CN.UTF-8"},
            "expected": "zh"
        },
        {
            "name": "场景4: 英文系统环境 (LANG=en_US.UTF-8)",
            "env": {"DEPX_LANG": None, "LANG": "en_US.UTF-8"},
            "expected": "en"
        },
        {
            "name": "场景5: 台湾中文环境 (LANG=zh_TW.UTF-8)",
            "env": {"DEPX_LANG": None, "LANG": "zh_TW.UTF-8"},
            "expected": "zh"
        },
        {
            "name": "场景6: 英国英文环境 (LANG=en_GB.UTF-8)",
            "env": {"DEPX_LANG": None, "LANG": "en_GB.UTF-8"},
            "expected": "en"
        },
        {
            "name": "场景7: 无环境变量设置",
            "env": {"DEPX_LANG": None, "LANG": None, "LC_ALL": None},
            "expected": "en"  # 回退到英文
        }
    ]
    
    results_table = Table(title="场景测试结果")
    results_table.add_column("场景", style="cyan")
    results_table.add_column("预期", style="green")
    results_table.add_column("实际", style="yellow")
    results_table.add_column("结果", style="bold")
    
    for scenario in scenarios:
        # 设置测试环境
        for key, value in scenario["env"].items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        
        # 重新创建 I18nManager 实例来测试
        from depx.i18n.i18n_manager import I18nManager
        test_manager = I18nManager()
        detected = test_manager.auto_detect_language()
        
        # 记录结果
        status = "✅ 通过" if detected == scenario["expected"] else "❌ 失败"
        results_table.add_row(
            scenario["name"],
            scenario["expected"],
            detected,
            status
        )
    
    console.print(results_table)
    
    # 恢复原始环境变量
    if original_depx_lang is not None:
        os.environ["DEPX_LANG"] = original_depx_lang
    else:
        os.environ.pop("DEPX_LANG", None)
        
    if original_lang is not None:
        os.environ["LANG"] = original_lang
    else:
        os.environ.pop("LANG", None)
        
    if original_lc_all is not None:
        os.environ["LC_ALL"] = original_lc_all
    else:
        os.environ.pop("LC_ALL", None)


def test_locale_parsing():
    """测试 locale 字符串解析"""
    console.print("\n🔤 [bold blue]Locale 字符串解析测试[/bold blue]")
    
    from depx.i18n.i18n_manager import I18nManager
    manager = I18nManager()
    
    test_cases = [
        # 中文测试用例
        ("zh_CN.UTF-8", "zh"),
        ("zh_TW.UTF-8", "zh"),
        ("zh_HK.UTF-8", "zh"),
        ("zh-CN", "zh"),
        ("zh-TW", "zh"),
        ("zh", "zh"),
        ("chinese", "zh"),
        
        # 英文测试用例
        ("en_US.UTF-8", "en"),
        ("en_GB.UTF-8", "en"),
        ("en_CA.UTF-8", "en"),
        ("en-US", "en"),
        ("en-GB", "en"),
        ("en", "en"),
        ("english", "en"),
        
        # 无效测试用例
        ("fr_FR.UTF-8", None),
        ("de_DE.UTF-8", None),
        ("", None),
        ("invalid", None),
    ]
    
    parse_table = Table(title="Locale 解析测试")
    parse_table.add_column("输入", style="cyan")
    parse_table.add_column("预期", style="green")
    parse_table.add_column("实际", style="yellow")
    parse_table.add_column("结果", style="bold")
    
    for input_str, expected in test_cases:
        actual = manager._parse_locale_string(input_str)
        status = "✅ 通过" if actual == expected else "❌ 失败"
        
        parse_table.add_row(
            input_str or "(空字符串)",
            str(expected) if expected else "None",
            str(actual) if actual else "None",
            status
        )
    
    console.print(parse_table)


def show_usage_examples():
    """显示使用示例"""
    console.print("\n💡 [bold blue]使用示例[/bold blue]")
    
    examples = [
        "# 自动检测语言（推荐）",
        "depx scan",
        "",
        "# 手动指定中文",
        "depx --lang zh scan",
        "",
        "# 手动指定英文", 
        "depx --lang en scan",
        "",
        "# 通过环境变量设置默认语言",
        "export DEPX_LANG=zh",
        "depx scan  # 将使用中文界面",
        "",
        "# 查看语言检测详情",
        "python test_language_detection.py",
    ]
    
    console.print(Panel("\n".join(examples), title="使用示例", border_style="green"))


def main():
    """主函数"""
    console.print("🌍 [bold green]Depx 智能语言检测测试[/bold green]")
    console.print("=" * 60)
    
    try:
        # 测试当前环境
        test_current_environment()
        
        # 测试不同场景
        test_different_scenarios()
        
        # 测试 locale 解析
        test_locale_parsing()
        
        # 显示使用示例
        show_usage_examples()
        
        console.print("\n✅ [bold green]所有测试完成！[/bold green]")
        
    except Exception as e:
        console.print(f"\n❌ [red]测试过程中出现错误：{e}[/red]")
        import traceback
        console.print(traceback.format_exc())


if __name__ == "__main__":
    main()
