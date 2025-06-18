#!/bin/bash
# 测试交互式脚本的本地版本

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
    echo "║                        🚀 Depx v0.8.6                        ║"
    echo "║                   跨语言依赖管理工具                          ║"
    echo "║                     本地测试脚本                             ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
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
    
    read -p "请输入选项编号 (1-6): " choice
    
    case $choice in
        1)
            echo -e "${BLUE}🖥️ 启动交互式界面...${NC}"
            python interactive_depx.py
            ;;
        2)
            echo -e "${BLUE}📋 进入命令行模式...${NC}"
            echo "输入 'exit' 退出"
            while true; do
                read -p "depx> " cmd
                if [[ "$cmd" == "exit" || "$cmd" == "quit" ]]; then
                    break
                fi
                if [[ -n "$cmd" ]]; then
                    python run_depx.py $cmd
                fi
            done
            ;;
        3)
            echo -e "${BLUE}📊 分析当前目录...${NC}"
            python run_depx.py info .
            ;;
        4)
            read -p "🔍 请输入要搜索的包名: " package
            if [[ -n "$package" ]]; then
                python run_depx.py search "$package"
            fi
            ;;
        5)
            python run_depx.py --help
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

# 检查是否可以交互
check_interactive() {
    if [[ ! -t 0 ]]; then
        echo -e "${YELLOW}⚠️  检测到非交互模式${NC}"
        return 1
    fi
    echo -e "${GREEN}✅ 交互模式正常${NC}"
    return 0
}

# 主函数
main() {
    show_banner
    
    echo -e "${BLUE}🔍 正在检查交互模式...${NC}"
    if ! check_interactive; then
        echo -e "${RED}❌ 无法进入交互模式${NC}"
        exit 1
    fi
    
    # 循环显示菜单
    while true; do
        show_usage_menu
        echo ""
        read -p "是否继续使用？(Y/n): " continue_choice
        if [[ "$continue_choice" =~ ^[Nn]$ ]]; then
            echo -e "${GREEN}👋 感谢使用 Depx！${NC}"
            break
        fi
    done
}

# 运行主函数
main "$@"
