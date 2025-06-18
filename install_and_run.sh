#!/bin/bash
# Depx 一键安装和运行脚本
# 支持 Linux 和 macOS
# 使用方法: curl -fsSL https://raw.githubusercontent.com/your-repo/depx/main/install_and_run.sh | bash

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
    echo "║                        🚀 Depx v0.8.7                        ║"
    echo "║                   跨语言依赖管理工具                          ║"
    echo "║                     一键安装运行脚本                         ║"
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
    
    if [[ $(echo "$PYTHON_VERSION >= 3.8" | bc -l 2>/dev/null || echo "0") == "0" ]]; then
        # 如果没有 bc，使用 Python 比较版本
        VERSION_CHECK=$($PYTHON_CMD -c "import sys; print(1 if sys.version_info >= (3, 8) else 0)")
        if [[ "$VERSION_CHECK" == "0" ]]; then
            echo -e "${RED}❌ Python 版本过低，需要 3.8+，当前版本: $PYTHON_VERSION${NC}"
            exit 1
        fi
    fi
}

# 检查 pip
check_pip() {
    # 优先使用与 Python 对应的 pip
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

# 创建临时目录
create_temp_dir() {
    TEMP_DIR=$(mktemp -d)
    echo -e "${BLUE}📁 创建临时目录: $TEMP_DIR${NC}"
    cd "$TEMP_DIR"
}

# 下载 Depx
download_depx() {
    echo -e "${BLUE}📥 正在下载 Depx...${NC}"
    
    # 方法1: 使用 git clone（如果有 git）
    if command -v git &> /dev/null; then
        git clone https://github.com/NekoNuo/depx.git depx-repo
        cd depx-repo
    else
        # 方法2: 使用 curl 下载 zip
        if command -v curl &> /dev/null; then
            curl -L https://github.com/NekoNuo/depx/archive/master.zip -o depx.zip
            if command -v unzip &> /dev/null; then
                unzip -q depx.zip
                cd depx-master
            else
                echo -e "${RED}❌ 需要 unzip 命令来解压文件${NC}"
                exit 1
            fi
        elif command -v wget &> /dev/null; then
            wget https://github.com/NekoNuo/depx/archive/master.zip -O depx.zip
            if command -v unzip &> /dev/null; then
                unzip -q depx.zip
                cd depx-master
            else
                echo -e "${RED}❌ 需要 unzip 命令来解压文件${NC}"
                exit 1
            fi
        else
            echo -e "${RED}❌ 需要 curl 或 wget 来下载文件${NC}"
            exit 1
        fi
    fi
    
    echo -e "${GREEN}✅ Depx 下载完成${NC}"
}

# 安装依赖
install_dependencies() {
    echo -e "${BLUE}📦 正在安装依赖...${NC}"
    
    # 检查并安装依赖
    DEPS=("click" "rich" "pyyaml")
    for dep in "${DEPS[@]}"; do
        if ! $PYTHON_CMD -c "import $dep" &> /dev/null; then
            echo -e "${YELLOW}📦 安装 $dep...${NC}"
            $PIP_CMD install "$dep" --user
        else
            echo -e "${GREEN}✅ $dep 已安装${NC}"
        fi
    done
    
    echo -e "${GREEN}✅ 所有依赖安装完成${NC}"
}

# 显示使用菜单
show_usage_menu() {
    echo -e "${PURPLE}"
    echo "🚀 Depx 已准备就绪！请选择运行方式："
    echo ""
    echo "1. 🖥️  交互式界面 - 友好的菜单界面"
    echo "2. 📋 命令行模式 - 直接运行命令"
    echo "3. 📊 快速分析 - 分析当前目录"
    echo "4. 🔍 快速搜索 - 搜索包"
    echo "5. ❓ 显示帮助 - 查看所有命令"
    echo "6. 🚪 退出"
    echo -e "${NC}"
    
    read -p "请输入选项编号 (1-6): " choice < /dev/tty
    
    case $choice in
        1)
            echo -e "${BLUE}🖥️ 启动交互式界面...${NC}"
            $PYTHON_CMD interactive_depx.py
            ;;
        2)
            echo -e "${BLUE}📋 进入命令行模式...${NC}"
            echo "输入 'exit' 退出"
            while true; do
                read -p "depx> " cmd < /dev/tty
                if [[ "$cmd" == "exit" || "$cmd" == "quit" ]]; then
                    break
                fi
                if [[ -n "$cmd" ]]; then
                    # 特殊处理帮助命令
                    if [[ "$cmd" == "--help" || "$cmd" == "-h" || "$cmd" == "help" ]]; then
                        echo -e "${BLUE}📋 Depx 可用命令：${NC}"
                        echo "  info [路径]          - 分析项目依赖"
                        echo "  search <包名>        - 搜索包 (搜索所有包管理器)"
                        echo "  install <包名>       - 安装包"
                        echo "  uninstall <包名>     - 卸载包"
                        echo "  update [包名]        - 更新包"
                        echo "  clean [路径]         - 清理依赖"
                        echo "  scan [路径]          - 扫描项目"
                        echo "  global-deps          - 全局依赖"
                        echo "  export [路径]        - 导出结果"
                        echo "  config               - 配置管理"
                        echo "  --version            - 显示版本"
                        echo "  --help               - 显示帮助"
                        echo ""
                        echo "示例："
                        echo "  info .               - 分析当前目录"
                        echo "  search react         - 搜索 react 包 (所有包管理器)"
                        echo "  install express      - 安装 express 包"
                    else
                        # 使用 -m depx 方式运行，确保功能完整
                        $PYTHON_CMD -m depx $cmd
                    fi
                fi
            done
            ;;
        3)
            echo -e "${BLUE}📊 分析当前目录...${NC}"
            $PYTHON_CMD -m depx info .
            ;;
        4)
            read -p "🔍 请输入要搜索的包名: " package < /dev/tty
            if [[ -n "$package" ]]; then
                echo -e "${BLUE}🔍 搜索包: $package (所有包管理器)${NC}"
                $PYTHON_CMD -m depx search "$package"
            fi
            ;;
        5)
            $PYTHON_CMD -m depx --help
            ;;
        6)
            echo -e "${GREEN}👋 感谢使用 Depx！${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ 无效选项${NC}"
            show_usage_menu
            ;;
    esac
}

# 清理函数
cleanup() {
    if [[ -n "$TEMP_DIR" && -d "$TEMP_DIR" ]]; then
        echo -e "${BLUE}🧹 清理临时文件...${NC}"
        rm -rf "$TEMP_DIR"
    fi
}

# 设置清理陷阱
trap cleanup EXIT

# 检查是否可以交互
check_interactive() {
    if [[ ! -t 0 ]]; then
        echo -e "${YELLOW}⚠️  检测到非交互模式（可能通过管道执行）${NC}"
        echo -e "${BLUE}🚀 直接启动 Depx 命令行模式...${NC}"
        echo ""
        echo -e "${GREEN}✨ Depx 已安装完成！您可以使用以下命令：${NC}"
        echo "  $PYTHON_CMD -m depx info .        # 分析当前目录"
        echo "  $PYTHON_CMD -m depx search react  # 搜索包"
        echo "  $PYTHON_CMD -m depx --help        # 查看帮助"
        echo ""
        echo -e "${BLUE}💡 要获得交互界面，请下载脚本后本地运行：${NC}"
        echo "curl -fsSL https://raw.githubusercontent.com/NekoNuo/depx/master/install_and_run.sh -o install_depx.sh && bash install_depx.sh"
        return 1
    fi
    return 0
}

# 主函数
main() {
    show_banner

    echo -e "${BLUE}🔍 正在检查系统环境...${NC}"
    check_os
    check_python
    check_pip

    create_temp_dir
    download_depx
    install_dependencies

    echo -e "${GREEN}🎉 安装完成！${NC}"

    # 检查是否可以交互
    if ! check_interactive; then
        return 0
    fi

    # 循环显示菜单
    while true; do
        show_usage_menu
        echo ""
        read -p "是否继续使用？(Y/n): " continue_choice < /dev/tty
        if [[ "$continue_choice" =~ ^[Nn]$ ]]; then
            echo -e "${GREEN}👋 感谢使用 Depx！${NC}"
            break
        fi
    done
}

# 运行主函数
main "$@"
