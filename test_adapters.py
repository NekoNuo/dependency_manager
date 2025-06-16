#!/usr/bin/env python3
"""
测试可用的适配器
"""
import sys
import logging
from pathlib import Path

from depman.core.config import Config
from depman.core.manager import DependencyManager
from depman.adapters.npm import NpmAdapter
from depman.adapters.pip import PipAdapter
from depman.adapters.brew import BrewAdapter

def setup_logging():
    """配置日志"""
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    
    # 创建控制台处理器
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    
    # 添加处理器到根记录器
    root_logger.addHandler(console)

def main():
    """主函数"""
    setup_logging()
    
    print("测试DepMan适配器")
    print("-" * 40)
    
    # 测试npm适配器
    npm = NpmAdapter()
    print(f"NPM适配器: {npm.name}")
    print(f"- 可用: {npm.is_available()}")
    print(f"- 依赖类型: {npm.dependency_type}")
    
    # 测试pip适配器
    pip = PipAdapter()
    print(f"\nPip适配器: {pip.name}")
    print(f"- 可用: {pip.is_available()}")
    print(f"- 依赖类型: {pip.dependency_type}")
    
    # 测试brew适配器
    brew = BrewAdapter()
    print(f"\nBrew适配器: {brew.name}")
    print(f"- 可用: {brew.is_available()}")
    print(f"- 依赖类型: {brew.dependency_type}")
    
    # 测试DependencyManager
    print("\n\n测试DependencyManager")
    print("-" * 40)
    
    config = Config()
    manager = DependencyManager(config)
    
    # 强制手动加载npm适配器
    print("\n手动加载npm适配器")
    npm_adapter = manager._load_adapter("npm")
    if npm_adapter:
        print(f"成功加载npm适配器: {npm_adapter.name}")
    else:
        print("无法加载npm适配器")
    
    # 扫描当前目录
    print("\n扫描当前目录：")
    scan_results = manager.scan_project(Path.cwd())
    if scan_results:
        print(f"发现依赖项:")
        for result in scan_results:
            print(f"- {result}")
    else:
        print("未发现依赖项")
    
    # 扫描node.js示例项目
    node_project = Path("examples/node_project")
    if node_project.exists():
        print(f"\n扫描Node.js项目 ({node_project}):")
        adapter = manager._get_adapter_for_project(node_project)
        if adapter:
            print(f"找到适配器: {adapter.name}")
            scan_results = manager.scan_project(node_project)
            if scan_results:
                print(f"发现依赖项:")
                for result in scan_results:
                    print(f"- {result}")
            else:
                print("未发现依赖项")
        else:
            print(f"未找到适配器处理项目")
    
    # 扫描Python示例项目
    py_project = Path("examples/python_project")
    if py_project.exists():
        print(f"\n扫描Python项目 ({py_project}):")
        adapter = manager._get_adapter_for_project(py_project)
        if adapter:
            print(f"找到适配器: {adapter.name}")
            scan_results = manager.scan_project(py_project)
            if scan_results:
                print(f"发现依赖项:")
                for result in scan_results:
                    print(f"- {result}")
            else:
                print("未发现依赖项")
        else:
            print(f"未找到适配器处理项目")
    
    # 打印出所有已注册的适配器
    print("\n已注册的适配器:")
    for dep_type, adapter in manager._adapters.items():
        print(f"- {adapter.name} ({dep_type})")

if __name__ == "__main__":
    main() 