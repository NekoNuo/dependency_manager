# Depx 多语言支持和增强帮助功能

## 🌍 新增功能概览

本次更新为 Depx 添加了完整的多语言支持和大幅增强的帮助信息，让工具更加国际化和用户友好。

### ✨ 主要特性

1. **完整的多语言支持**
   - 支持中文（zh）和英文（en）
   - 自动检测系统语言
   - 运行时语言切换
   - 所有用户界面文本国际化

2. **增强的帮助信息**
   - 详细的命令描述和使用示例
   - 准确展示支持的编程语言
   - 每种语言的配置文件和包管理器信息
   - 美观的格式化输出

3. **智能语言检测**
   - 自动检测系统语言设置
   - 支持环境变量配置
   - 命令行参数覆盖

## 🚀 使用方法

### 基本语言切换

```bash
# 使用英文界面
depx --lang en scan

# 使用中文界面
depx --lang zh scan

# 查看中文帮助
depx --lang zh --help
```

### 环境变量配置

```bash
# 设置默认语言为中文
export DEPX_LANG=zh
depx scan  # 将使用中文界面

# 设置默认语言为英文
export DEPX_LANG=en
depx scan  # 将使用英文界面
```

### 增强的帮助信息

```bash
# 查看主帮助（包含支持的语言列表和示例）
depx --help

# 查看特定命令的详细帮助
depx scan --help
depx analyze --help
depx clean --help
```

## 📋 支持的语言展示

新的帮助系统会准确显示支持的编程语言：

### 🎯 当前支持的语言：
- **Node.js** - package.json, node_modules (npm, yarn, pnpm)
- **Python** - requirements.txt, setup.py, pyproject.toml, Pipfile
- **Java** - pom.xml (Maven), build.gradle (Gradle)
- **Go** - go.mod, go.sum, Gopkg.toml
- **Rust** - Cargo.toml, Cargo.lock
- **PHP** - composer.json, composer.lock
- **C#** - .csproj, packages.config, project.json

### 🚧 计划支持的语言：
- **Ruby** - Gemfile, Gemfile.lock (Bundler, gem)
- **Swift** - Package.swift (Swift Package Manager)
- **Dart** - pubspec.yaml, pubspec.lock (pub)
- **Scala** - build.sbt, project/build.properties (sbt)

## 💡 使用示例

### 中文界面示例

```bash
# 扫描项目（中文）
$ depx --lang zh scan ~/projects

🔍 扫描目录：/home/user/projects
📏 扫描深度：5
⚡ 并行处理：已启用

✅ 发现 3 个项目

┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃ 项目名称               ┃ 类型   ┃ 路径                         ┃ 依赖数量 ┃  总大小 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━┩
│ my-react-app           │ nodejs │ /home/user/projects/react    │       15 │ 45.2 MB │
│ my-python-app          │ python │ /home/user/projects/python   │       12 │ 38.1 MB │
│ my-go-app              │ go     │ /home/user/projects/go       │        8 │ 12.5 MB │
└────────────────────────┴────────┴──────────────────────────────┴──────────┴─────────┘
```

### 英文界面示例

```bash
# 分析依赖（英文）
$ depx --lang en analyze ~/projects

📊 Analyzing directory: /home/user/projects

✅ Found 3 projects

📈 Summary
📊 Total projects: 3
📦 Total dependencies: 35
💾 Total space used: 95.8 MB
```

## 🛠️ 技术实现

### 国际化架构

```
depx/i18n/
├── __init__.py          # 国际化模块入口
├── i18n_manager.py      # 国际化管理器
├── en.yaml             # 英文翻译文件
└── zh.yaml             # 中文翻译文件
```

### 核心组件

1. **I18nManager**: 负责语言切换和文本翻译
2. **语言文件**: YAML 格式的翻译文件，支持嵌套键和格式化
3. **自动检测**: 基于系统 locale 和环境变量的智能语言检测
4. **CLI 集成**: 与 Click 框架深度集成的多语言命令行界面

### 扩展性设计

- 易于添加新语言：只需创建新的 YAML 文件
- 支持复杂的文本格式化和参数替换
- 模块化设计，便于维护和扩展

## 🧪 测试和验证

### 运行演示脚本

```bash
# 运行多语言功能演示
python demo_i18n.py
```

### 运行测试

```bash
# 运行国际化测试
pytest tests/test_i18n.py -v
```

### 手动测试

```bash
# 测试不同语言的帮助信息
depx --lang en --help
depx --lang zh --help

# 测试命令的多语言输出
depx --lang zh scan --help
depx --lang en analyze --help
```

## 📈 改进效果

### 用户体验提升

- **本地化体验**: 中文用户可以使用母语界面
- **详细帮助**: 更丰富的帮助信息和使用示例
- **准确信息**: 实时显示支持的编程语言和功能

### 国际化程度

- **完整翻译**: 所有用户界面文本都支持多语言
- **智能检测**: 自动适应用户的语言环境
- **灵活切换**: 支持运行时语言切换

### 开发者友好

- **易于扩展**: 简单的 YAML 文件格式
- **类型安全**: 完整的类型注解和错误处理
- **测试覆盖**: 全面的测试用例

## 🔮 未来计划

1. **更多语言支持**: 日语、韩语、法语等
2. **动态翻译**: 支持在线翻译服务
3. **本地化配置**: 日期、数字格式的本地化
4. **用户偏好**: 记住用户的语言选择

---

这次更新让 Depx 成为了一个真正国际化的工具，为不同语言背景的用户提供了更好的使用体验！
