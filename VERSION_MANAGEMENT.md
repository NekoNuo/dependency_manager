# Depx 版本管理指南

## 🎯 简化版本更新

现在只需要一个命令就能更新所有文件的版本号！

### 快速更新版本号

```bash
# 更新到新版本（推荐）
python update_version.py 0.8.5

# 这个命令会自动：
# 1. 更新 version.py 中的版本号
# 2. 更新所有相关文件的版本号
# 3. 验证更新结果
```

## 📋 版本管理工具

### 基本命令

```bash
# 检查当前版本
python version.py version

# 检查版本号一致性
python version.py check

# 手动更新所有文件（如果 version.py 已修改）
python version.py update
```

## 📁 版本号管理的文件

以下文件的版本号会自动同步更新：

1. **`pyproject.toml`** - Python 项目配置
2. **`depx/__init__.py`** - Python 模块版本（动态读取）
3. **`depx/cli.py`** - CLI 版本显示（动态读取）
4. **`install_and_run.sh`** - Linux/macOS 脚本横幅
5. **`install_and_run.ps1`** - Windows 脚本横幅
6. **`interactive_depx.py`** - 交互界面横幅

## 🔧 工作原理

### 1. 统一版本源
- **`version.py`** 是唯一的版本号定义文件
- 所有其他文件都从这里读取或通过工具同步

### 2. 自动同步机制
- **Python 模块**: 运行时动态读取版本号（无需更新文件）
- **CLI 命令**: 运行时动态读取版本号（无需更新文件）
- **配置文件**: 通过正则表达式自动替换
- **脚本文件**: 通过模式匹配自动更新

### 3. 一致性检查
- 自动检测版本号不一致的文件
- 提供详细的差异报告
- 支持批量修复

## 📝 使用示例

### 场景1: 发布新版本

```bash
# 1. 更新版本号
python update_version.py 1.0.0

# 2. 验证更新
python version.py check

# 3. 提交更改
git add .
git commit -m "chore: 更新版本号到 1.0.0"

# 4. 创建标签
git tag v1.0.0
git push origin v1.0.0
```

### 场景2: 检查版本一致性

```bash
# 检查所有文件版本号是否一致
python version.py check

# 如果发现不一致，自动修复
python version.py update
```

### 场景3: 查看当前版本

```bash
# 方法1: 使用版本工具
python version.py version

# 方法2: 使用 Python 模块
python -c "import depx; print(depx.__version__)"

# 方法3: 使用 CLI
python run_depx.py --version
```

## 🛠️ 高级用法

### 手动修改版本号

如果需要手动修改版本号：

1. **编辑 `version.py`**:
   ```python
   VERSION = "0.9.0"  # 修改这里
   ```

2. **运行同步工具**:
   ```bash
   python version.py update
   ```

### 添加新的版本文件

如果需要在新文件中包含版本号：

1. **编辑 `version.py`** 的 `VERSION_FILES` 字典
2. **添加文件配置**:
   ```python
   VERSION_FILES = {
       # ... 现有配置 ...
       "new_file.py": {
           "pattern": r'VERSION = "[^"]*"',
           "replacement": f'VERSION = "{VERSION}"'
       }
   }
   ```

## 🔍 故障排除

### 常见问题

**Q: 版本号更新失败怎么办？**
A: 检查文件权限和路径，确保在项目根目录运行

**Q: 某个文件版本号没有更新？**
A: 检查 `version.py` 中的正则表达式是否正确匹配

**Q: 如何回滚版本号？**
A: 使用 `python update_version.py <旧版本号>` 回滚

### 调试方法

```bash
# 详细检查版本一致性
python version.py check

# 查看具体的匹配模式
python -c "from version import VERSION_FILES; print(VERSION_FILES)"
```

## 📊 版本号规范

### 语义化版本

遵循 [Semantic Versioning](https://semver.org/) 规范：

- **主版本号**: 不兼容的 API 修改
- **次版本号**: 向下兼容的功能性新增
- **修订号**: 向下兼容的问题修正

### 示例

```
1.0.0 - 首个稳定版本
1.1.0 - 新增功能
1.1.1 - 修复 bug
2.0.0 - 重大更新，可能不兼容
```

## 🎉 优势

### 简化流程
- **一个命令** - 更新所有版本号
- **自动同步** - 无需手动修改多个文件
- **一致性保证** - 自动检查和修复不一致

### 减少错误
- **统一管理** - 避免遗漏某个文件
- **格式验证** - 确保版本号格式正确
- **自动化** - 减少人为错误

### 提高效率
- **快速发布** - 版本更新只需几秒钟
- **易于维护** - 清晰的版本管理流程
- **团队协作** - 标准化的版本更新方式

---

🎯 现在版本管理变得简单了！只需要一个命令就能搞定所有版本号更新！
