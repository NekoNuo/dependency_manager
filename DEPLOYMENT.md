# Depx 一键运行部署指南

## 🚀 快速开始

### Linux/macOS/WSL
```bash
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

### Windows PowerShell
```powershell
irm https://github.com/NekoNuo/depx/raw/master/install_and_run.ps1 | iex
```

### 使用 wget (如果没有 curl)
```bash
wget -qO- https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

## 🐳 Docker 环境

```bash
# Docker 方式运行 Depx
docker run --rm -it -v $(pwd):/workspace python:3.9-slim bash -c "
cd /workspace &&
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
" 
```

## ☁️ 云端环境

### GitHub Codespaces
```bash
# GitHub Codespaces 中运行
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

### Replit
```bash
# Replit 中运行
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

### Google Colab
```python
# 在 Colab 中运行
!curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

## 📱 移动端

### Termux (Android)
```bash
pkg install python git
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

### iSH (iOS)
```bash
apk add python3 py3-pip git curl
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

## 🌐 在线试用

### 方法1: GitHub Codespaces
1. 访问 https://github.com/NekoNuo/depx
2. 点击 "Code" -> "Codespaces" -> "Create codespace"
3. 在终端中运行: `curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash`

### 方法2: Gitpod
1. 访问 `https://gitpod.io/#https://github.com/NekoNuo/depx`
2. 在终端中运行: `curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash`

### 方法3: Replit
1. 访问 https://replit.com
2. 创建新的 Python 项目
3. 在 Shell 中运行: `curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash`

## 🔧 自定义部署

### 下载到本地
```bash
# 下载独立包
curl -L https://github.com/NekoNuo/depx/archive/master.zip -o depx.zip
unzip depx.zip
cd depx-master
python quick_start.py
```

### 克隆仓库
```bash
git clone https://github.com/NekoNuo/depx.git
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
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

### 问题3: 权限问题
```bash
# 使用用户安装
pip install --user click rich pyyaml
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
```

## 🎯 使用示例

### 快速分析项目
```bash
# 一键运行并分析当前目录
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
# 选择选项 3 (快速分析)
```

### 搜索包
```bash
# 一键运行并搜索包
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
# 选择选项 4 (快速搜索)
# 输入包名，如: lodash
```

### 交互式使用
```bash
# 一键运行交互界面
curl -fsSL https://github.com/NekoNuo/depx/raw/master/install_and_run.sh | bash
# 选择选项 1 (交互式界面)
```

---

🎉 享受 Depx 的便捷体验！无需安装，即开即用！
