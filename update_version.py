#!/usr/bin/env python3
"""
快速版本更新脚本
使用方法: python update_version.py 0.8.4
"""

import sys
import re
import os

def update_version_in_file(new_version):
    """更新 version.py 文件中的版本号"""
    version_file = "version.py"
    
    if not os.path.exists(version_file):
        print(f"❌ 版本文件不存在: {version_file}")
        return False
    
    try:
        # 读取文件
        with open(version_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换版本号
        new_content = re.sub(
            r'VERSION = "[^"]*"',
            f'VERSION = "{new_version}"',
            content
        )
        
        # 写回文件
        with open(version_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 已更新版本文件: {new_version}")
        return True
        
    except Exception as e:
        print(f"❌ 更新版本文件失败: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("使用方法: python update_version.py <新版本号>")
        print("示例: python update_version.py 0.8.4")
        sys.exit(1)
    
    new_version = sys.argv[1]
    
    # 验证版本号格式
    if not re.match(r'^\d+\.\d+\.\d+$', new_version):
        print("❌ 版本号格式错误，应为 x.y.z 格式")
        sys.exit(1)
    
    print(f"🔄 正在更新版本号到 {new_version}...")
    
    # 更新版本文件
    if not update_version_in_file(new_version):
        sys.exit(1)
    
    # 运行版本管理工具更新所有文件
    import subprocess
    try:
        result = subprocess.run([sys.executable, "version.py", "update"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 所有文件版本号更新完成")
            print(result.stdout)
        else:
            print("❌ 更新其他文件失败")
            print(result.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"❌ 运行版本管理工具失败: {e}")
        sys.exit(1)
    
    print(f"🎉 版本更新完成！新版本: {new_version}")

if __name__ == "__main__":
    main()
