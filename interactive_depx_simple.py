#!/usr/bin/env python3
"""
Depx 简化交互式运行脚本 - Windows 兼容版本
专为 Windows 环境优化，避免编码和显示问题

使用方法:
    python interactive_depx_simple.py
"""

import sys
import os
from pathlib import Path

# 简化的编码设置
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"

# 添加当前目录到 Python 路径
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
        print("缺少必要的依赖包，请先安装：")
        print(f"pip install {' '.join(missing_deps)}")
        return False
    
    return True

def show_banner():
    """显示简化横幅"""
    print("=" * 60)
    print("                    Depx v0.8.8")
    print("               跨语言依赖管理工具")
    print("                 简化交互模式")
    print("=" * 60)

def show_menu():
    """显示简化菜单"""
    menu = """
请选择要执行的操作：

1. 分析项目依赖 (info)
2. 搜索包 (search) - 搜索所有包管理器
3. 安装包 (install)
4. 卸载包 (uninstall)
5. 更新包 (update)
6. 清理依赖 (clean)
7. 扫描全局依赖 (scan)
8. 导出结果 (export)
9. 配置管理 (config)
0. 退出

请输入选项编号 (0-9): """
    return input(menu).strip()

def get_path_input():
    """获取路径输入"""
    path = input("请输入项目路径 (默认为当前目录 '.'): ").strip()
    return path if path else "."

def get_package_input():
    """获取包名输入"""
    return input("请输入包名: ").strip()

def execute_command(cmd_args):
    """执行命令 - 简化版本"""
    try:
        from depx.cli import cli
        
        # 保存原始 sys.argv
        original_argv = sys.argv.copy()
        
        # 设置新的 sys.argv
        sys.argv = ["depx"] + cmd_args
        
        print(f"执行命令: depx {' '.join(cmd_args)}")
        print("-" * 50)
        
        # 执行命令
        cli()
        
        print("-" * 50)
        print("命令执行完成")
        
        # 恢复原始 sys.argv
        sys.argv = original_argv
        
    except SystemExit:
        # Click 会调用 sys.exit()，这是正常的
        sys.argv = original_argv
    except Exception as e:
        print(f"执行错误: {e}")
        sys.argv = original_argv

def main():
    """主函数 - 简化版本"""
    # 检查依赖
    if not check_dependencies():
        input("按 Enter 键退出...")
        sys.exit(1)
    
    show_banner()
    print("Windows 简化交互模式 - 避免编码问题")
    print("如果遇到问题，请使用命令行模式")
    print("")
    
    while True:
        try:
            choice = show_menu()
            
            if choice == "0":
                print("感谢使用 Depx！")
                break
            elif choice == "1":
                # 分析项目依赖
                path = get_path_input()
                print(f"\n正在分析项目: {path}")
                execute_command(["info", path])
            elif choice == "2":
                # 搜索包
                package = get_package_input()
                if package:
                    print(f"\n正在搜索包: {package} (所有包管理器)")
                    execute_command(["search", package])
            elif choice == "3":
                # 安装包
                package = get_package_input()
                if package:
                    print(f"\n正在安装包: {package}")
                    execute_command(["install", package])
            elif choice == "4":
                # 卸载包
                package = get_package_input()
                if package:
                    print(f"\n正在卸载包: {package}")
                    execute_command(["uninstall", package])
            elif choice == "5":
                # 更新包
                package = input("请输入包名 (留空检查所有过时包): ").strip()
                if package:
                    print(f"\n正在更新包: {package}")
                    execute_command(["update", package])
                else:
                    print(f"\n正在检查过时的包...")
                    execute_command(["update", "--check"])
            elif choice == "6":
                # 清理依赖
                path = get_path_input()
                print(f"\n正在清理项目: {path}")
                execute_command(["clean", path])
            elif choice == "7":
                # 扫描全局依赖
                print(f"\n正在扫描全局依赖...")
                execute_command(["scan"])
            elif choice == "8":
                # 导出结果
                path = get_path_input()
                print(f"\n正在导出分析结果: {path}")
                execute_command(["export", path])
            elif choice == "9":
                # 配置管理
                print(f"\n配置管理")
                execute_command(["config"])
            else:
                print("无效选项，请输入 0-9 之间的数字")
            
            # 等待用户按键继续
            if choice != "0":
                input("\n按 Enter 键继续...")
                print("\n" + "=" * 60)
                
        except KeyboardInterrupt:
            print("\n\n感谢使用 Depx！")
            break
        except Exception as e:
            print(f"错误: {e}")
            input("\n按 Enter 键继续...")

if __name__ == "__main__":
    main()
