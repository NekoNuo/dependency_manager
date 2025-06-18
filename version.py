#!/usr/bin/env python3
"""
Depx 版本管理
统一管理所有文件中的版本号
"""

# 版本号配置 - 只需要修改这里！
VERSION = "0.8.9"

# 需要更新版本号的文件列表
VERSION_FILES = {
    "pyproject.toml": {
        "pattern": r'version = "[^"]*"',
        "replacement": f'version = "{VERSION}"'
    },
    "depx/__init__.py": {
        "pattern": r'__version__ = "[^"]*"',
        "replacement": f'__version__ = "{VERSION}"'
    },
    # CLI 现在动态读取版本号，无需硬编码
    "install_and_run.sh": {
        "pattern": r'🚀 Depx v[0-9.]+',
        "replacement": f'🚀 Depx v{VERSION}'
    },
    "install_and_run.ps1": {
        "pattern": r'🚀 Depx v[0-9.]+',
        "replacement": f'🚀 Depx v{VERSION}'
    },
    "interactive_depx.py": {
        "pattern": r'🚀 Depx v[0-9.]+',
        "replacement": f'🚀 Depx v{VERSION}'
    }
}

def update_version():
    """更新所有文件中的版本号"""
    import re
    import os
    
    print(f"🔄 正在更新版本号到 {VERSION}...")
    
    updated_files = []
    failed_files = []
    
    for file_path, config in VERSION_FILES.items():
        try:
            if not os.path.exists(file_path):
                print(f"⚠️  文件不存在: {file_path}")
                continue
                
            # 读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 替换版本号
            new_content = re.sub(config["pattern"], config["replacement"], content)
            
            # 检查是否有变化
            if new_content != content:
                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_files.append(file_path)
                print(f"✅ 已更新: {file_path}")
            else:
                print(f"📝 无需更新: {file_path}")
                
        except Exception as e:
            failed_files.append((file_path, str(e)))
            print(f"❌ 更新失败: {file_path} - {e}")
    
    # 总结
    print(f"\n📊 更新完成:")
    print(f"✅ 成功更新: {len(updated_files)} 个文件")
    if failed_files:
        print(f"❌ 更新失败: {len(failed_files)} 个文件")
        for file_path, error in failed_files:
            print(f"   - {file_path}: {error}")
    
    if updated_files:
        print(f"\n🎯 已更新的文件:")
        for file_path in updated_files:
            print(f"   - {file_path}")
    
    return len(failed_files) == 0

def get_version():
    """获取当前版本号"""
    return VERSION

def check_version_consistency():
    """检查所有文件中的版本号是否一致"""
    import re
    import os
    
    print(f"🔍 检查版本号一致性...")
    
    inconsistent_files = []
    
    for file_path, config in VERSION_FILES.items():
        try:
            if not os.path.exists(file_path):
                continue
                
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找当前版本号
            match = re.search(config["pattern"], content)
            if match:
                current_line = match.group(0)
                expected_line = config["replacement"]
                if current_line != expected_line:
                    inconsistent_files.append({
                        "file": file_path,
                        "current": current_line,
                        "expected": expected_line
                    })
                    
        except Exception as e:
            print(f"❌ 检查失败: {file_path} - {e}")
    
    if inconsistent_files:
        print(f"⚠️  发现 {len(inconsistent_files)} 个文件版本号不一致:")
        for item in inconsistent_files:
            print(f"   📁 {item['file']}")
            print(f"      当前: {item['current']}")
            print(f"      期望: {item['expected']}")
        return False
    else:
        print(f"✅ 所有文件版本号一致: {VERSION}")
        return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "update":
            success = update_version()
            sys.exit(0 if success else 1)
        elif command == "check":
            consistent = check_version_consistency()
            sys.exit(0 if consistent else 1)
        elif command == "version":
            print(VERSION)
            sys.exit(0)
        else:
            print(f"❌ 未知命令: {command}")
            sys.exit(1)
    else:
        print(f"Depx 版本管理工具")
        print(f"当前版本: {VERSION}")
        print(f"\n使用方法:")
        print(f"  python version.py update  - 更新所有文件的版本号")
        print(f"  python version.py check   - 检查版本号一致性")
        print(f"  python version.py version - 显示当前版本号")
