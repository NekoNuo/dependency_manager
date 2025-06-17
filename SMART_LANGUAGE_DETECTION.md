# Depx 智能语言检测功能

## 🧠 智能检测概览

Depx 现在具备了完全智能的语言检测功能，能够根据用户的系统环境自动选择最合适的界面语言，无需手动指定。

## 🔍 检测机制

### 检测优先级（从高到低）

1. **DEPX_LANG 环境变量** - 用户明确指定的语言偏好
2. **LANG 环境变量** - 系统主要语言设置
3. **LC_ALL 环境变量** - 系统全局语言设置
4. **系统默认 locale** - 操作系统默认语言
5. **终端语言设置** - 终端应用的语言配置
6. **回退到英文** - 如果所有检测都失败

### 支持的语言标识

#### 中文检测
- `zh`, `zh_CN`, `zh_TW`, `zh_HK`, `zh_SG`
- `zh-cn`, `zh-tw`, `zh-hk`, `zh-sg`
- `chinese`, `china`, `taiwan`, `hongkong`

#### 英文检测
- `en`, `en_US`, `en_GB`, `en_CA`, `en_AU`
- `en-us`, `en-gb`, `en-ca`, `en-au`
- `english`, `american`, `british`

## 🚀 使用方式

### 1. 完全自动（推荐）
```bash
# 系统会自动检测语言环境
depx scan
depx analyze
depx info .
```

### 2. 环境变量设置
```bash
# 设置默认中文
export DEPX_LANG=zh
depx scan  # 自动使用中文界面

# 设置默认英文
export DEPX_LANG=en
depx scan  # 自动使用英文界面
```

### 3. 临时指定语言
```bash
# 临时使用中文
depx --lang zh scan

# 临时使用英文
depx --lang en scan
```

### 4. 查看检测信息
```bash
# 查看详细的语言检测信息
depx config --lang-info
```

## 📊 检测效果演示

### 中文系统环境
```bash
$ depx config --lang-info

🌍 Language Detection Information
   Environment Variables   
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Variable  ┃ Value       ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ DEPX_LANG │ 未设置      │
│ LANG      │ zh_CN.UTF-8 │
│ LC_ALL    │ 未设置      │
└───────────┴─────────────┘

         System Information          
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Item              ┃ Value         ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ System Locale     │ zh_CN / UTF-8 │
│ Detected Language │ zh            │
│ Current Language  │ zh            │
└───────────────────┴───────────────┘

# 自动使用中文界面
$ depx scan
🔍 扫描目录：/path/to/project
📏 扫描深度：5
⚡ 并行处理：已启用
✅ 发现 1 个项目
```

### 英文系统环境
```bash
$ LANG=en_US.UTF-8 depx config --lang-info

🌍 Language Detection Information
   Environment Variables   
┏━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Variable  ┃ Value       ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ DEPX_LANG │ 未设置      │
│ LANG      │ en_US.UTF-8 │
│ LC_ALL    │ 未设置      │
└───────────┴─────────────┘

         System Information          
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Item              ┃ Value         ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ System Locale     │ en_US / UTF-8 │
│ Detected Language │ en            │
│ Current Language  │ en            │
└───────────────────┴───────────────┘

# 自动使用英文界面
$ depx scan
🔍 Scanning directory: /path/to/project
📏 Scan depth: 5
⚡ Parallel processing: Enabled
✅ Found 1 projects
```

## 🔧 技术实现

### 核心检测算法
```python
def auto_detect_language(self) -> str:
    """智能检测系统语言"""
    detection_methods = [
        self._detect_from_depx_env,      # DEPX_LANG 环境变量
        self._detect_from_lang_env,      # LANG 环境变量
        self._detect_from_lc_env,        # LC_ALL 环境变量
        self._detect_from_system_locale, # 系统默认 locale
        self._detect_from_terminal,      # 终端语言设置
    ]
    
    for method in detection_methods:
        detected_lang = method()
        if detected_lang and detected_lang in self._translations:
            return detected_lang
    
    return self._fallback_language  # 回退到英文
```

### Locale 解析器
```python
def _parse_locale_string(self, locale_str: str) -> Optional[str]:
    """解析 locale 字符串，提取语言代码"""
    # 支持格式：zh_CN.UTF-8, en_US.UTF-8, zh-CN, en-US 等
    # 智能识别中文和英文的各种变体
```

## 🎯 智能特性

### 1. 多格式支持
- ✅ 标准 locale 格式：`zh_CN.UTF-8`, `en_US.UTF-8`
- ✅ 简化格式：`zh-CN`, `en-US`
- ✅ 基础格式：`zh`, `en`
- ✅ 描述性格式：`chinese`, `english`

### 2. 地区变体识别
- ✅ 中文：大陆、台湾、香港、新加坡
- ✅ 英文：美国、英国、加拿大、澳大利亚

### 3. 错误处理
- ✅ 检测失败时优雅回退
- ✅ 不支持的语言自动使用英文
- ✅ 详细的调试日志

### 4. 性能优化
- ✅ 缓存检测结果
- ✅ 快速检测算法
- ✅ 最小化系统调用

## 📈 用户体验提升

### 之前（手动指定）
```bash
# 用户需要记住并手动指定语言
depx --lang zh scan    # 中文用户
depx --lang en scan    # 英文用户
```

### 现在（智能检测）
```bash
# 用户只需要正常使用，系统自动适配
depx scan              # 自动检测并使用合适的语言
```

## 🔍 调试和故障排除

### 查看检测详情
```bash
depx config --lang-info
```

### 强制指定语言
```bash
# 如果自动检测不准确，可以强制指定
export DEPX_LANG=zh
depx scan
```

### 调试日志
```bash
# 启用详细日志查看检测过程
depx --verbose scan
```

## 🌟 优势总结

1. **零配置使用** - 开箱即用，无需设置
2. **智能适配** - 自动适应用户的语言环境
3. **灵活覆盖** - 支持手动指定和环境变量
4. **健壮性强** - 多重检测机制，确保可靠性
5. **调试友好** - 提供详细的检测信息
6. **性能优秀** - 快速检测，不影响启动速度

## 🎉 总结

智能语言检测功能让 Depx 真正成为了一个"智能"的国际化工具：

- **中文用户**：无需任何设置，自动使用中文界面
- **英文用户**：无需任何设置，自动使用英文界面
- **高级用户**：可以通过环境变量或命令行参数精确控制

这个功能大大提升了用户体验，让 Depx 能够无缝适应不同语言环境的用户需求！🚀
