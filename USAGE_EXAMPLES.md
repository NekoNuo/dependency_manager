# Depx 使用示例

## 🚀 快速开始

### 一键运行（最简单）
```bash
# Linux/macOS
curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/master/install_and_run.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/NekoNuo/depx/master/install_and_run.ps1 | iex
```

## 📋 命令行使用示例

### 基本命令
```bash
# 查看帮助
python run_depx.py --help

# 查看版本
python run_depx.py --version

# 分析当前项目
python run_depx.py info .

# 分析指定项目
python run_depx.py info /path/to/project
```

### 包搜索
```bash
# 搜索包（自动检测包管理器）
python run_depx.py search lodash

# 搜索所有包管理器
python run_depx.py search react --all

# 搜索 npm 包
python run_depx.py search express --package-manager npm

# 搜索 Python 包
python run_depx.py search requests --package-manager pip
```

### 包安装
```bash
# 安装包（自动检测项目类型）
python run_depx.py install lodash

# 指定包管理器安装
python run_depx.py install express --package-manager npm
python run_depx.py install requests --package-manager pip

# 在指定目录安装
python run_depx.py install lodash --path /path/to/project
```

### 包更新
```bash
# 检查过时的包
python run_depx.py update --check

# 预览更新操作
python run_depx.py update --dry-run

# 更新特定包
python run_depx.py update lodash

# 更新所有包
python run_depx.py update
```

### 包卸载
```bash
# 卸载包
python run_depx.py uninstall lodash

# 指定包管理器卸载
python run_depx.py uninstall express --package-manager npm
```

### 全局依赖
```bash
# 扫描所有全局依赖
python run_depx.py global-deps

# 只扫描 npm 全局包
python run_depx.py global-deps --type npm

# 按大小排序
python run_depx.py global-deps --sort-by size

# 限制显示数量
python run_depx.py global-deps --limit 10
```

## 🖥️ 交互式界面使用

### 启动交互界面
```bash
python interactive_depx.py
```

### 菜单选项说明
- **选项 1**: 📊 分析项目依赖 - 分析指定项目的依赖结构
- **选项 2**: 🔍 搜索包 - 跨语言搜索包
- **选项 3**: 📦 安装包 - 智能安装包
- **选项 4**: 🗑️ 卸载包 - 安全卸载包
- **选项 5**: 🔄 更新包 - 检查和更新包
- **选项 6**: 🧹 清理依赖 - 清理未使用的依赖
- **选项 7**: 🌐 扫描全局依赖 - 扫描全局安装的包
- **选项 8**: 📤 导出结果 - 导出分析结果
- **选项 9**: ⚙️ 配置管理 - 管理 Depx 配置

## 🎯 实际使用场景

### 场景1：分析新项目
```bash
# 1. 进入项目目录
cd /path/to/new-project

# 2. 分析项目依赖
python run_depx.py info .

# 3. 检查是否有过时的依赖
python run_depx.py update --check
```

### 场景2：搜索和安装包
```bash
# 1. 搜索需要的包
python run_depx.py search axios

# 2. 安装包
python run_depx.py install axios

# 3. 验证安装
python run_depx.py info .
```

### 场景3：项目维护
```bash
# 1. 检查过时依赖
python run_depx.py update --check

# 2. 预览更新
python run_depx.py update --dry-run

# 3. 执行更新
python run_depx.py update

# 4. 清理未使用的依赖
python run_depx.py clean .
```

### 场景4：全局环境管理
```bash
# 1. 查看全局安装的包
python run_depx.py global-deps

# 2. 按大小排序查看
python run_depx.py global-deps --sort-by size --limit 20

# 3. 只查看 npm 全局包
python run_depx.py global-deps --type npm
```

## 💡 使用技巧

### 1. 语言切换
```bash
# 使用英文界面
python run_depx.py --lang en info .

# 使用中文界面
python run_depx.py --lang zh info .
```

### 2. 详细输出
```bash
# 启用详细日志
python run_depx.py --verbose info .
```

### 3. 组合使用
```bash
# 搜索并安装
python run_depx.py search lodash
python run_depx.py install lodash

# 检查并更新
python run_depx.py update --check
python run_depx.py update lodash
```

## ❓ 常见问题

### Q: 如何知道支持哪些命令？
A: 运行 `python run_depx.py --help` 查看所有可用命令

### Q: 如何查看特定命令的帮助？
A: 运行 `python run_depx.py <命令> --help`，例如：
```bash
python run_depx.py search --help
python run_depx.py install --help
```

### Q: 命令行模式和交互式模式有什么区别？
A: 
- **命令行模式**: 直接执行单个命令，适合脚本和专家用户
- **交互式模式**: 菜单驱动，逐步操作，适合新手和探索性使用

### Q: 如何在不同项目类型中使用？
A: Depx 会自动检测项目类型，也可以手动指定：
```bash
python run_depx.py install lodash --type nodejs
python run_depx.py install requests --type python
```
