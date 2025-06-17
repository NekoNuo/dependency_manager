# GitHub Actions 使用指南

## 🔧 已修复的问题

### ✅ 更新了过时的 Actions

我们已经将所有 GitHub Actions 更新到最新版本：

- `actions/upload-artifact@v3` → `actions/upload-artifact@v4`
- `actions/download-artifact@v3` → `actions/download-artifact@v4`
- `actions/setup-python@v4` → `actions/setup-python@v5`
- `codecov/codecov-action@v3` → `codecov/codecov-action@v4`

## 📋 工作流概览

### 1. CI 工作流 (`.github/workflows/ci.yml`)

**触发条件：**
- 推送到 `main`, `master`, `develop` 分支
- 创建 Pull Request

**功能：**
- 多版本测试 (Python 3.8-3.12)
- 多平台测试 (Ubuntu, Windows, macOS)
- 代码质量检查 (flake8, black, isort)
- 安全扫描 (bandit, safety)
- 测试覆盖率报告

### 2. 发布工作流 (`.github/workflows/publish.yml`)

**触发条件：**
- 推送标签 (`v*`)
- 创建 GitHub Release
- 手动触发

**功能：**
- 完整测试套件
- 包构建和验证
- TestPyPI 发布 (测试)
- PyPI 发布 (正式)

## 🚀 使用方法

### 配置 Secrets

在 GitHub 仓库设置中添加：

```
PYPI_API_TOKEN: 你的 PyPI API Token
TEST_PYPI_API_TOKEN: 你的 TestPyPI API Token
```

### 发布流程

#### 1. 测试发布 (TestPyPI)

```bash
# 方法 1: 推送标签
git tag v0.4.0
git push origin v0.4.0

# 方法 2: 手动触发
# 在 GitHub Actions 页面手动运行工作流
```

#### 2. 正式发布 (PyPI)

```bash
# 在 GitHub 上创建 Release
# 1. 去 Releases 页面
# 2. 点击 "Create a new release"
# 3. 选择标签: v0.4.0
# 4. 填写发布说明
# 5. 点击 "Publish release"
```

## 📊 工作流状态

### 查看运行状态

1. 在 GitHub 仓库页面点击 `Actions`
2. 查看工作流运行状态
3. 点击具体运行查看详细日志

### 状态徽章

可以在 README.md 中添加：

```markdown
![CI](https://github.com/yourusername/depx/workflows/CI/badge.svg)
![Publish](https://github.com/yourusername/depx/workflows/Build%20and%20Publish%20to%20PyPI/badge.svg)
```

## 🔍 故障排除

### 常见问题

1. **API Token 错误**
   - 检查 Secrets 配置
   - 确认 Token 有效性

2. **版本冲突**
   - 确保版本号唯一
   - 检查 PyPI 上是否已存在该版本

3. **测试失败**
   - 查看测试日志
   - 本地运行测试确认

4. **构建失败**
   - 检查 `pyproject.toml` 配置
   - 确认所有文件包含正确

### 重新运行工作流

如果工作流失败，可以：
1. 在 Actions 页面点击失败的工作流
2. 点击 "Re-run jobs" 重新运行
3. 或者 "Re-run failed jobs" 只重新运行失败的任务

## 📝 工作流详解

### CI 工作流特点

```yaml
# 测试矩阵
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']

# 并行执行多个任务
jobs:
  test:    # 运行测试
  lint:    # 代码质量检查
  security: # 安全扫描
```

### 发布工作流特点

```yaml
# 顺序执行的任务
jobs:
  test:         # 1. 测试
  build:        # 2. 构建 (依赖 test)
  publish-test: # 3. TestPyPI 发布 (依赖 build)
  publish-pypi: # 4. PyPI 发布 (依赖 build + publish-test)

# 条件发布
if: github.event_name == 'release' && github.event.action == 'published'
```

## 🎯 最佳实践

### 开发流程

1. **功能开发**
   ```bash
   git checkout -b feature/new-feature
   # 开发代码...
   git push origin feature/new-feature
   ```

2. **创建 PR**
   - 自动触发 CI 测试
   - 确保所有检查通过

3. **合并到主分支**
   ```bash
   git checkout main
   git merge feature/new-feature
   git push origin main
   ```

4. **准备发布**
   ```bash
   # 更新版本号
   # 更新 CHANGELOG.md
   git commit -m "Bump version to 0.4.1"
   git push origin main
   ```

5. **测试发布**
   ```bash
   git tag v0.4.1
   git push origin v0.4.1
   ```

6. **正式发布**
   - 在 GitHub 创建 Release

### 版本管理

- 使用语义化版本 (Semantic Versioning)
- 标签格式: `v0.4.0`
- 同步更新所有版本号文件

## 🔒 安全考虑

- API Tokens 存储在 GitHub Secrets 中
- 使用 `environment` 保护生产发布
- 自动安全扫描检查依赖漏洞

现在你的 GitHub Actions 工作流已经完全更新并准备就绪！🚀
