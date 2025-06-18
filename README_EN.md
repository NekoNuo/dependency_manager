# Depx - Universal Multi-Language Dependency Manager

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](https://github.com/NekoNuo/depx)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/NekoNuo/depx)

🚀 **Depx** is a powerful cross-platform dependency management tool that provides unified discovery, transparent information, space optimization, and cross-platform support for multiple programming languages.

## ✨ Key Features

- 🌍 **Multi-Language Support**: Node.js, Python, Rust, Java, Go, PHP, C#
- 🔍 **Universal Search**: Search packages across all package managers simultaneously
- 🧠 **Smart Detection**: Automatically detect project types and preferred package managers
- 💻 **Cross-Platform**: Windows, macOS, Linux with native support
- 🎯 **Interactive Interface**: User-friendly menu-driven interface
- 🌐 **Multilingual UI**: English and Chinese interface support
- ⚡ **Fast Performance**: Optimized scanning and analysis algorithms

## 🚀 Quick Start

### One-Click Installation

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/NekoNuo/depx/main/install_and_run.ps1 | iex
```

**macOS/Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/quick_install.sh | bash
```

### Manual Installation

```bash
# Install from PyPI
pip install depx --user

# Verify installation
python -m depx --version
```

## 📋 Usage Examples

### Basic Commands

```bash
# Analyze current directory
python -m depx info .

# Search packages (all package managers)
python -m depx search react

# Scan for projects
python -m depx scan

# Install packages
python -m depx install express

# Update packages
python -m depx update --check

# Clean dependencies
python -m depx clean .
```

### Interactive Mode

```bash
# Launch interactive interface
python interactive_depx.py

# Windows optimized interface
powershell -File windows_interactive.ps1
```

## 🛠️ Supported Package Managers

| Language | Package Managers | Status |
|----------|------------------|--------|
| **Node.js** | npm, yarn, pnpm | ✅ Full Support |
| **Python** | pip, conda | ✅ Full Support |
| **Rust** | cargo | ✅ Full Support |
| **Java** | maven, gradle | ✅ Full Support |
| **Go** | go modules | ✅ Full Support |
| **PHP** | composer | ✅ Full Support |
| **C#** | nuget, dotnet | ✅ Full Support |

## 🔧 Configuration

Depx supports flexible configuration through YAML files:

```yaml
# .depx.yaml
scan:
  max_depth: 5
  parallel: true
  project_types: ["nodejs", "python", "rust"]

cleanup:
  auto_confirm: false
  backup_enabled: true

log_level: "INFO"
cache_enabled: true
```

## 📊 Features Overview

### Project Analysis
- **Dependency Discovery**: Automatically find and analyze dependencies
- **Size Calculation**: Calculate disk space usage for each dependency
- **Outdated Detection**: Identify packages that need updates
- **Security Scanning**: Check for known vulnerabilities

### Package Search
- **Universal Search**: Search across npm, PyPI, crates.io, Maven Central, etc.
- **Smart Filtering**: Filter results by language, popularity, or maintenance status
- **Detailed Information**: Get comprehensive package information

### Dependency Management
- **Bulk Operations**: Install, update, or remove multiple packages
- **Version Management**: Handle version conflicts and constraints
- **Environment Isolation**: Respect virtual environments and project boundaries

## 🌐 Internationalization

Depx automatically detects your system language and provides localized interfaces:

- **English**: Full feature support
- **中文**: 完整功能支持
- **Auto-Detection**: Intelligent language switching

## 🔍 Troubleshooting

### Common Issues

1. **Installation Problems**
   ```bash
   # Use alternative installation method
   curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/quick_install.sh | bash
   ```

2. **Permission Issues**
   ```bash
   # Install to user directory
   pip install depx --user
   ```

3. **Windows Encoding Issues**
   ```powershell
   # Use Windows optimized script
   powershell -File windows_interactive.ps1
   ```

### Getting Help

- 📖 **Documentation**: [GitHub Wiki](https://github.com/NekoNuo/depx/wiki)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/NekoNuo/depx/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/NekoNuo/depx/discussions)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone repository
git clone https://github.com/NekoNuo/depx.git
cd depx

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Run development version
python -m depx --help
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors and users
- Inspired by various package management tools
- Built with ❤️ for the developer community

---

**Made with ❤️ by the Depx Team**

[🏠 Homepage](https://github.com/NekoNuo/depx) | [📖 Documentation](https://github.com/NekoNuo/depx/wiki) | [🐛 Issues](https://github.com/NekoNuo/depx/issues)
