# 简化的发布流程指南

## 🚀 新的发布流程

修改后的 GitHub Actions 工作流程现在支持**直接通过标签推送发布到 PyPI**，无需创建 GitHub Release。

## 📋 发布方式

### 方式 1：标签推送（推荐）⭐
```bash
# 1. 更新版本号（在 pyproject.toml 中）
# 2. 提交更改
git add .
git commit -m "Bump version to v0.4.1"

# 3. 创建并推送标签
git tag v0.4.1
git push origin v0.4.1
```

**结果**：
- ✅ 自动运行所有测试（Python 3.8-3.12）
- ✅ 构建包
- ✅ 发布到 TestPyPI
- ✅ **直接发布到 PyPI**（新增！）

### 方式 2：GitHub Release（传统方式）
1. 在 GitHub 网页上创建新的 Release
2. 选择标签或创建新标签
3. 发布 Release

**结果**：与方式 1 相同

### 方式 3：手动触发
1. 在 GitHub Actions 页面点击 "Build and Publish to PyPI"
2. 选择 "Run workflow"
3. 选择是否发布到 PyPI

## 🔄 完整的发布流程

### 自动化流程
```
推送标签 → 运行测试 → 构建包 → TestPyPI → PyPI
    ↓           ↓         ↓        ↓        ↓
  v0.4.1    所有平台    wheel+tar  测试环境  生产环境
           Python版本    格式检查   验证包   正式发布
```

### 触发条件对比

| 触发方式 | TestPyPI | PyPI | 说明 |
|---------|----------|------|------|
| 推送标签 (v*) | ✅ | ✅ | **新增：直接发布** |
| GitHub Release | ✅ | ✅ | 传统方式 |
| 手动触发 | ✅ | 可选 | 灵活控制 |

## 🛡️ 安全性

- 所有发布都需要通过完整的测试套件
- PyPI 发布使用 `environment: pypi` 保护
- 需要正确配置 `PYPI_API_TOKEN` 密钥

## 📝 版本管理建议

1. **开发版本**：`v0.4.1-dev`, `v0.4.1-alpha.1`
2. **预发布版本**：`v0.4.1-rc.1`
3. **正式版本**：`v0.4.1`

## 🚨 注意事项

- 确保 `pyproject.toml` 中的版本号与标签匹配
- 标签必须以 `v` 开头（如 `v0.4.1`）
- PyPI 不允许重复发布相同版本号
- 建议先在 TestPyPI 验证包的正确性

## 🔧 回滚方案

如果需要回滚到只有 Release 才发布的模式：

```yaml
# 在 .github/workflows/publish.yml 中修改
if: |
  (github.event_name == 'release' && github.event.action == 'published') ||
  (github.event_name == 'workflow_dispatch' && github.event.inputs.publish_to_pypi == 'true')
```

## 📊 发布历史追踪

- GitHub Actions 页面查看所有发布记录
- PyPI 页面查看已发布的版本
- TestPyPI 页面查看测试发布
