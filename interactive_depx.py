#!/usr/bin/env python3
"""
Depx 交互式运行脚本
提供友好的交互界面，无需安装即可使用

使用方法:
    python interactive_depx.py
"""

import sys
import os
from pathlib import Path

# 设置 UTF-8 编码
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())
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
        print("❌ 缺少必要的依赖包，请先安装：")
        print(f"pip install {' '.join(missing_deps)}")
        return False
    
    return True

def show_banner():
    """显示欢迎横幅"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                        🚀 Depx v0.8.5                        ║
║                   跨语言依赖管理工具                          ║
║                     交互式运行模式                           ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def show_menu():
    """显示主菜单"""
    menu = """
📋 请选择要执行的操作：

1. 📊 分析项目依赖 (info)
2. 🔍 搜索包 (search)
3. 📦 安装包 (install)
4. 🗑️  卸载包 (uninstall)
5. 🔄 更新包 (update)
6. 🧹 清理依赖 (clean)
7. 🌐 扫描全局依赖 (scan)
8. 📤 导出结果 (export)
9. ⚙️  配置管理 (config)
0. 🚪 退出

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
    """执行命令"""
    try:
        from depx.cli import cli
        
        # 保存原始 sys.argv
        original_argv = sys.argv.copy()
        
        # 设置新的 sys.argv
        sys.argv = ["depx"] + cmd_args
        
        # 执行命令
        cli()
        
        # 恢复原始 sys.argv
        sys.argv = original_argv
        
    except SystemExit:
        # Click 会调用 sys.exit()，这是正常的
        pass
    except Exception as e:
        print(f"❌ 执行错误: {e}")

def main():
    """主函数"""
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    show_banner()
    
    while True:
        try:
            choice = show_menu()
            
            if choice == "0":
                print("👋 感谢使用 Depx！")
                break
            elif choice == "1":
                # 分析项目依赖
                path = get_path_input()
                print(f"\n🔍 正在分析项目: {path}")
                execute_command(["info", path])
            elif choice == "2":
                # 搜索包
                package = get_package_input()
                if package:
                    print(f"\n🔍 正在搜索包: {package}")
                    execute_command(["search", package])
            elif choice == "3":
                # 安装包
                package = get_package_input()
                if package:
                    print(f"\n📦 正在安装包: {package}")
                    execute_command(["install", package])
            elif choice == "4":
                # 卸载包
                package = get_package_input()
                if package:
                    print(f"\n🗑️ 正在卸载包: {package}")
                    execute_command(["uninstall", package])
            elif choice == "5":
                # 更新包
                package = input("请输入包名 (留空更新所有包): ").strip()
                if package:
                    print(f"\n🔄 正在更新包: {package}")
                    execute_command(["update", package])
                else:
                    print(f"\n🔄 正在检查过时的包...")
                    execute_command(["update", "--check"])
            elif choice == "6":
                # 清理依赖
                path = get_path_input()
                print(f"\n🧹 正在清理项目: {path}")
                execute_command(["clean", path])
            elif choice == "7":
                # 扫描全局依赖
                print(f"\n🌐 正在扫描全局依赖...")
                execute_command(["scan"])
            elif choice == "8":
                # 导出结果
                path = get_path_input()
                print(f"\n📤 正在导出分析结果: {path}")
                execute_command(["export", path])
            elif choice == "9":
                # 配置管理
                print(f"\n⚙️ 配置管理")
                execute_command(["config"])
            else:
                print("❌ 无效选项，请输入 0-9 之间的数字")
            
            # 等待用户按键继续
            if choice != "0":
                input("\n按 Enter 键继续...")
                
        except KeyboardInterrupt:
            print("\n\n👋 感谢使用 Depx！")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")
            input("\n按 Enter 键继续...")

if __name__ == "__main__":
    main()
