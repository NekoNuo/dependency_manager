# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2025-06-17

### Added
- 🌍 **智能多语言支持**
  - 自动检测系统语言环境（中文/英文）
  - 5 种语言检测方法：DEPX_LANG、LANG、LC_ALL、系统 locale、终端设置
  - 支持多种语言格式：zh_CN.UTF-8、en_US.UTF-8、zh-CN、en-US 等
  - 智能回退机制，检测失败时安全回退到英文
- 🎯 **完整的国际化界面**
  - 所有用户界面文本完全本地化（中文/英文）
  - 运行时语言切换：`--lang zh/en` 参数
  - 环境变量支持：`DEPX_LANG=zh/en`
  - 表格、消息、帮助信息全面多语言化
- 📚 **增强的帮助系统**
  - 详细的命令描述和使用示例
  - 准确展示支持的 7 种编程语言信息
  - 每种语言的配置文件和包管理器详情
  - 自定义 Click Group 提供丰富的帮助信息
- 🔍 **语言检测调试功能**
  - 新增 `depx config --lang-info` 命令
  - 显示详细的环境变量和系统设置
  - 提供完整的故障排除信息
  - 支持调试模式查看检测过程

### Enhanced
- 🧠 **智能检测算法**
  - 多重检测机制确保可靠性
  - 支持中文各种变体：大陆、台湾、香港、新加坡
  - 支持英文各种变体：美国、英国、加拿大、澳大利亚
  - 性能优化的快速检测算法
- 🎨 **用户体验大幅提升**
  - 零配置使用：开箱即用的语言适配
  - 智能适配：自动适应用户语言环境
  - 灵活覆盖：支持手动指定和环境变量
  - 友好的错误提示和调试信息

### Technical
- 🏗️ **国际化架构**
  - 新增 `depx/i18n/` 模块
  - 基于 YAML 的翻译文件系统
  - 支持嵌套键和参数格式化
  - 完善的错误处理和回退机制
- 📦 **依赖更新**
  - 新增 `pyyaml>=6.0.0` 依赖
  - 保持 Python 3.8-3.12 完全兼容
- 🧪 **测试覆盖增强**
  - 新增 10 个国际化测试用例
  - 完整的多语言功能测试
  - 跨平台语言检测验证

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
