# Depx 独立运行指南

无需安装即可使用 Depx 的所有功能！

## 🚀 一键运行（推荐）

### Linux/macOS 一键运行
```bash
curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/master/install_and_run.sh | bash
```

### Windows PowerShell 一键运行
```powershell
irm https://raw.githubusercontent.com/NekoNuo/depx/master/install_and_run.ps1 | iex
```

这些脚本会：
- ✅ 自动检查系统环境（Python、pip）
- ✅ 自动下载 Depx 最新版本
- ✅ 自动安装必要依赖
- ✅ 提供友好的交互界面
- ✅ 使用完毕后自动清理临时文件

## 🚀 本地快速开始

### 方法一：一键启动（推荐）

```bash
python quick_start.py
```

这个脚本会：
- 自动检查 Python 版本
- 自动检查并安装依赖
- 提供多种运行方式选择

### 方法二：交互式界面

```bash
python interactive_depx.py
```

提供友好的菜单界面，适合不熟悉命令行的用户。

### 方法三：直接命令行

```bash
python run_depx.py [命令] [选项]
```

直接运行 Depx 命令，适合熟悉命令行的用户。

## 📋 使用示例

### 基本命令

```bash
# 分析当前项目
python run_depx.py info .

# 搜索包
python run_depx.py search lodash

# 安装包
python run_depx.py install express

# 卸载包
python run_depx.py uninstall express

# 检查过时的包
python run_depx.py update --check

# 更新特定包
python run_depx.py update lodash

# 清理未使用的依赖
python run_depx.py clean .
```

### 高级功能

```bash
# 搜索所有包管理器
python run_depx.py search react --all

# 指定包管理器安装
python run_depx.py install numpy --package-manager pip

# 预览更新操作
python run_depx.py update --dry-run

# 导出分析结果
python run_depx.py export . --format json
```

## 🔧 环境要求

### Python 版本
- Python 3.8 或更高版本

### 必要依赖
- `click` - 命令行界面
- `rich` - 美化输出
- `pyyaml` - YAML 配置文件支持

### 自动安装依赖

使用 `quick_start.py` 会自动检查并提示安装缺少的依赖：

```bash
python quick_start.py
```

### 手动安装依赖

```bash
pip install click rich pyyaml
```

## 📁 文件说明

### 核心脚本

- **`quick_start.py`** - 一键启动脚本，自动检查环境
- **`interactive_depx.py`** - 交互式界面脚本
- **`run_depx.py`** - 直接命令行脚本

### 项目文件

- **`depx/`** - Depx 核心模块
- **`pyproject.toml`** - 项目配置
- **`README.md`** - 项目说明

## 🌟 功能特性

### 支持的包管理器
- **npm** - Node.js 包管理器
- **yarn** - Node.js 包管理器（替代方案）
- **pip** - Python 包管理器
- **cargo** - Rust 包管理器

### 支持的项目类型
- **Node.js** - JavaScript/TypeScript 项目
- **Python** - Python 项目
- **Rust** - Rust 项目

### 主要功能
- 📊 **依赖分析** - 分析项目依赖结构
- 🔍 **包搜索** - 跨语言包搜索
- 📦 **包安装** - 智能包安装
- 🗑️ **包卸载** - 安全包卸载
- 🔄 **包更新** - 智能包更新
- 🧹 **依赖清理** - 清理未使用的依赖
- 🌐 **全局扫描** - 扫描全局依赖
- 📤 **结果导出** - 导出分析结果

## 🎯 使用场景

### 开发者
- 快速分析新项目的依赖结构
- 搜索和比较不同语言的包
- 管理多语言项目的依赖

### 团队协作
- 统一的依赖管理工具
- 标准化的项目分析流程
- 跨平台的使用体验

### 学习和探索
- 了解不同语言的包生态
- 学习依赖管理最佳实践
- 探索新的技术栈

## 🔍 故障排除

### 常见问题

**Q: 提示缺少依赖怎么办？**
A: 运行 `python quick_start.py` 自动安装，或手动安装：`pip install click rich pyyaml`

**Q: 提示找不到模块怎么办？**
A: 确保在 Depx 项目根目录中运行脚本

**Q: Python 版本太低怎么办？**
A: 升级到 Python 3.8 或更高版本

**Q: 包管理器不兼容怎么办？**
A: 在对应的项目目录中使用，或使用 `--type` 参数指定项目类型

### 获取帮助

```bash
# 查看所有命令
python run_depx.py --help

# 查看特定命令帮助
python run_depx.py search --help
python run_depx.py install --help
```

## 📞 支持

如果遇到问题或有建议，请：
1. 检查本文档的故障排除部分
2. 查看项目的 README.md
3. 提交 Issue 或 Pull Request

---

🎉 享受使用 Depx 的便捷体验！
