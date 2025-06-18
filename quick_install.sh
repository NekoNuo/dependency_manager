#!/bin/bash
# Depx 快速安装脚本 - 更健壮的版本
# 使用方法: curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/main/quick_install.sh | bash

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 显示横幅
show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                        🚀 Depx v0.8.8                        ║"
    echo "║                   跨语言依赖管理工具                          ║"
    echo "║                     快速安装脚本                             ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# 检查操作系统
check_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        echo -e "${RED}❌ 不支持的操作系统: $OSTYPE${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ 检测到操作系统: $OS${NC}"
}

# 检查 Python
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo -e "${RED}❌ 未找到 Python，请先安装 Python 3.8+${NC}"
        echo -e "${YELLOW}安装方法:${NC}"
        if [[ "$OS" == "macos" ]]; then
            echo "  brew install python3"
            echo "  或从 https://python.org 下载安装"
        else
            echo "  sudo apt-get install python3 python3-pip  # Ubuntu/Debian"
            echo "  sudo yum install python3 python3-pip     # CentOS/RHEL"
        fi
        exit 1
    fi
    
    # 检查 Python 版本
    PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    echo -e "${GREEN}✅ 找到 Python: $PYTHON_CMD (版本 $PYTHON_VERSION)${NC}"
    
    # 简单的版本检查
    VERSION_CHECK=$($PYTHON_CMD -c "import sys; print(1 if sys.version_info >= (3, 8) else 0)")
    if [[ "$VERSION_CHECK" == "0" ]]; then
        echo -e "${RED}❌ Python 版本过低，需要 3.8+，当前版本: $PYTHON_VERSION${NC}"
        exit 1
    fi
}

# 检查 pip
check_pip() {
    if [[ "$PYTHON_CMD" == "python3" ]]; then
        if command -v pip3 &> /dev/null; then
            PIP_CMD="pip3"
        elif $PYTHON_CMD -m pip --version &> /dev/null; then
            PIP_CMD="$PYTHON_CMD -m pip"
        else
            echo -e "${RED}❌ 未找到 pip3，请先安装 pip${NC}"
            exit 1
        fi
    else
        if command -v pip &> /dev/null; then
            PIP_CMD="pip"
        elif $PYTHON_CMD -m pip --version &> /dev/null; then
            PIP_CMD="$PYTHON_CMD -m pip"
        else
            echo -e "${RED}❌ 未找到 pip，请先安装 pip${NC}"
            exit 1
        fi
    fi
    echo -e "${GREEN}✅ 找到 pip: $PIP_CMD${NC}"
}

# 安装 Depx
install_depx() {
    echo -e "${BLUE}📦 正在安装 Depx...${NC}"
    
    # 尝试从 PyPI 安装
    if $PIP_CMD install depx --user --upgrade; then
        echo -e "${GREEN}✅ Depx 安装成功！${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠️  PyPI 安装失败，尝试从源码安装...${NC}"
        return 1
    fi
}

# 从源码安装
install_from_source() {
    echo -e "${BLUE}📥 从源码安装 Depx...${NC}"
    
    # 创建临时目录
    TEMP_DIR=$(mktemp -d)
    echo -e "${BLUE}📁 创建临时目录: $TEMP_DIR${NC}"
    cd "$TEMP_DIR"
    
    # 安装依赖
    echo -e "${BLUE}📦 安装依赖...${NC}"
    $PIP_CMD install click rich pyyaml --user
    
    # 下载源码
    DOWNLOAD_SUCCESS=false
    DOWNLOAD_URLS=(
        "https://github.com/NekoNuo/depx/archive/refs/heads/master.zip"
        "https://github.com/NekoNuo/depx/archive/master.zip"
        "https://codeload.github.com/NekoNuo/depx/zip/refs/heads/master"
    )
    
    for url in "${DOWNLOAD_URLS[@]}"; do
        echo -e "${BLUE}🔗 尝试下载: $url${NC}"
        
        if command -v curl &> /dev/null; then
            if curl -fsSL "$url" -o depx.zip --connect-timeout 10 --max-time 60; then
                DOWNLOAD_SUCCESS=true
                break
            fi
        elif command -v wget &> /dev/null; then
            if wget -q "$url" -O depx.zip --timeout=60; then
                DOWNLOAD_SUCCESS=true
                break
            fi
        fi
        
        echo -e "${YELLOW}⚠️  下载失败，尝试下一个链接...${NC}"
    done
    
    if [[ "$DOWNLOAD_SUCCESS" == "false" ]]; then
        echo -e "${RED}❌ 源码下载失败${NC}"
        echo -e "${YELLOW}💡 请手动安装：${NC}"
        echo "  1. 访问: https://github.com/NekoNuo/depx"
        echo "  2. 下载源码"
        echo "  3. 运行: pip install . --user"
        cd /
        rm -rf "$TEMP_DIR"
        exit 1
    fi
    
    # 解压并安装
    if unzip -q depx.zip; then
        DEPX_DIR=$(find . -maxdepth 1 -type d -name "depx*" | head -1)
        if [[ -n "$DEPX_DIR" ]]; then
            cd "$DEPX_DIR"
            if $PIP_CMD install . --user; then
                echo -e "${GREEN}✅ 源码安装成功！${NC}"
                cd /
                rm -rf "$TEMP_DIR"
                return 0
            fi
        fi
    fi
    
    echo -e "${RED}❌ 源码安装失败${NC}"
    cd /
    rm -rf "$TEMP_DIR"
    exit 1
}

# 验证安装
verify_installation() {
    echo -e "${BLUE}🔍 验证安装...${NC}"
    
    if $PYTHON_CMD -m depx --version &> /dev/null; then
        VERSION=$($PYTHON_CMD -m depx --version)
        echo -e "${GREEN}✅ Depx 安装成功！版本: $VERSION${NC}"
        return 0
    else
        echo -e "${RED}❌ 安装验证失败${NC}"
        return 1
    fi
}

# 显示使用说明
show_usage() {
    echo -e "${PURPLE}"
    echo "🎉 Depx 安装完成！"
    echo ""
    echo "📋 常用命令："
    echo "  $PYTHON_CMD -m depx info .        # 分析当前目录"
    echo "  $PYTHON_CMD -m depx search react  # 搜索包 (所有包管理器)"
    echo "  $PYTHON_CMD -m depx scan          # 扫描项目"
    echo "  $PYTHON_CMD -m depx --help        # 查看帮助"
    echo ""
    echo "🔗 更多信息："
    echo "  GitHub: https://github.com/NekoNuo/depx"
    echo "  文档: https://github.com/NekoNuo/depx/blob/master/README.md"
    echo -e "${NC}"
}

# 主函数
main() {
    show_banner
    
    echo -e "${BLUE}🔍 正在检查系统环境...${NC}"
    check_os
    check_python
    check_pip
    
    echo -e "${BLUE}📦 开始安装 Depx...${NC}"
    
    # 尝试 PyPI 安装
    if ! install_depx; then
        # 如果 PyPI 失败，尝试源码安装
        install_from_source
    fi
    
    # 验证安装
    if verify_installation; then
        show_usage
    else
        echo -e "${RED}❌ 安装失败，请检查错误信息${NC}"
        exit 1
    fi
}

# 运行主函数
main "$@"
