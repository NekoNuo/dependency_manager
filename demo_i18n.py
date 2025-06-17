#!/usr/bin/env python3
"""
Depx 多语言支持演示脚本

展示新增的国际化功能和增强的帮助信息
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from depx.i18n import set_language, get_text, get_current_language
from depx.utils.language_info import format_language_support_info, get_language_statistics
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def demo_language_switching():
    """演示语言切换功能"""
    console.print("\n🌍 [bold blue]多语言支持演示[/bold blue]")
    
    # 英文模式
    console.print("\n📝 [yellow]English Mode:[/yellow]")
    set_language("en")
    console.print(f"Current language: {get_current_language()}")
    console.print(f"Main description: {get_text('cli.main.description')}")
    console.print(f"Scan help: {get_text('cli.scan.help')}")
    
    # 中文模式
    console.print("\n📝 [yellow]中文模式：[/yellow]")
    set_language("zh")
    console.print(f"当前语言: {get_current_language()}")
    console.print(f"主要描述: {get_text('cli.main.description')}")
    console.print(f"扫描帮助: {get_text('cli.scan.help')}")


def demo_language_support_info():
    """演示语言支持信息"""
    console.print("\n🎯 [bold blue]支持的编程语言信息[/bold blue]")
    
    # 英文版本
    console.print("\n📝 [yellow]English Version:[/yellow]")
    en_info = format_language_support_info("en")
    console.print(Panel(en_info, title="Supported Languages", border_style="green"))
    
    # 中文版本
    console.print("\n📝 [yellow]中文版本：[/yellow]")
    zh_info = format_language_support_info("zh")
    console.print(Panel(zh_info, title="支持的语言", border_style="blue"))


def demo_statistics():
    """演示统计信息"""
    console.print("\n📊 [bold blue]语言支持统计[/bold blue]")
    
    stats = get_language_statistics()
    
    table = Table(title="Language Support Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Count", justify="right", style="yellow")
    
    table.add_row("Supported Languages", str(stats["supported_languages"]))
    table.add_row("Planned Languages", str(stats["planned_languages"]))
    table.add_row("Total Config Files", str(stats["total_config_files"]))
    table.add_row("Total Package Managers", str(stats["total_package_managers"]))
    
    console.print(table)


def demo_help_messages():
    """演示帮助信息"""
    console.print("\n❓ [bold blue]帮助信息演示[/bold blue]")
    
    # 英文帮助
    set_language("en")
    console.print("\n📝 [yellow]English Help Messages:[/yellow]")
    
    help_table = Table(title="Command Help (English)")
    help_table.add_column("Command", style="cyan")
    help_table.add_column("Help Text", style="white")
    
    commands = ["scan", "analyze", "info", "global_deps", "clean", "export", "config"]
    for cmd in commands:
        help_text = get_text(f"cli.{cmd}.help")
        help_table.add_row(cmd, help_text[:60] + "..." if len(help_text) > 60 else help_text)
    
    console.print(help_table)
    
    # 中文帮助
    set_language("zh")
    console.print("\n📝 [yellow]中文帮助信息：[/yellow]")
    
    help_table_zh = Table(title="命令帮助（中文）")
    help_table_zh.add_column("命令", style="cyan")
    help_table_zh.add_column("帮助文本", style="white")
    
    for cmd in commands:
        help_text = get_text(f"cli.{cmd}.help")
        help_table_zh.add_row(cmd, help_text[:60] + "..." if len(help_text) > 60 else help_text)
    
    console.print(help_table_zh)


def demo_formatted_messages():
    """演示格式化消息"""
    console.print("\n💬 [bold blue]格式化消息演示[/bold blue]")
    
    # 英文格式化消息
    set_language("en")
    console.print("\n📝 [yellow]English Formatted Messages:[/yellow]")
    console.print(get_text("messages.scanning", path="/home/user/projects"))
    console.print(get_text("messages.found_projects", count=15))
    console.print(get_text("messages.scan_depth", depth=5))
    
    # 中文格式化消息
    set_language("zh")
    console.print("\n📝 [yellow]中文格式化消息：[/yellow]")
    console.print(get_text("messages.scanning", path="/home/user/projects"))
    console.print(get_text("messages.found_projects", count=15))
    console.print(get_text("messages.scan_depth", depth=5))


def main():
    """主函数"""
    console.print("🚀 [bold green]Depx 多语言支持和增强帮助信息演示[/bold green]")
    console.print("=" * 60)
    
    try:
        # 演示各种功能
        demo_language_switching()
        demo_language_support_info()
        demo_statistics()
        demo_help_messages()
        demo_formatted_messages()
        
        console.print("\n✅ [bold green]演示完成！[/bold green]")
        console.print("\n💡 [yellow]提示：[/yellow]")
        console.print("• 使用 'depx --help' 查看增强的帮助信息")
        console.print("• 使用 'depx --lang zh' 切换到中文界面")
        console.print("• 使用 'depx --lang en' 切换到英文界面")
        console.print("• 设置环境变量 DEPX_LANG=zh 来默认使用中文")
        
    except Exception as e:
        console.print(f"\n❌ [red]演示过程中出现错误：{e}[/red]")
        import traceback
        console.print(traceback.format_exc())


if __name__ == "__main__":
    main()
