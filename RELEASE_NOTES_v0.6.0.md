# Depx v0.6.0 发布说明

## 🎉 重大更新：智能多语言支持

我们很高兴地宣布 Depx v0.6.0 的发布！这是一个重要的功能更新，引入了完整的智能多语言支持系统，让 Depx 真正成为一个国际化的工具。

## 🌟 主要新功能

### 🧠 智能语言检测
- **自动检测系统语言**：无需手动设置，自动适应用户的语言环境
- **多重检测机制**：支持 5 种不同的语言检测方法
- **智能回退**：检测失败时安全回退到英文界面

### 🌍 完整的多语言支持
- **中英文双语界面**：所有用户界面文本完全本地化
- **运行时语言切换**：支持 `--lang` 参数动态切换语言
- **环境变量支持**：通过 `DEPX_LANG` 设置默认语言

### 📚 增强的帮助信息
- **详细的命令描述**：每个命令都有详细的使用说明
- **准确的语言支持信息**：实时显示支持的 7 种编程语言
- **丰富的使用示例**：提供完整的使用示例和最佳实践

### 🔍 语言检测调试
- **检测信息查看**：新增 `depx config --lang-info` 命令
- **详细的环境信息**：显示所有相关的环境变量和系统设置
- **故障排除指南**：提供完整的调试和故障排除信息

## 🚀 使用方式

### 完全自动（推荐）
```bash
# 系统自动检测语言环境，无需任何设置
depx scan
depx analyze
depx info .
```

### 环境变量设置
```bash
# 设置默认中文界面
export DEPX_LANG=zh
depx scan

# 设置默认英文界面
export DEPX_LANG=en
depx scan
```

### 临时语言切换
```bash
# 临时使用中文界面
depx --lang zh scan

# 临时使用英文界面
depx --lang en scan
```

### 查看语言检测信息
```bash
# 查看详细的语言检测信息
depx config --lang-info
```

## 📊 智能检测机制

### 检测优先级（从高到低）
1. **DEPX_LANG 环境变量** - 用户明确指定的语言偏好
2. **LANG 环境变量** - 系统主要语言设置
3. **LC_ALL 环境变量** - 系统全局语言设置
4. **系统默认 locale** - 操作系统默认语言
5. **终端语言设置** - 终端应用的语言配置
6. **回退到英文** - 如果所有检测都失败

### 支持的语言格式
- **中文**：`zh`, `zh_CN`, `zh_TW`, `zh_HK`, `zh-cn`, `chinese` 等
- **英文**：`en`, `en_US`, `en_GB`, `en_CA`, `en-us`, `english` 等

## 🎯 支持的编程语言

帮助信息现在准确显示支持的编程语言：

### 当前支持 (7种)
- **Node.js** - package.json, node_modules (npm, yarn, pnpm)
- **Python** - requirements.txt, setup.py, pyproject.toml, Pipfile
- **Java** - pom.xml (Maven), build.gradle (Gradle)
- **Go** - go.mod, go.sum, Gopkg.toml
- **Rust** - Cargo.toml, Cargo.lock
- **PHP** - composer.json, composer.lock
- **C#** - .csproj, packages.config, project.json

### 计划支持 (4种)
- **Ruby** - Gemfile, Gemfile.lock
- **Swift** - Package.swift
- **Dart** - pubspec.yaml, pubspec.lock
- **Scala** - build.sbt, project/build.properties

## 🔧 技术改进

### 国际化架构
- 新增 `depx/i18n/` 模块，提供完整的国际化支持
- 基于 YAML 的翻译文件，易于维护和扩展
- 支持嵌套键和参数格式化

### 错误处理增强
- 完善的错误处理和回退机制
- 翻译失败时优雅降级
- 详细的调试日志

### 性能优化
- 智能缓存机制，减少重复检测
- 快速语言检测算法
- 最小化系统调用

## 📈 用户体验提升

### 之前版本
```bash
# 用户需要手动指定语言
depx --lang zh scan    # 中文用户
depx --lang en scan    # 英文用户
```

### v0.6.0 版本
```bash
# 用户只需正常使用，系统自动适配
depx scan              # 自动检测并使用合适的语言
```

## 🧪 测试覆盖

- **单元测试**：新增 10 个国际化相关测试用例
- **功能测试**：完整的多语言功能测试
- **兼容性测试**：跨平台语言检测测试
- **性能测试**：语言检测性能验证

## 📦 依赖更新

### 新增依赖
- `pyyaml>=6.0.0` - YAML 文件解析支持

### 兼容性
- 保持与 Python 3.8-3.12 的完全兼容
- 所有新依赖都是必需的，但轻量级

## 🔄 升级指南

### 从 v0.5.x 升级
```bash
# 升级 Depx
pip install --upgrade depx

# 验证升级
depx --version  # 应显示 v0.6.0

# 体验新功能
depx config --lang-info
depx scan  # 自动语言检测
```

### 配置迁移
- 无需任何配置迁移
- 现有的使用方式完全兼容
- 新功能为可选增强

## 🐛 Bug 修复

- 修复了帮助信息格式化问题
- 改进了错误消息的显示
- 优化了表格输出的对齐

## 🚧 已知问题

- 某些特殊的 locale 设置可能需要手动指定语言
- 在某些终端中，中文字符可能显示不完整（终端配置问题）

## 🔮 下一步计划

### v0.7.0 规划
- 更多语言支持（日语、韩语、法语等）
- 依赖安全扫描功能
- Web 界面（可选）
- 插件系统

## 🙏 致谢

感谢所有用户的反馈和建议！特别感谢对多语言支持功能的需求反馈。

## 📞 支持

如果您在使用过程中遇到任何问题：

- 查看语言检测信息：`depx config --lang-info`
- 提交 Issue：[GitHub Issues](https://github.com/yourusername/depx/issues)
- 查看文档：[README.md](README.md)

---

**下载地址**：[PyPI](https://pypi.org/project/depx/)  
**源代码**：[GitHub](https://github.com/yourusername/depx)  
**更新日志**：[CHANGELOG.md](CHANGELOG.md)

🎉 **Depx v0.6.0 - 让依赖管理更智能，更国际化！**
