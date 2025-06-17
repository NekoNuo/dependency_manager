# Depx v0.5.0 发布说明

🎉 **Depx v0.5.0 正式发布！**

这是一个重大版本更新，新增了对 **5 种主流编程语言** 的支持，使 Depx 成为真正的多语言依赖管理工具！

## 🌟 主要新功能

### 🚀 多语言支持大幅扩展

现在 Depx 支持 **7 种编程语言**，覆盖了绝大多数主流开发场景：

#### 🆕 新增语言支持

1. **☕ Java 项目支持**
   - **Maven**: `pom.xml` 解析
   - **Gradle**: `build.gradle`, `build.gradle.kts` 解析
   - 自动检测构建工具和 Java 版本
   - 支持依赖范围识别（compile, test, provided）

2. **🐹 Go 项目支持**
   - **Go Modules**: `go.mod`, `go.sum` 解析
   - **Legacy**: `Gopkg.toml`, `vendor.json` 支持
   - 自动检测 Go 版本和模块路径
   - 支持间接依赖标识

3. **🦀 Rust 项目支持**
   - **Cargo**: `Cargo.toml`, `Cargo.lock` 解析
   - 支持依赖类型（dependencies, dev-dependencies, build-dependencies）
   - 自动检测 Rust 版本和 edition
   - Workspace 项目支持

4. **🐘 PHP 项目支持**
   - **Composer**: `composer.json`, `composer.lock` 解析
   - 自动检测 PHP 版本和框架（Laravel, Symfony 等）
   - 支持生产和开发依赖区分
   - Vendor 目录大小计算

5. **⚡ C# 项目支持**
   - **现代 .NET**: `.csproj` PackageReference 解析
   - **传统 .NET**: `packages.config` 支持
   - **Legacy .NET Core**: `project.json` 支持
   - 自动检测 .NET 版本和框架类型

#### ✅ 现有语言（已优化）
- **Node.js**: package.json, npm/yarn/pnpm
- **Python**: requirements.txt, pyproject.toml, Pipfile

## 📊 功能对比

| 语言 | 配置文件 | 包管理器 | 依赖类型 | 版本检测 | 缓存支持 |
|------|----------|----------|----------|----------|----------|
| Node.js | ✅ | ✅ | ✅ | ✅ | ✅ |
| Python | ✅ | ✅ | ✅ | ✅ | ✅ |
| Java | ✅ | ✅ | ✅ | ✅ | ✅ |
| Go | ✅ | ✅ | ✅ | ✅ | ✅ |
| Rust | ✅ | ✅ | ✅ | ✅ | ✅ |
| PHP | ✅ | ✅ | ✅ | ✅ | ✅ |
| C# | ✅ | ✅ | ✅ | ✅ | ✅ |

## 🛠️ 使用示例

### 扫描多语言项目

```bash
# 扫描包含多种语言的项目目录
depx scan ~/projects

# 输出示例：
# ✅ Found 12 projects
# 📦 Node.js Projects: 4
# 🐍 Python Projects: 3
# ☕ Java Projects: 2
# 🐹 Go Projects: 2
# 🦀 Rust Projects: 1
```

### 查看特定语言项目

```bash
# 查看 Java 项目详情
depx info ~/projects/my-spring-app

# 查看 Go 项目详情  
depx info ~/projects/my-go-service

# 查看 Rust 项目详情
depx info ~/projects/my-rust-cli
```

### 分析多语言依赖

```bash
# 分析所有项目的依赖情况
depx analyze ~/projects

# 按项目类型分组显示
# 支持跨语言重复依赖检测
# 提供多语言清理建议
```

## 🔧 技术改进

### 🏗️ 架构优化
- **模块化解析器设计**：每种语言独立解析器
- **统一接口标准**：所有解析器遵循相同接口
- **可扩展架构**：轻松添加新语言支持

### 📈 性能提升
- **并行解析**：多项目并行处理
- **智能缓存**：避免重复解析
- **内存优化**：大型项目支持

### 🧪 测试覆盖
- **15+ 测试用例**：覆盖所有核心功能
- **多语言测试项目**：真实项目结构测试
- **CI/CD 验证**：Python 3.8-3.12 全版本测试

## 📋 完整功能列表

### 🔍 项目扫描
- 自动识别 7 种语言项目
- 递归目录扫描
- 智能项目类型检测

### 📦 依赖解析
- 配置文件解析
- 依赖类型识别
- 版本信息提取
- 锁定文件支持

### 💾 大小计算
- 依赖磁盘占用
- 缓存目录扫描
- 构建产物统计

### 🧹 清理功能
- 开发依赖清理
- 缓存文件清理
- 大型依赖识别

### 📊 分析报告
- 重复依赖检测
- 依赖统计分析
- 清理建议生成

### 📤 导出功能
- JSON/CSV/HTML 格式
- 项目信息导出
- 依赖报告导出

## 🚀 升级指南

### 从 v0.4.x 升级

```bash
# 升级到最新版本
pip install --upgrade depx

# 验证新语言支持
depx --version  # 应显示 v0.5.0
depx scan --help  # 查看新功能
```

### 新功能体验

```bash
# 扫描多语言项目
depx scan ~/projects

# 查看支持的项目类型
depx scan ~/projects | grep "Projects:"

# 测试新语言解析
depx info ~/my-java-project
depx info ~/my-go-project
depx info ~/my-rust-project
```

## 🔮 下一步计划

### v0.6.0 规划
- **Ruby** 支持 (Gemfile)
- **Swift** 支持 (Package.swift)
- **Dart** 支持 (pubspec.yaml)
- **依赖安全扫描**
- **依赖更新检查**

## 🙏 致谢

感谢所有用户的反馈和建议，让 Depx 能够不断改进和完善！

---

**下载地址**: [PyPI](https://pypi.org/project/depx/)  
**源代码**: [GitHub](https://github.com/yourusername/depx)  
**文档**: [README](https://github.com/yourusername/depx#readme)
