"""
Depx 命令行界面

提供用户友好的命令行接口
"""

import logging
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.text import Text

from .core.scanner import ProjectScanner
from .core.analyzer import DependencyAnalyzer
from .parsers.base import ProjectType, DependencyType
from .utils.file_utils import format_size

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Rich 控制台
console = Console()


@click.group()
@click.version_option(version="0.1.0")
@click.option('--verbose', '-v', is_flag=True, help='启用详细输出')
def cli(verbose: bool):
    """
    Depx - 本地多语言依赖统一管理器
    
    统一发现、信息透明、空间优化、跨平台支持
    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)


@cli.command()
@click.argument('path', type=click.Path(exists=True, path_type=Path), default='.')
@click.option('--depth', '-d', default=5, help='扫描深度 (默认: 5)')
@click.option('--type', '-t', 'project_types', multiple=True, 
              type=click.Choice([pt.value for pt in ProjectType if pt != ProjectType.UNKNOWN]),
              help='指定项目类型')
@click.option('--parallel/--no-parallel', default=True, help='是否使用并行处理')
def scan(path: Path, depth: int, project_types: tuple, parallel: bool):
    """扫描指定目录，发现项目和依赖"""
    
    console.print(f"\n🔍 扫描目录: [bold blue]{path.absolute()}[/bold blue]")
    console.print(f"📏 扫描深度: {depth}")
    console.print(f"⚡ 并行处理: {'启用' if parallel else '禁用'}")
    
    if project_types:
        console.print(f"🎯 项目类型: {', '.join(project_types)}")
    
    scanner = ProjectScanner()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("正在扫描项目...", total=None)
        
        try:
            projects = scanner.scan_directory(path, depth, parallel)
        except Exception as e:
            console.print(f"[red]扫描失败: {e}[/red]")
            sys.exit(1)
        
        progress.update(task, description="扫描完成")
    
    if not projects:
        console.print("\n[yellow]未发现任何项目[/yellow]")
        return
    
    # 过滤项目类型
    if project_types:
        filtered_types = [ProjectType(pt) for pt in project_types]
        projects = [p for p in projects if p.project_type in filtered_types]
    
    console.print(f"\n✅ 发现 [bold green]{len(projects)}[/bold green] 个项目")
    
    # 显示项目列表
    _display_projects_table(projects)


@cli.command()
@click.argument('path', type=click.Path(exists=True, path_type=Path), default='.')
@click.option('--depth', '-d', default=5, help='扫描深度 (默认: 5)')
@click.option('--sort-by', '-s', default='size', 
              type=click.Choice(['name', 'size', 'type']),
              help='排序方式')
@click.option('--limit', '-l', default=20, help='显示数量限制')
def analyze(path: Path, depth: int, sort_by: str, limit: int):
    """分析项目依赖，生成详细报告"""
    
    console.print(f"\n📊 分析目录: [bold blue]{path.absolute()}[/bold blue]")
    
    scanner = ProjectScanner()
    analyzer = DependencyAnalyzer()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        # 扫描项目
        scan_task = progress.add_task("正在扫描项目...", total=None)
        projects = scanner.scan_directory(path, depth)
        progress.update(scan_task, description="扫描完成")
        
        if not projects:
            console.print("\n[yellow]未发现任何项目[/yellow]")
            return
        
        # 分析依赖
        analyze_task = progress.add_task("正在分析依赖...", total=None)
        report = analyzer.analyze_projects(projects)
        progress.update(analyze_task, description="分析完成")
    
    # 显示分析报告
    _display_analysis_report(report, sort_by, limit)


@cli.command()
@click.argument('project_path', type=click.Path(exists=True, path_type=Path))
def info(project_path: Path):
    """显示单个项目的详细信息"""
    
    scanner = ProjectScanner()
    
    console.print(f"\n📋 项目信息: [bold blue]{project_path.absolute()}[/bold blue]")
    
    project = scanner.scan_single_project(project_path)
    
    if not project:
        console.print("[red]无法识别项目类型或解析失败[/red]")
        return
    
    _display_project_info(project)


def _display_projects_table(projects):
    """显示项目列表表格"""
    table = Table(title="发现的项目")
    
    table.add_column("项目名称", style="cyan", no_wrap=True)
    table.add_column("类型", style="magenta")
    table.add_column("路径", style="blue")
    table.add_column("依赖数量", justify="right", style="green")
    table.add_column("总大小", justify="right", style="yellow")
    
    for project in projects:
        table.add_row(
            project.name,
            project.project_type.value,
            str(project.path),
            str(len(project.dependencies)),
            format_size(project.total_size_bytes)
        )
    
    console.print(table)


def _display_analysis_report(report, sort_by: str, limit: int):
    """显示分析报告"""
    summary = report["summary"]
    
    # 总览面板
    summary_text = f"""
📊 总项目数: {summary['total_projects']}
📦 总依赖数: {summary['total_dependencies']}
💾 总占用空间: {summary['total_size_formatted']}
    """
    
    console.print(Panel(summary_text.strip(), title="📈 总览", border_style="green"))
    
    # 最大依赖表格
    dep_stats = report["dependency_stats"]
    if dep_stats.largest_dependencies:
        dep_table = Table(title="🔥 占用空间最大的依赖")
        dep_table.add_column("依赖名称", style="cyan")
        dep_table.add_column("大小", justify="right", style="yellow")
        
        for name, size in dep_stats.largest_dependencies[:limit]:
            dep_table.add_row(name, format_size(size))
        
        console.print(dep_table)
    
    # 重复依赖
    duplicates = report["duplicate_dependencies"]
    if duplicates["count"] > 0:
        dup_table = Table(title="🔄 重复依赖")
        dup_table.add_column("依赖名称", style="cyan")
        dup_table.add_column("项目数", justify="right", style="magenta")
        dup_table.add_column("版本数", justify="right", style="blue")
        dup_table.add_column("总大小", justify="right", style="yellow")
        dup_table.add_column("可节省", justify="right", style="green")
        
        for dup in duplicates["dependencies"][:limit]:
            dup_table.add_row(
                dup["name"],
                str(dup["project_count"]),
                str(dup["version_count"]),
                dup["total_size_formatted"],
                format_size(dup["potential_savings"])
            )
        
        console.print(dup_table)
    
    # 清理建议
    suggestions = report["cleanup_suggestions"]
    if suggestions:
        console.print("\n💡 [bold yellow]清理建议[/bold yellow]")
        for suggestion in suggestions:
            console.print(f"• {suggestion['title']}: {suggestion['description']}")
            console.print(f"  潜在节省: {format_size(suggestion['potential_savings'])}")


def _display_project_info(project):
    """显示单个项目的详细信息"""
    # 项目基本信息
    info_text = f"""
📁 项目名称: {project.name}
🏷️  项目类型: {project.project_type.value}
📍 项目路径: {project.path}
⚙️  配置文件: {project.config_file}
📦 依赖数量: {len(project.dependencies)}
💾 总大小: {format_size(project.total_size_bytes)}
    """
    
    console.print(Panel(info_text.strip(), title="📋 项目信息", border_style="blue"))
    
    # 依赖列表
    if project.dependencies:
        dep_table = Table(title="📦 依赖列表")
        dep_table.add_column("名称", style="cyan")
        dep_table.add_column("版本", style="magenta")
        dep_table.add_column("类型", style="blue")
        dep_table.add_column("大小", justify="right", style="yellow")
        
        for dep in project.dependencies:
            dep_table.add_row(
                dep.name,
                dep.installed_version or dep.version,
                dep.dependency_type.value,
                format_size(dep.size_bytes)
            )
        
        console.print(dep_table)


def main():
    """主入口函数"""
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[yellow]操作已取消[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]发生错误: {e}[/red]")
        if logger.isEnabledFor(logging.DEBUG):
            import traceback
            console.print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
