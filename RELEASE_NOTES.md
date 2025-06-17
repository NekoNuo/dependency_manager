# Depx v0.4.0 发布说明

🎉 **Depx v0.4.0 正式发布！**

这是一个重大版本更新，新增了全局依赖管理功能，并完善了 CI/CD 流程。

## 🌟 主要新功能

### 🌍 全局依赖扫描
- **npm 全局包扫描**：显示准确的大小和完整路径
- **pip 全局包扫描**：列出所有已安装的 Python 包
- **yarn 全局包扫描**：基础支持 yarn 全局包
- **多包管理器统一管理**：一个命令查看所有全局依赖

### 📋 新增命令
```bash
# 扫描所有全局依赖
depx global-deps

# 按包管理器筛选
depx global-deps --type npm
depx global-deps --type pip

# 排序和限制
depx global-deps --sort-by size --limit 10
```

## 🔧 技术改进

### 🏗️ GitHub Actions CI/CD
- **多版本测试**：Python 3.8-3.12
- **多平台测试**：Ubuntu, Windows, macOS
- **自动发布**：标签触发 TestPyPI，Release 触发 PyPI
- **代码质量检查**：Flake8, Black, isort
- **安全扫描**：Bandit, Safety

### 📦 现代化打包
- **pyproject.toml**：现代 Python 打包标准
- **自动化构建**：GitHub Actions 自动构建和发布
- **完整文档**：详细的使用说明和开发指南

## 📊 实际测试结果

在真实环境中的测试表现：

```
🌍 扫描全局依赖...
✅ 发现 83 个全局依赖
📦 检测到的包管理器: npm, pip

🌍 全局依赖
┏━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 依赖名称 ┃ 版本    ┃ 包管理器 ┃    大小 ┃ 安装路径                                           ┃
┡━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ pnpm     │ 10.12.1 │ npm      │ 18.2 MB │ /Users/user/.nvm/versions/node/v18.18.0/lib/...   │
│ npm      │ 9.8.1   │ npm      │ 10.3 MB │ /Users/user/.nvm/versions/node/v18.18.0/lib/...   │
│ corepack │ 0.19.0  │ npm      │  1.5 MB │ /Users/user/.nvm/versions/node/v18.18.0/lib/...   │
└──────────┴─────────┴──────────┴─────────┴────────────────────────────────────────────────────┘
```

## 🚀 如何升级

### 从 PyPI 安装/升级
```bash
# 新安装
pip install depx

# 升级现有版本
pip install --upgrade depx

# 验证版本
depx --version
```

### 从源码安装
```bash
git clone https://github.com/yourusername/depx.git
cd depx
pip install -e .
```

## 🧪 测试覆盖

- **15 个测试用例**全部通过
- **多平台兼容性**验证
- **实际环境**功能测试

## 📚 完整功能列表

### 项目级依赖管理
- ✅ Node.js 项目扫描和分析
- ✅ 依赖分类（生产、开发、可选、同级）
- ✅ 重复依赖检测
- ✅ 清理建议生成
- ✅ 精确的磁盘空间计算

### 全局依赖管理 ⭐ 新增
- ✅ npm 全局包扫描
- ✅ pip 全局包扫描
- ✅ yarn 全局包扫描
- ✅ 多包管理器统一视图
- ✅ 灵活的筛选和排序

### 命令行工具
- ✅ `depx scan` - 项目扫描
- ✅ `depx analyze` - 依赖分析
- ✅ `depx info` - 项目信息
- ✅ `depx global-deps` - 全局依赖 ⭐ 新增

## 🗺️ 下一步计划

### v0.5.0 (计划中)
- 🚧 Python 项目支持
- 🚧 依赖清理功能
- 🚧 配置文件支持
- 🚧 性能优化

### v0.6.0 (未来)
- 🔮 Java/Maven/Gradle 支持
- 🔮 Go 项目支持
- 🔮 Web 界面 (可选)
- 🔮 依赖安全扫描

## 🤝 贡献

我们欢迎各种形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 📞 支持

如果您遇到任何问题或有建议，请：
- 提交 [GitHub Issue](https://github.com/yourusername/depx/issues)
- 参与 [GitHub Discussions](https://github.com/yourusername/depx/discussions)

---

**感谢使用 Depx！** 🎉

让依赖管理变得简单高效！
