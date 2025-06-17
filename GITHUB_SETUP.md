# GitHub 仓库设置指南

## 🔐 GitHub Actions Secrets 配置

为了让 Depx 的自动发布功能正常工作，您需要在 GitHub 仓库中配置以下 Secrets：

### 必需的 Secrets

#### 1. PyPI API Token (可选)
如果您想自动发布到 PyPI，需要配置：

**Secret 名称**: `PYPI_API_TOKEN`
**获取方法**:
1. 访问 [PyPI Account Settings](https://pypi.org/manage/account/)
2. 点击 "Add API token"
3. 设置 Token 名称（如：depx-release）
4. 选择 Scope 为 "Entire account" 或特定项目
5. 复制生成的 token（以 `pypi-` 开头）

**配置步骤**:
1. 在 GitHub 仓库页面，点击 "Settings"
2. 在左侧菜单中点击 "Secrets and variables" → "Actions"
3. 点击 "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Secret: 粘贴您的 PyPI API token
6. 点击 "Add secret"

### 自动提供的 Tokens

#### GitHub Token
GitHub 会自动提供 `GITHUB_TOKEN`，用于：
- 创建 GitHub Releases
- 上传发布文件
- 访问仓库内容

**无需手动配置** - GitHub Actions 会自动提供此 token。

## ⚙️ 仓库权限设置

### Actions 权限
确保 GitHub Actions 有足够的权限：

1. 进入仓库 "Settings"
2. 点击 "Actions" → "General"
3. 在 "Workflow permissions" 部分：
   - 选择 "Read and write permissions"
   - 勾选 "Allow GitHub Actions to create and approve pull requests"

### Pages 设置（可选）
如果您想启用 GitHub Pages 来展示文档：

1. 进入仓库 "Settings"
2. 点击 "Pages"
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "master" 或 "main"
5. Folder 选择 "/ (root)"

## 🚀 发布流程

### 自动发布
当您推送带有版本标签的提交时，会自动触发发布：

```bash
# 创建并推送标签
git tag v0.8.1
git push origin v0.8.1
```

### 手动发布
您也可以在 GitHub 网页上手动触发发布：

1. 进入仓库的 "Actions" 页面
2. 选择 "Release Depx" 或 "Simple Release" workflow
3. 点击 "Run workflow"
4. 选择分支并点击 "Run workflow"

## 📋 发布内容

### GitHub Release 包含：
- ✅ Python wheel 文件 (.whl)
- ✅ 源码包 (.tar.gz)
- ✅ 独立运行包 (depx-standalone.zip)
- ✅ 独立运行包 (depx-standalone.tar.gz)
- ✅ 详细的发布说明
- ✅ 一键运行命令

### PyPI 发布包含：
- ✅ Python wheel 文件
- ✅ 源码包
- ✅ 项目元数据

## 🔍 故障排除

### 常见问题

#### 1. PyPI 发布失败
**错误**: `HTTPError: 400 Bad Request`
**原因**: 版本号已存在或 API token 无效
**解决**: 
- 检查版本号是否已在 PyPI 上存在
- 验证 `PYPI_API_TOKEN` 是否正确配置
- 确保 token 有足够的权限

#### 2. GitHub Release 失败
**错误**: `403 Forbidden`
**原因**: 权限不足
**解决**:
- 检查仓库的 Actions 权限设置
- 确保 workflow 有 `contents: write` 权限

#### 3. Secret 名称错误
**错误**: `Secret names must not start with GITHUB_`
**原因**: 使用了保留的 Secret 名称前缀
**解决**: 
- 不要使用 `GITHUB_` 开头的 Secret 名称
- 使用 `${{ github.token }}` 而不是 `${{ secrets.GITHUB_TOKEN }}`

### 调试步骤

1. **查看 Actions 日志**:
   - 进入仓库的 "Actions" 页面
   - 点击失败的 workflow run
   - 查看详细的错误日志

2. **检查权限设置**:
   - 确认 Actions 权限设置正确
   - 验证 Secrets 配置无误

3. **测试发布**:
   - 先使用 "Simple Release" workflow 测试
   - 成功后再尝试完整的发布流程

## 📞 获取帮助

如果遇到问题：

1. 查看 GitHub Actions 的详细日志
2. 检查本文档的故障排除部分
3. 确认所有配置步骤都已正确完成
4. 在仓库中创建 Issue 描述具体问题

---

🎉 配置完成后，您就可以享受自动化的发布流程了！
