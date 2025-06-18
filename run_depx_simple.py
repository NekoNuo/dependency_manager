#!/usr/bin/env python3
"""
Depx 简化运行脚本 (无 emoji，兼容所有系统)
无需安装即可使用 Depx 的所有功能

使用方法:
    python run_depx_simple.py [命令] [选项]
    
示例:
    python run_depx_simple.py info .
    python run_depx_simple.py search lodash
    python run_depx_simple.py install express
    python run_depx_simple.py update --check
"""

import sys
import os
from pathlib import Path

# 添加当前目录到 Python 路径，以便导入 depx 模块
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def check_dependencies():
    """检查必要的依赖是否可用"""
    missing_deps = []
    
    try:
        import click
    except ImportError:
        missing_deps.append("click")
    
    try:
        import rich
    except ImportError:
        missing_deps.append("rich")
    
    try:
        import yaml
    except ImportError:
        missing_deps.append("pyyaml")
    
    if missing_deps:
        print("ERROR: 缺少必要的依赖包，请先安装：")
        print(f"pip install {' '.join(missing_deps)}")
        print("\n或者使用以下命令安装所有依赖：")
        print("pip install click rich pyyaml")
        return False
    
    return True

def main():
    """主函数"""
    print("Depx 简化运行模式")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    try:
        # 导入并运行 Depx CLI
        from depx.cli import cli
        
        # 如果没有提供参数，显示帮助信息
        if len(sys.argv) == 1:
            print("可用命令：")
            print("  info      - 分析项目依赖信息")
            print("  search    - 搜索包")
            print("  install   - 安装包")
            print("  uninstall - 卸载包")
            print("  update    - 更新包")
            print("  clean     - 清理未使用的依赖")
            print("  scan      - 扫描全局依赖")
            print("  export    - 导出分析结果")
            print("  config    - 配置管理")
            print("\n使用 'python run_depx_simple.py [命令] --help' 查看详细帮助")
            print("\n示例：")
            print("  python run_depx_simple.py info .")
            print("  python run_depx_simple.py search lodash")
            print("  python run_depx_simple.py install express")
            sys.exit(0)
        
        # 运行 CLI
        cli()
        
    except ImportError as e:
        print(f"ERROR: 导入错误: {e}")
        print("请确保在 Depx 项目根目录中运行此脚本")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: 运行错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
