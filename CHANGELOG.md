# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2025-06-17

### Added
- 🌍 **全局依赖扫描功能**
  - npm 全局包扫描（含准确大小和路径）
  - pip 全局包扫描
  - yarn 全局包扫描
  - 多包管理器统一管理
- 📋 **新增 `depx global-deps` 命令**
  - 支持按包管理器类型筛选 (`--type`)
  - 支持多种排序方式 (`--sort-by`)
  - 支持限制显示数量 (`--limit`)
- 🔧 **GitHub Actions CI/CD**
  - 多 Python 版本测试 (3.8-3.12)
  - 多操作系统测试 (Ubuntu, Windows, macOS)
  - 自动代码质量检查
  - 自动安全扫描
- 📦 **自动发布流程**
  - TestPyPI 测试发布
  - PyPI 正式发布
  - 标签触发发布
- 🧪 **完善的测试覆盖**
  - 15 个测试用例
  - 全局扫描器专项测试
  - CLI 命令测试

### Enhanced
- 📚 **完整的文档**
  - 详细的命令说明和示例
  - 安装和使用指南
  - 开发环境设置
  - 发布流程说明
- 🏗️ **项目结构优化**
  - 现代 Python 打包配置 (`pyproject.toml`)
  - 完善的 `MANIFEST.in`
  - MIT 许可证
- 🎨 **用户体验改进**
  - 美观的命令行输出
  - 详细的帮助信息
  - 错误处理优化

### Technical
- 📊 **数据结构扩展**
  - `GlobalDependencyInfo` 全局依赖信息
  - `PackageManagerType` 包管理器类型枚举
  - 扩展的 `DependencyType` 支持全局依赖
- 🔍 **智能检测**
  - 自动检测系统中可用的包管理器
  - 优雅处理命令不可用的情况
  - 并发安全的多包管理器扫描

## [0.1.0] - 2025-06-17

### Added
- 🏗️ **基础架构**
  - 模块化设计：Scanner、Parser、Analyzer、CLI
  - 可扩展的解析器架构
- 📁 **Node.js 项目支持**
  - package.json 解析
  - node_modules 分析
  - 依赖分类（生产、开发、可选、同级）
  - 精确的磁盘空间计算
- 🔄 **依赖分析功能**
  - 重复依赖检测
  - 清理建议生成
  - 空间占用统计
- 🎯 **命令行界面**
  - `depx scan` - 项目扫描
  - `depx analyze` - 依赖分析
  - `depx info` - 项目信息
- 🧪 **基础测试**
  - 项目扫描器测试
  - 核心功能验证

---

## 发布说明

### 如何升级

```bash
# 从 PyPI 升级
pip install --upgrade depx

# 验证版本
depx --version
```

### 新功能使用

```bash
# 扫描全局依赖
depx global-deps

# 按包管理器筛选
depx global-deps --type npm

# 按大小排序
depx global-deps --sort-by size --limit 10
```

### 兼容性

- Python 3.8+ 支持
- 跨平台：Windows、macOS、Linux
- 向后兼容所有 0.1.x 版本的命令
