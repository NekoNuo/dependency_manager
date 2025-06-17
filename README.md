# Depx - 本地多语言依赖统一管理器

🚀 **统一发现 • 信息透明 • 空间优化 • 跨平台支持**

Depx 是一个强大的本地依赖管理工具，能够自动识别和分析本地文件系统中各种编程语言项目的依赖关系，帮助开发者更好地管理和优化项目依赖。

## ✨ 核心特性

### 🔍 统一发现
- 自动识别本地文件系统中的各类编程语言项目
- 支持 Node.js、Python、Java、Go、Rust 等多种语言（逐步支持）
- 智能扫描项目配置文件和依赖目录

### 📊 信息透明
- 提供依赖的详细信息：名称、版本、大小、位置
- 清晰展示项目依赖关系和层级结构
- 支持多种排序和筛选方式

### 💾 空间优化
- 识别重复和冗余的依赖
- 计算精确的磁盘占用空间
- 提供智能清理建议

### 🌐 跨平台支持
- 在 Windows、macOS 和 Linux 上稳定运行
- 统一的命令行界面
- 美观的输出格式

## 🚀 快速开始

### 安装

```bash
# 克隆项目
git clone <repository-url>
cd depx

# 安装依赖
pip install -r requirements.txt

# 安装 Depx
pip install -e .
```

### 基本使用

```bash
# 扫描当前目录
depx scan

# 扫描指定目录
depx scan /path/to/projects

# 分析依赖并生成报告
depx analyze

# 查看单个项目信息
depx info /path/to/project

# 查看帮助
depx --help
```

## 📋 命令详解

### `depx scan` - 项目扫描

扫描指定目录，发现所有支持的项目类型。

```bash
# 基本扫描
depx scan

# 指定扫描深度
depx scan --depth 3

# 只扫描特定类型的项目
depx scan --type nodejs --type python

# 禁用并行处理
depx scan --no-parallel
```

### `depx analyze` - 依赖分析

深度分析项目依赖，生成详细报告。

```bash
# 基本分析
depx analyze

# 按大小排序
depx analyze --sort-by size

# 限制显示数量
depx analyze --limit 10
```

### `depx info` - 项目信息

显示单个项目的详细信息。

```bash
depx info /path/to/project
```

## 🏗️ 项目结构

```
depx/
├── depx/
│   ├── __init__.py
│   ├── cli.py              # 命令行入口
│   ├── core/
│   │   ├── scanner.py      # 项目扫描器
│   │   └── analyzer.py     # 依赖分析器
│   ├── parsers/
│   │   ├── base.py         # 基础解析器
│   │   └── nodejs.py       # Node.js 解析器
│   └── utils/
│       └── file_utils.py   # 文件工具
├── tests/                  # 测试文件
├── requirements.txt        # Python 依赖
└── setup.py               # 安装配置
```

## 🎯 当前支持

### ✅ 已支持
- **Node.js**: package.json, node_modules, npm/yarn/pnpm

### 🚧 计划支持
- **Python**: requirements.txt, setup.py, pyproject.toml, venv
- **Java**: pom.xml, build.gradle, Maven/Gradle 缓存
- **Go**: go.mod, go.sum, GOPATH/GOMODCACHE
- **Rust**: Cargo.toml, Cargo.lock, ~/.cargo
- **PHP**: composer.json, vendor/
- **C#**: *.csproj, packages.config, NuGet 缓存

## 🧪 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_scanner.py

# 运行测试并显示覆盖率
pytest --cov=depx
```

## 🤝 贡献指南

我们欢迎各种形式的贡献！

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🗺️ 开发路线图

### v0.1.0 (当前)
- ✅ 基础架构搭建
- ✅ Node.js 项目支持
- ✅ 命令行界面
- ✅ 基础测试

### v0.2.0 (计划中)
- 🚧 Python 项目支持
- 🚧 依赖清理功能
- 🚧 配置文件支持
- 🚧 性能优化

### v0.3.0 (未来)
- 🔮 Java/Maven/Gradle 支持
- 🔮 Go 项目支持
- 🔮 Web 界面 (可选)
- 🔮 依赖安全扫描

## 📞 联系我们

如果您有任何问题或建议，请通过以下方式联系我们：

- 提交 Issue
- 发起 Discussion
- 发送邮件

---

**Depx** - 让依赖管理变得简单高效！ 🎉