#!/usr/bin/env python3
"""
Depx 快速启动脚本
自动检查环境并提供多种运行方式

使用方法:
    python quick_start.py
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_version():
    """检查 Python 版本"""
    if sys.version_info < (3, 8):
        print("❌ Depx 需要 Python 3.8 或更高版本")
        print(f"当前版本: {sys.version}")
        return False
    return True

def check_dependencies():
    """检查并安装依赖"""
    required_deps = ["click", "rich", "pyyaml"]
    missing_deps = []
    
    for dep in required_deps:
        try:
            __import__(dep.replace("-", "_"))
        except ImportError:
            missing_deps.append(dep)
    
    if missing_deps:
        print(f"📦 检测到缺少依赖: {', '.join(missing_deps)}")
        install = input("是否自动安装缺少的依赖？(y/N): ").strip().lower()
        
        if install in ['y', 'yes']:
            try:
                print("🔄 正在安装依赖...")
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install"
                ] + missing_deps)
                print("✅ 依赖安装完成！")
                return True
            except subprocess.CalledProcessError:
                print("❌ 依赖安装失败，请手动安装：")
                print(f"pip install {' '.join(missing_deps)}")
                return False
        else:
            print("❌ 请手动安装依赖：")
            print(f"pip install {' '.join(missing_deps)}")
            return False
    
    return True

def show_startup_menu():
    """显示启动菜单"""
    menu = """
🚀 Depx 快速启动

请选择运行方式：

1. 🖥️  交互式界面 - 友好的菜单界面
2. 📋 命令行模式 - 直接运行命令
3. 📊 快速分析 - 分析当前目录
4. 🔍 快速搜索 - 搜索包
5. ❓ 显示帮助 - 查看所有命令

请输入选项编号 (1-5): """
    return input(menu).strip()

def run_interactive():
    """运行交互式界面"""
    try:
        subprocess.run([sys.executable, "interactive_depx.py"])
    except FileNotFoundError:
        print("❌ 找不到 interactive_depx.py 文件")

def run_command_mode():
    """运行命令行模式"""
    print("\n📋 命令行模式")
    print("输入 'exit' 退出")
    
    while True:
        try:
            cmd = input("\ndepx> ").strip()
            if cmd.lower() in ['exit', 'quit']:
                break
            if not cmd:
                continue
                
            # 运行命令
            subprocess.run([sys.executable, "run_depx.py"] + cmd.split())
            
        except KeyboardInterrupt:
            print("\n👋 退出命令行模式")
            break

def quick_analyze():
    """快速分析当前目录"""
    print("\n📊 正在分析当前目录...")
    subprocess.run([sys.executable, "run_depx.py", "info", "."])

def quick_search():
    """快速搜索"""
    package = input("\n🔍 请输入要搜索的包名: ").strip()
    if package:
        subprocess.run([sys.executable, "run_depx.py", "search", package])

def show_help():
    """显示帮助"""
    subprocess.run([sys.executable, "run_depx.py", "--help"])

def main():
    """主函数"""
    print("🚀 Depx 快速启动器")
    print("=" * 50)
    
    # 检查 Python 版本
    if not check_python_version():
        sys.exit(1)
    
    # 检查并安装依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 检查必要文件
    required_files = ["run_depx.py", "interactive_depx.py", "depx"]
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ 缺少必要文件: {', '.join(missing_files)}")
        print("请确保在 Depx 项目根目录中运行此脚本")
        sys.exit(1)
    
    print("✅ 环境检查完成！")
    
    while True:
        try:
            choice = show_startup_menu()
            
            if choice == "1":
                run_interactive()
            elif choice == "2":
                run_command_mode()
            elif choice == "3":
                quick_analyze()
            elif choice == "4":
                quick_search()
            elif choice == "5":
                show_help()
            else:
                print("❌ 无效选项，请输入 1-5 之间的数字")
            
            # 询问是否继续
            if choice in ["1", "2"]:
                break
            else:
                continue_choice = input("\n是否继续使用？(Y/n): ").strip().lower()
                if continue_choice in ['n', 'no']:
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 感谢使用 Depx！")
            break

if __name__ == "__main__":
    main()
