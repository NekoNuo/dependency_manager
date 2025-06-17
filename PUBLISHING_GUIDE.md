# Depx 发布指南

## 🚀 发布方式总览

Depx 提供了多种发布方式，满足不同的使用场景：

### 1. 📋 TestPyPI 发布（测试）

**用途**：测试包的构建和发布流程，不影响正式版本

**触发方式：**
- 推送任何 `v*` 标签
- 手动触发工作流

**结果**：
- 运行完整测试
- 构建包
- 发布到 TestPyPI
- **不会发布到正式 PyPI**

### 2. 🎯 PyPI 发布（正式）

**用途**：正式发布新版本供用户安装

**触发方式：**
- 在 GitHub 上创建 Release
- 手动触发工作流并选择发布到 PyPI

**结果**：
- 运行完整测试
- 构建包
- 发布到 TestPyPI（测试）
- **发布到正式 PyPI**

## 📋 具体操作步骤

### 方式 1: 测试发布（推荐先做）

```bash
# 1. 确保代码已提交
git add .
git commit -m "Prepare for v0.4.0 release"
git push origin main

# 2. 创建并推送标签
git tag v0.4.0
git push origin v0.4.0

# 3. 查看 GitHub Actions 运行状态
# 访问: https://github.com/yourusername/depx/actions
```

**预期结果：**
- ✅ 测试通过
- ✅ 包构建成功
- ✅ 发布到 TestPyPI
- ❌ 不会发布到 PyPI（这是预期的）

**测试安装：**
```bash
pip install --index-url https://test.pypi.org/simple/ depx
```

### 方式 2: 正式发布（GitHub Release）

```bash
# 1. 在 GitHub 网站上操作
# 访问: https://github.com/yourusername/depx/releases

# 2. 点击 "Create a new release"

# 3. 填写信息：
# - Tag: v0.4.0 (选择已存在的标签)
# - Title: Depx v0.4.0
# - Description: 复制 RELEASE_NOTES.md 的内容

# 4. 点击 "Publish release"
```

**预期结果：**
- ✅ 测试通过
- ✅ 包构建成功
- ✅ 发布到 TestPyPI
- ✅ **发布到正式 PyPI**

**用户安装：**
```bash
pip install depx
```

### 方式 3: 手动发布（高级用户）

```bash
# 1. 访问 GitHub Actions 页面
# https://github.com/yourusername/depx/actions

# 2. 点击 "Build and Publish to PyPI" 工作流

# 3. 点击 "Run workflow"

# 4. 选择选项：
# - Branch: main
# - Publish to PyPI: true (如果要发布到正式 PyPI)

# 5. 点击 "Run workflow"
```

## 🔧 配置要求

### GitHub Secrets

在 GitHub 仓库设置中配置以下 Secrets：

```
Settings → Secrets and variables → Actions → New repository secret
```

**必需的 Secrets：**
- `PYPI_API_TOKEN`: PyPI API Token
- `TEST_PYPI_API_TOKEN`: TestPyPI API Token

### 获取 API Tokens

**PyPI Token：**
1. 访问 https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. 选择 "Entire account" 或特定项目
4. 复制生成的 token

**TestPyPI Token：**
1. 访问 https://test.pypi.org/manage/account/token/
2. 重复上述步骤

## 📊 发布流程图

```
推送标签 v0.4.0
    ↓
运行测试 (多版本/多平台)
    ↓
构建包 (wheel + sdist)
    ↓
发布到 TestPyPI ✅
    ↓
检查是否为 Release? 
    ↓ (是)          ↓ (否)
发布到 PyPI ✅    结束 ⏹️
```

## 🔍 故障排除

### 常见问题

**1. API Token 错误**
```
Error: Invalid or non-existent authentication information.
```
**解决方案：**
- 检查 GitHub Secrets 配置
- 确认 Token 有效且权限正确

**2. 版本冲突**
```
Error: File already exists.
```
**解决方案：**
- 更新版本号（pyproject.toml, setup.py, __init__.py）
- 确保版本号唯一

**3. 测试失败**
```
Error: Tests failed
```
**解决方案：**
- 本地运行测试：`pytest tests/ -v`
- 修复失败的测试
- 重新推送代码

### 查看发布状态

**GitHub Actions：**
- 访问：`https://github.com/yourusername/depx/actions`
- 查看工作流运行状态和日志

**PyPI 页面：**
- TestPyPI：`https://test.pypi.org/project/depx/`
- PyPI：`https://pypi.org/project/depx/`

## 🎯 最佳实践

### 发布前检查清单

- [ ] 所有测试通过
- [ ] 版本号已更新
- [ ] CHANGELOG.md 已更新
- [ ] README.md 已更新
- [ ] 代码已格式化（black）
- [ ] 先发布到 TestPyPI 测试

### 版本号规范

使用语义化版本：
- `v0.4.0` - 主要版本
- `v0.4.1` - 补丁版本
- `v0.5.0` - 次要版本

### 发布节奏

建议的发布流程：
1. **开发** → 功能分支
2. **测试** → 合并到 main
3. **预发布** → 推送标签到 TestPyPI
4. **正式发布** → 创建 GitHub Release

现在你可以根据需要选择合适的发布方式！🚀
