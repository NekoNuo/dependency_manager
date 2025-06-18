# Depx - 通用多语言依赖管理器

[![版本](https://img.shields.io/badge/version-0.9.0-blue.svg)](https://github.com/NekoNuo/depx)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![许可证](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![平台](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/NekoNuo/depx)

🚀 **Depx** 是一个强大的跨平台依赖管理工具，为多种编程语言提供统一发现、透明信息、空间优化和跨平台支持。

## ✨ 核心特性

- 🌍 **多语言支持**: Node.js、Python、Rust、Java、Go、PHP、C#
- 🔍 **统一搜索**: 同时搜索所有包管理器的包
- 🧠 **智能检测**: 自动检测项目类型和首选包管理器
- 💻 **跨平台**: Windows、macOS、Linux 原生支持
- 🎯 **交互界面**: 用户友好的菜单驱动界面
- 🌐 **多语言界面**: 中英文界面支持
- ⚡ **高性能**: 优化的扫描和分析算法

## 🚀 快速开始

### 一键安装

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/NekoNuo/depx/main/install_and_run.ps1 | iex
```

**macOS/Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/quick_install.sh | bash
```

### 手动安装

```bash
# 从 PyPI 安装
pip install depx --user

# 验证安装
python -m depx --version
```

## 📋 使用示例

### 基本命令

```bash
# 分析当前目录
python -m depx info .

# 搜索包（所有包管理器）
python -m depx search react

# 扫描项目
python -m depx scan

# 安装包
python -m depx install express

# 更新包
python -m depx update --check

# 清理依赖
python -m depx clean .
```

### 交互模式

```bash
# 启动交互界面
python interactive_depx.py

# Windows 优化界面
powershell -File windows_interactive.ps1
```

## 🛠️ 支持的包管理器

| 语言 | 包管理器 | 状态 |
|------|----------|------|
| **Node.js** | npm, yarn, pnpm | ✅ 完全支持 |
| **Python** | pip, conda | ✅ 完全支持 |
| **Rust** | cargo | ✅ 完全支持 |
| **Java** | maven, gradle | ✅ 完全支持 |
| **Go** | go modules | ✅ 完全支持 |
| **PHP** | composer | ✅ 完全支持 |
| **C#** | nuget, dotnet | ✅ 完全支持 |

## 🔧 配置

Depx 支持通过 YAML 文件进行灵活配置：

```yaml
# .depx.yaml
scan:
  max_depth: 5
  parallel: true
  project_types: ["nodejs", "python", "rust"]

cleanup:
  auto_confirm: false
  backup_enabled: true

log_level: "INFO"
cache_enabled: true
```

## 📊 功能概览

### 项目分析
- **依赖发现**: 自动查找和分析依赖关系
- **大小计算**: 计算每个依赖的磁盘空间使用
- **过时检测**: 识别需要更新的包
- **安全扫描**: 检查已知漏洞

### 包搜索
- **统一搜索**: 跨 npm、PyPI、crates.io、Maven Central 等搜索
- **智能过滤**: 按语言、流行度或维护状态过滤结果
- **详细信息**: 获取全面的包信息

### 依赖管理
- **批量操作**: 安装、更新或删除多个包
- **版本管理**: 处理版本冲突和约束
- **环境隔离**: 尊重虚拟环境和项目边界

## 🌐 国际化

Depx 自动检测您的系统语言并提供本地化界面：

- **English**: 完整功能支持
- **中文**: 完整功能支持
- **自动检测**: 智能语言切换

## 🔍 故障排除

### 常见问题

1. **安装问题**
   ```bash
   # 使用备选安装方法
   curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/quick_install.sh | bash
   ```

2. **权限问题**
   ```bash
   # 安装到用户目录
   pip install depx --user
   ```

3. **Windows 编码问题**
   ```powershell
   # 使用 Windows 优化脚本
   powershell -File windows_interactive.ps1
   ```

### 获取帮助

- 📖 **文档**: [GitHub Wiki](https://github.com/NekoNuo/depx/wiki)
- 🐛 **错误报告**: [GitHub Issues](https://github.com/NekoNuo/depx/issues)
- 💬 **讨论**: [GitHub Discussions](https://github.com/NekoNuo/depx/discussions)

## 🤝 贡献

我们欢迎贡献！请查看我们的[贡献指南](CONTRIBUTING.md)了解详情。

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/NekoNuo/depx.git
cd depx

# 安装依赖
pip install -r requirements.txt

# 运行测试
python -m pytest tests/

# 运行开发版本
python -m depx --help
```

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 感谢所有贡献者和用户
- 受到各种包管理工具的启发
- 为开发者社区用 ❤️ 构建

---

**由 Depx 团队用 ❤️ 制作**

[🏠 主页](https://github.com/NekoNuo/depx) | [📖 文档](https://github.com/NekoNuo/depx/wiki) | [🐛 问题](https://github.com/NekoNuo/depx/issues)
