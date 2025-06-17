# Depx v0.4.0 新功能指南

## 🎉 新增功能概览

Depx v0.4.0 大幅扩展了功能，从一个简单的依赖分析工具升级为完整的多语言依赖管理解决方案！

### 🆕 主要新功能

1. **🐍 Python 项目支持** - 完整的 Python 生态支持
2. **🧹 依赖清理功能** - 安全清理不需要的依赖和缓存
3. **📊 导出功能** - 多格式导出分析结果
4. **⚙️ 配置文件支持** - 灵活的 YAML 配置

---

## 🐍 Python 项目支持

### 支持的配置文件

- `requirements.txt` - 标准依赖文件
- `pyproject.toml` - 现代 Python 项目配置
- `setup.py` - 传统 Python 包配置
- `Pipfile` - Pipenv 配置文件
- `environment.yml` - Conda 环境文件

### 支持的包管理器

- **pip** - 标准 Python 包管理器
- **pipenv** - 虚拟环境和依赖管理
- **poetry** - 现代 Python 依赖管理
- **conda** - 科学计算包管理器

### 使用示例

```bash
# 扫描 Python 项目
depx scan . --type python

# 查看 Python 项目详情
depx info /path/to/python/project

# 分析 Python 项目依赖
depx analyze . --type python
```

### 检测功能

- **虚拟环境检测** - 自动识别 venv, .venv, env 等
- **Python 版本检测** - 从 .python-version, runtime.txt 读取
- **包管理器识别** - 自动识别使用的包管理器
- **依赖类型分类** - 区分生产、开发、可选依赖

---

## 🧹 依赖清理功能

### 清理类型

- **`dev`** - 开发依赖（测试、构建工具等）
- **`cache`** - 包管理器缓存
- **`unused`** - 未使用的依赖（基于启发式分析）
- **`large`** - 大型依赖（默认 >50MB）

### 使用示例

```bash
# 查看清理计划（干运行）
depx clean . --type dev cache --dry-run

# 实际执行清理
depx clean . --type dev --no-dry-run

# 清理特定类型
depx clean . --type cache large --no-dry-run

# 跳过确认直接清理
depx clean . --type dev --no-dry-run --no-confirm
```

### 安全特性

- **默认干运行** - 先显示清理计划，确认后执行
- **确认机制** - 执行前需要用户确认
- **详细日志** - 记录所有清理操作
- **错误处理** - 清理失败时继续处理其他项目

### 清理效果

```
📋 Cleanup Plan
💾 Total space to free: 2.3 GB

Project Dependencies to Clean
┏━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Project ┃ Dependency ┃ Type           ┃ Size    ┃
┡━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ webapp  │ jest       │ dev_dependency │ 45.2 MB │
│ api     │ nodemon    │ dev_dependency │ 12.8 MB │
└─────────┴────────────┴────────────────┴─────────┘

Global Caches to Clean
┏━━━━━━━━━━┳━━━━━━━━━┓
┃ Cache    ┃ Size    ┃
┡━━━━━━━━━━╇━━━━━━━━━┩
│ npm cache│ 1.8 GB  │
│ pip cache│ 512 MB  │
└──────────┴─────────┘
```

---

## 📊 导出功能

### 支持格式

- **JSON** - 结构化数据，便于程序处理
- **CSV** - 表格数据，便于 Excel 分析
- **HTML** - 可视化报告，便于查看和分享

### 导出类型

- **`projects`** - 项目列表和基本信息
- **`dependencies`** - 全局依赖详情
- **`report`** - 完整分析报告

### 使用示例

```bash
# 导出项目信息为 JSON
depx export . --format json --type projects

# 导出全局依赖为 CSV
depx export . --format csv --type dependencies

# 导出完整报告为 HTML
depx export . --format html --type report --output report.html
```

### 导出内容

**JSON 格式示例：**
```json
{
  "export_info": {
    "timestamp": "2025-06-17T11:17:12.447396",
    "format": "json",
    "type": "projects",
    "count": 3
  },
  "projects": [
    {
      "name": "webapp",
      "project_type": "nodejs",
      "dependencies": [...],
      "total_size_bytes": 245760000,
      "metadata": {...}
    }
  ]
}
```

**HTML 报告特性：**
- 响应式设计，支持移动端
- 交互式表格
- 汇总统计信息
- 美观的可视化界面

---

## ⚙️ 配置文件支持

### 配置文件格式

支持 YAML 格式配置文件：
- `.depx.yaml` / `.depx.yml`
- `depx.yaml` / `depx.yml`
- `pyproject.toml` 中的 `[tool.depx]` 部分

### 配置选项

```yaml
# 扫描配置
scan:
  max_depth: 5
  parallel: true
  include_patterns: []
  exclude_patterns: ["*.tmp", "*.log"]
  project_types: ["nodejs", "python"]
  follow_symlinks: false

# 清理配置
cleanup:
  dry_run: true
  backup_before_clean: true
  cleanup_types: ["dev", "cache"]
  size_threshold_mb: 50
  confirm_before_clean: true

# 导出配置
export:
  default_format: "json"
  output_directory: "./depx-exports"
  include_metadata: true
  compress_output: false

# 全局设置
log_level: "INFO"
cache_enabled: true
cache_directory: "~/.depx/cache"
ignore_directories:
  - ".git"
  - "__pycache__"
  - "node_modules"
  - ".venv"
```

### 配置管理命令

```bash
# 创建默认配置文件
depx config --create

# 创建指定路径的配置文件
depx config --create --path custom-config.yaml

# 显示当前配置
depx config --show

# 使用指定配置文件
depx config --show --path custom-config.yaml
```

### 配置优先级

1. 命令行参数（最高优先级）
2. 当前目录的配置文件
3. 父目录的配置文件（向上搜索）
4. 默认配置（最低优先级）

---

## 🚀 使用场景

### 1. 开发环境清理

```bash
# 清理开发依赖释放空间
depx clean ~/projects --type dev --dry-run
depx clean ~/projects --type dev --no-dry-run
```

### 2. 项目迁移

```bash
# 导出项目信息用于迁移
depx export ~/old-projects --format json --type projects
depx export ~/old-projects --format html --type report
```

### 3. 依赖审计

```bash
# 分析所有项目的依赖情况
depx analyze ~/projects --sort-by size --limit 50
depx export ~/projects --format csv --type dependencies
```

### 4. 团队配置标准化

```bash
# 创建团队标准配置
depx config --create --path .depx.yaml
# 提交到版本控制
git add .depx.yaml
git commit -m "Add Depx configuration"
```

---

## 📈 性能提升

### 多语言支持

- **Node.js** - 原有功能增强
- **Python** - 全新支持
- **扩展性** - 易于添加新语言支持

### 并行处理

- 默认启用并行扫描
- 大幅提升大型项目扫描速度
- 可通过配置文件调整

### 智能缓存

- 扫描结果缓存
- 避免重复计算
- 配置文件控制缓存行为

---

## 🔧 高级用法

### 自定义扫描规则

```yaml
scan:
  include_patterns: 
    - "src/**"
    - "lib/**"
  exclude_patterns:
    - "**/*.test.js"
    - "**/dist/**"
  project_types: ["nodejs"]
```

### 批量操作

```bash
# 批量清理多个项目
find ~/projects -name "package.json" -execdir depx clean . --type dev --no-dry-run \;

# 批量导出项目信息
for dir in ~/projects/*/; do
  depx export "$dir" --format json --output "${dir}/depx-report.json"
done
```

### 集成到 CI/CD

```yaml
# GitHub Actions 示例
- name: Analyze Dependencies
  run: |
    depx analyze . --format json --output dependency-report.json
    depx clean . --type dev cache --dry-run
```

---

## 🎯 下一步计划

- **更多语言支持** - Java, Go, Rust, PHP
- **依赖安全扫描** - 检查已知漏洞
- **依赖更新检查** - 检查过时的依赖
- **可视化界面** - Web 界面支持
- **插件系统** - 自定义扩展支持

现在 Depx 已经是一个功能完整的多语言依赖管理工具！🎉
