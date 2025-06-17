#!/usr/bin/env python3
"""
Depx 部署脚本生成器
生成各种平台的一键运行脚本
"""

import os
import sys
from pathlib import Path

def generate_curl_command(repo_url):
    """生成 curl 一键运行命令"""
    return f"curl -fsSL {repo_url}/raw/master/install_and_run.sh | bash"

def generate_powershell_command(repo_url):
    """生成 PowerShell 一键运行命令"""
    return f"irm {repo_url}/raw/master/install_and_run.ps1 | iex"

def generate_wget_command(repo_url):
    """生成 wget 一键运行命令"""
    return f"wget -qO- {repo_url}/raw/master/install_and_run.sh | bash"

def generate_docker_command(repo_url):
    """生成 Docker 一键运行命令"""
    return f"""# Docker 方式运行 Depx
docker run --rm -it -v $(pwd):/workspace python:3.9-slim bash -c "
cd /workspace &&
curl -fsSL {repo_url}/raw/master/install_and_run.sh | bash
" """

def generate_github_codespaces_command(repo_url):
    """生成 GitHub Codespaces 命令"""
    return f"""# GitHub Codespaces 中运行
curl -fsSL {repo_url}/raw/master/install_and_run.sh | bash"""

def generate_replit_command(repo_url):
    """生成 Replit 命令"""
    return f"""# Replit 中运行
curl -fsSL {repo_url}/raw/master/install_and_run.sh | bash"""

def create_deployment_readme(repo_url):
    """创建部署说明文档"""
    content = f"""# Depx 一键运行部署指南

## 🚀 快速开始

### Linux/macOS/WSL
```bash
{generate_curl_command(repo_url)}
```

### Windows PowerShell
```powershell
{generate_powershell_command(repo_url)}
```

### 使用 wget (如果没有 curl)
```bash
{generate_wget_command(repo_url)}
```

## 🐳 Docker 环境

```bash
{generate_docker_command(repo_url)}
```

## ☁️ 云端环境

### GitHub Codespaces
```bash
{generate_github_codespaces_command(repo_url)}
```

### Replit
```bash
{generate_replit_command(repo_url)}
```

### Google Colab
```python
# 在 Colab 中运行
!curl -fsSL {repo_url}/raw/master/install_and_run.sh | bash
```

## 📱 移动端

### Termux (Android)
```bash
pkg install python git
{generate_curl_command(repo_url)}
```

### iSH (iOS)
```bash
apk add python3 py3-pip git curl
{generate_curl_command(repo_url)}
```

## 🌐 在线试用

### 方法1: GitHub Codespaces
1. 访问 {repo_url}
2. 点击 "Code" -> "Codespaces" -> "Create codespace"
3. 在终端中运行: `{generate_curl_command(repo_url)}`

### 方法2: Gitpod
1. 访问 `https://gitpod.io/#{repo_url}`
2. 在终端中运行: `{generate_curl_command(repo_url)}`

### 方法3: Replit
1. 访问 https://replit.com
2. 创建新的 Python 项目
3. 在 Shell 中运行: `{generate_curl_command(repo_url)}`

## 🔧 自定义部署

### 下载到本地
```bash
# 下载独立包
curl -L {repo_url}/archive/master.zip -o depx.zip
unzip depx.zip
cd depx-master
python quick_start.py
```

### 克隆仓库
```bash
git clone {repo_url}.git
cd depx
python quick_start.py
```

## 📋 系统要求

- Python 3.8+
- pip
- 网络连接

## 🆘 故障排除

### 问题1: Python 版本过低
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3.9 python3.9-pip

# CentOS/RHEL
sudo yum install python39 python39-pip

# macOS
brew install python@3.9
```

### 问题2: 网络连接问题
```bash
# 使用代理
export https_proxy=http://proxy.example.com:8080
{generate_curl_command(repo_url)}
```

### 问题3: 权限问题
```bash
# 使用用户安装
pip install --user click rich pyyaml
{generate_curl_command(repo_url)}
```

## 🎯 使用示例

### 快速分析项目
```bash
# 一键运行并分析当前目录
{generate_curl_command(repo_url)}
# 选择选项 3 (快速分析)
```

### 搜索包
```bash
# 一键运行并搜索包
{generate_curl_command(repo_url)}
# 选择选项 4 (快速搜索)
# 输入包名，如: lodash
```

### 交互式使用
```bash
# 一键运行交互界面
{generate_curl_command(repo_url)}
# 选择选项 1 (交互式界面)
```

---

🎉 享受 Depx 的便捷体验！无需安装，即开即用！
"""
    
    return content

def main():
    """主函数"""
    # 默认仓库 URL，可以通过命令行参数修改
    repo_url = "https://github.com/your-username/depx"
    
    if len(sys.argv) > 1:
        repo_url = sys.argv[1]
    
    print("🚀 Depx 部署脚本生成器")
    print("=" * 50)
    
    # 生成各种命令
    print("📋 一键运行命令:")
    print(f"Linux/macOS: {generate_curl_command(repo_url)}")
    print(f"Windows:     {generate_powershell_command(repo_url)}")
    print(f"wget:        {generate_wget_command(repo_url)}")
    print()
    
    # 创建部署文档
    readme_content = create_deployment_readme(repo_url)
    
    # 保存到文件
    with open("DEPLOYMENT.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ 部署文档已生成: DEPLOYMENT.md")
    
    # 生成 HTML 版本（可选）
    try:
        import markdown
        html_content = markdown.markdown(readme_content)
        with open("deployment.html", "w", encoding="utf-8") as f:
            f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Depx 部署指南</title>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
""")
        print("✅ HTML 版本已生成: deployment.html")
    except ImportError:
        print("ℹ️  安装 markdown 包可生成 HTML 版本: pip install markdown")

if __name__ == "__main__":
    main()
