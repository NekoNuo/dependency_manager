#!/bin/bash
# 测试下载功能的简化脚本

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🧪 测试 Depx 下载功能...${NC}"

# 创建临时目录
TEMP_DIR=$(mktemp -d)
echo -e "${BLUE}📁 创建临时目录: $TEMP_DIR${NC}"
cd "$TEMP_DIR"

# 测试下载链接
DOWNLOAD_URLS=(
    "https://github.com/NekoNuo/depx/archive/refs/heads/master.zip"
    "https://github.com/NekoNuo/depx/archive/master.zip"
    "https://codeload.github.com/NekoNuo/depx/zip/refs/heads/master"
    "https://github.com/NekoNuo/depx/archive/refs/heads/main.zip"
    "https://github.com/NekoNuo/depx/archive/main.zip"
)

DOWNLOAD_SUCCESS=false

for url in "${DOWNLOAD_URLS[@]}"; do
    echo -e "${BLUE}🔗 测试链接: $url${NC}"
    
    if command -v curl &> /dev/null; then
        if curl -fsSL "$url" -o depx.zip --connect-timeout 10 --max-time 30; then
            echo -e "${GREEN}✅ 下载成功 (curl)${NC}"
            DOWNLOAD_SUCCESS=true
            break
        else
            echo -e "${YELLOW}⚠️  curl 下载失败${NC}"
        fi
    fi
    
    if command -v wget &> /dev/null; then
        if wget -q "$url" -O depx.zip --timeout=30; then
            echo -e "${GREEN}✅ 下载成功 (wget)${NC}"
            DOWNLOAD_SUCCESS=true
            break
        else
            echo -e "${YELLOW}⚠️  wget 下载失败${NC}"
        fi
    fi
done

if [[ "$DOWNLOAD_SUCCESS" == "true" ]]; then
    echo -e "${GREEN}🎉 下载测试成功！${NC}"
    
    # 测试解压
    if command -v unzip &> /dev/null; then
        if unzip -q depx.zip; then
            echo -e "${GREEN}✅ 解压成功${NC}"
            
            # 查找目录
            DEPX_DIRS=$(find . -maxdepth 1 -type d -name "depx*")
            if [[ -n "$DEPX_DIRS" ]]; then
                echo -e "${GREEN}📁 找到目录:${NC}"
                echo "$DEPX_DIRS"
                
                # 检查关键文件
                for dir in $DEPX_DIRS; do
                    if [[ -f "$dir/depx/__init__.py" ]]; then
                        echo -e "${GREEN}✅ 找到 depx 模块${NC}"
                        break
                    fi
                done
            else
                echo -e "${YELLOW}⚠️  未找到 depx 目录${NC}"
            fi
        else
            echo -e "${RED}❌ 解压失败${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  未安装 unzip${NC}"
    fi
else
    echo -e "${RED}❌ 所有下载链接都失败${NC}"
    echo -e "${YELLOW}💡 可能的原因：${NC}"
    echo "  1. 网络连接问题"
    echo "  2. GitHub 访问受限"
    echo "  3. 仓库链接已变更"
fi

# 清理
echo -e "${BLUE}🧹 清理临时文件...${NC}"
cd /
rm -rf "$TEMP_DIR"

echo -e "${BLUE}🏁 测试完成${NC}"
