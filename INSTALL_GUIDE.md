# Depx 安装指南

## 🚀 快速安装

### 方法1: 一键安装脚本（推荐）

**Linux/macOS:**
```bash
# 快速安装（推荐）
curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/quick_install.sh | bash

# 或者完整交互式安装
curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/install_and_run.sh -o install_depx.sh
bash install_depx.sh
```

**Windows PowerShell:**
```powershell
# 一键安装运行
irm https://raw.githubusercontent.com/NekoNuo/depx/main/install_and_run.ps1 | iex
```

### 方法2: 使用 pip 安装

```bash
# 从 PyPI 安装（稳定版本）
pip install depx --user

# 验证安装
python -m depx --version
```

### 方法3: 从源码安装（最新功能）

```bash
# 克隆仓库
git clone https://github.com/NekoNuo/depx.git
cd depx

# 安装依赖
pip install -r requirements.txt --user

# 直接运行
python -m depx --help
```

## 📋 使用方法

### 基本命令

```bash
# 分析当前目录
python -m depx info .

# 搜索包（搜索所有包管理器）
python -m depx search react

# 扫描项目
python -m depx scan

# 查看帮助
python -m depx --help
```

### 交互式界面

```bash
# 启动交互式界面
python interactive_depx.py
```

## 🔧 故障排除

### 常见问题

1. **下载失败**
   - 检查网络连接
   - 尝试使用代理或VPN
   - 使用备选安装方法

2. **权限问题**
   - 使用 `--user` 参数安装到用户目录
   - 避免使用 `sudo` 安装 Python 包

3. **编码问题（Windows）**
   - 确保控制台支持 UTF-8
   - 使用 PowerShell 而不是 cmd

4. **Python 版本**
   - 需要 Python 3.8 或更高版本
   - 使用 `python3` 而不是 `python`

### 获取帮助

- GitHub Issues: https://github.com/NekoNuo/depx/issues
- 文档: https://github.com/NekoNuo/depx/blob/master/README.md

## 🆕 版本说明

- **v0.8.8**: 修复搜索功能，改善一键脚本兼容性
- **v0.8.7**: 稳定版本（PyPI）
- **开发版**: 最新功能，从源码安装

## 🌟 功能特性

- ✅ 跨语言依赖管理（Node.js, Python, Rust, Java, Go, PHP, C#）
- ✅ 统一搜索所有包管理器
- ✅ 智能项目检测
- ✅ 交互式界面
- ✅ 跨平台支持（Windows, macOS, Linux）
- ✅ 中英文界面
