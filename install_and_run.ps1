# Depx 一键安装和运行脚本 (Windows PowerShell)
# 使用方法: irm https://raw.githubusercontent.com/your-repo/depx/main/install_and_run.ps1 | iex

# 设置错误处理
$ErrorActionPreference = "Stop"

# 设置控制台编码为 UTF-8
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    [Console]::InputEncoding = [System.Text.Encoding]::UTF8
    $env:PYTHONIOENCODING = "utf-8"
} catch {
    # 如果设置失败，继续执行但使用简化输出
    $global:UseSimpleOutput = $true
}

# 显示横幅
function Show-Banner {
    Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                        🚀 Depx v0.9.0                        ║" -ForegroundColor Cyan
    Write-Host "║                   跨语言依赖管理工具                          ║" -ForegroundColor Cyan
    Write-Host "║                     一键安装运行脚本                         ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

# 检查 Python
function Test-Python {
    Write-Host "🔍 正在检查 Python..." -ForegroundColor Blue
    
    $pythonCommands = @("python", "python3", "py")
    $pythonCmd = $null
    
    foreach ($cmd in $pythonCommands) {
        try {
            $version = & $cmd --version 2>$null
            if ($version -match "Python (\d+)\.(\d+)") {
                $major = [int]$matches[1]
                $minor = [int]$matches[2]
                if ($major -eq 3 -and $minor -ge 8) {
                    $pythonCmd = $cmd
                    Write-Host "✅ 找到 Python: $cmd ($version)" -ForegroundColor Green
                    break
                }
            }
        }
        catch {
            continue
        }
    }
    
    if (-not $pythonCmd) {
        Write-Host "❌ 未找到 Python 3.8+，请先安装 Python" -ForegroundColor Red
        Write-Host "下载地址: https://python.org/downloads/" -ForegroundColor Yellow
        Write-Host "或使用 winget: winget install Python.Python.3" -ForegroundColor Yellow
        exit 1
    }
    
    return $pythonCmd
}

# 检查 pip
function Test-Pip {
    param($pythonCmd)
    
    Write-Host "🔍 正在检查 pip..." -ForegroundColor Blue
    
    try {
        & $pythonCmd -m pip --version | Out-Null
        Write-Host "✅ pip 可用" -ForegroundColor Green
        return "$pythonCmd -m pip"
    }
    catch {
        Write-Host "❌ pip 不可用，请安装 pip" -ForegroundColor Red
        exit 1
    }
}

# 创建临时目录
function New-TempDirectory {
    $tempDir = Join-Path $env:TEMP "depx_$(Get-Random)"
    New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
    Write-Host "📁 创建临时目录: $tempDir" -ForegroundColor Blue
    return $tempDir
}

# 下载 Depx
function Get-Depx {
    param($tempDir)
    
    Write-Host "📥 正在下载 Depx..." -ForegroundColor Blue
    
    $zipUrl = "https://github.com/NekoNuo/depx/archive/master.zip"
    $zipPath = Join-Path $tempDir "depx.zip"
    $extractPath = Join-Path $tempDir "depx-master"
    
    try {
        # 下载 zip 文件
        Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath -UseBasicParsing
        
        # 解压文件
        Expand-Archive -Path $zipPath -DestinationPath $tempDir -Force
        
        # 进入解压目录
        Set-Location $extractPath
        
        Write-Host "✅ Depx 下载完成" -ForegroundColor Green
        return $extractPath
    }
    catch {
        Write-Host "❌ 下载失败: $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
}

# 安装依赖
function Install-Dependencies {
    param($pythonCmd, $pipCmd)
    
    Write-Host "📦 正在安装依赖..." -ForegroundColor Blue
    
    $dependencies = @("click", "rich", "pyyaml")
    
    foreach ($dep in $dependencies) {
        try {
            & $pythonCmd -c "import $dep" 2>$null
            Write-Host "✅ $dep 已安装" -ForegroundColor Green
        }
        catch {
            Write-Host "📦 安装 $dep..." -ForegroundColor Yellow
            Invoke-Expression "$pipCmd install $dep --user"
        }
    }
    
    Write-Host "✅ 所有依赖安装完成" -ForegroundColor Green
}

# 显示使用菜单
function Show-UsageMenu {
    param($pythonCmd)
    
    Write-Host ""
    Write-Host "🚀 Depx 已准备就绪！请选择运行方式：" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "1. 🖥️  交互式界面 - 友好的菜单界面" -ForegroundColor White
    Write-Host "2. 🖥️  简化交互界面 - Windows 兼容版本" -ForegroundColor White
    Write-Host "3. 📋 命令行模式 - 直接运行命令" -ForegroundColor White
    Write-Host "4. 📊 快速分析 - 分析当前目录" -ForegroundColor White
    Write-Host "5. 🔍 快速搜索 - 搜索包" -ForegroundColor White
    Write-Host "6. ❓ 显示帮助 - 查看所有命令" -ForegroundColor White
    Write-Host "7. 🚪 退出" -ForegroundColor White
    Write-Host ""
    
    $choice = Read-Host "请输入选项编号 (1-7)"
    
    switch ($choice) {
        "1" {
            Write-Host "启动交互式界面..." -ForegroundColor Blue
            try {
                # 检查是否有专门的 Windows 交互脚本
                if (Test-Path "windows_interactive.ps1") {
                    Write-Host "使用 Windows 优化交互界面..." -ForegroundColor Green
                    & powershell -ExecutionPolicy Bypass -File "windows_interactive.ps1" -PythonCmd $pythonCmd
                } else {
                    Write-Host "使用内置交互模式..." -ForegroundColor Yellow
                    # 内置简化交互模式
                    & powershell -Command "
                        `$env:PYTHONIOENCODING = 'utf-8'
                        Write-Host '=' * 60 -ForegroundColor Cyan
                        Write-Host '                    Depx v0.8.9' -ForegroundColor Cyan
                        Write-Host '               跨语言依赖管理工具' -ForegroundColor Cyan
                        Write-Host '                Windows 交互模式' -ForegroundColor Cyan
                        Write-Host '=' * 60 -ForegroundColor Cyan
                        Write-Host ''

                        do {
                            Write-Host '请选择操作：'
                            Write-Host '1. 分析当前目录'
                            Write-Host '2. 搜索包 (所有包管理器)'
                            Write-Host '3. 显示帮助'
                            Write-Host '0. 退出'

                            `$choice = Read-Host '请输入选项 (0-3)'

                            switch (`$choice) {
                                '1' {
                                    Write-Host '分析当前目录...' -ForegroundColor Blue
                                    & $pythonCmd -m depx info .
                                }
                                '2' {
                                    `$pkg = Read-Host '请输入要搜索的包名'
                                    if (`$pkg) {
                                        Write-Host '搜索包: ' `$pkg ' (所有包管理器)' -ForegroundColor Blue
                                        & $pythonCmd -m depx search `$pkg
                                    }
                                }
                                '3' {
                                    & $pythonCmd -m depx --help
                                }
                                '0' {
                                    Write-Host '退出交互模式' -ForegroundColor Green
                                    break
                                }
                                default {
                                    Write-Host '无效选项' -ForegroundColor Red
                                }
                            }

                            if (`$choice -ne '0') {
                                Read-Host '按 Enter 继续...'
                                Write-Host ''
                            }
                        } while (`$choice -ne '0')
                    "
                }
            } catch {
                Write-Host "交互界面启动失败: $($_.Exception.Message)" -ForegroundColor Red
                Write-Host "请尝试选项 3（命令行模式）" -ForegroundColor Yellow
            }
        }
        "2" {
            Write-Host "快速操作模式..." -ForegroundColor Blue
            try {
                $env:PYTHONIOENCODING = "utf-8"

                Write-Host "=" * 50 -ForegroundColor Green
                Write-Host "           Depx 快速操作" -ForegroundColor Green
                Write-Host "=" * 50 -ForegroundColor Green
                Write-Host ""

                do {
                    Write-Host "快速操作选项："
                    Write-Host "1. 分析当前目录"
                    Write-Host "2. 搜索包 (所有包管理器)"
                    Write-Host "3. 显示版本信息"
                    Write-Host "0. 返回主菜单"

                    $quickChoice = Read-Host "请输入选项 (0-3)"

                    switch ($quickChoice) {
                        "1" {
                            Write-Host ""
                            Write-Host "分析当前目录..." -ForegroundColor Blue
                            & $pythonCmd -m depx info .
                        }
                        "2" {
                            Write-Host ""
                            $pkg = Read-Host "请输入要搜索的包名"
                            if ($pkg) {
                                Write-Host "搜索包: $pkg (所有包管理器)" -ForegroundColor Blue
                                & $pythonCmd -m depx search $pkg
                            }
                        }
                        "3" {
                            Write-Host ""
                            Write-Host "Depx 版本信息:" -ForegroundColor Blue
                            & $pythonCmd -m depx --version
                            Write-Host ""
                            Write-Host "可用命令:" -ForegroundColor Blue
                            Write-Host "  info .        - 分析当前目录"
                            Write-Host "  search <包名> - 搜索包 (所有包管理器)"
                            Write-Host "  --help        - 显示完整帮助"
                        }
                        "0" {
                            Write-Host "返回主菜单" -ForegroundColor Green
                            break
                        }
                        default {
                            Write-Host "无效选项，请输入 0-3" -ForegroundColor Red
                        }
                    }

                    if ($quickChoice -ne "0") {
                        Write-Host ""
                        Read-Host "按 Enter 继续..."
                        Write-Host ""
                    }
                } while ($quickChoice -ne "0")

            } catch {
                Write-Host "快速操作模式失败: $($_.Exception.Message)" -ForegroundColor Red
                Write-Host "请尝试命令行模式 (选项 3)" -ForegroundColor Yellow
            }
        }
        "3" {
            Write-Host "进入命令行模式..." -ForegroundColor Blue
            Write-Host "输入 'exit' 退出"
            do {
                $cmd = Read-Host "depx>"
                if ($cmd -eq "exit" -or $cmd -eq "quit") {
                    break
                }
                if ($cmd) {
                    # 特殊处理帮助命令
                    if ($cmd -eq "--help" -or $cmd -eq "-h" -or $cmd -eq "help") {
                        Write-Host "Depx 可用命令：" -ForegroundColor Blue
                        Write-Host "  info [路径]          - 分析项目依赖"
                        Write-Host "  search <包名>        - 搜索包 (所有包管理器)"
                        Write-Host "  install <包名>       - 安装包"
                        Write-Host "  uninstall <包名>     - 卸载包"
                        Write-Host "  update [包名]        - 更新包"
                        Write-Host "  clean [路径]         - 清理依赖"
                        Write-Host "  scan [路径]          - 扫描项目"
                        Write-Host "  global-deps          - 全局依赖"
                        Write-Host "  export [路径]        - 导出结果"
                        Write-Host "  config               - 配置管理"
                        Write-Host "  --version            - 显示版本"
                        Write-Host "  --help               - 显示帮助"
                        Write-Host ""
                        Write-Host "示例："
                        Write-Host "  info .               - 分析当前目录"
                        Write-Host "  search react         - 搜索 react 包 (所有包管理器)"
                        Write-Host "  install express      - 安装 express 包"
                    } else {
                        try {
                            $env:PYTHONIOENCODING = "utf-8"
                            $env:PYTHONLEGACYWINDOWSSTDIO = "1"
                            # 使用 -m depx 方式运行，确保功能完整
                            Invoke-Expression "$pythonCmd -m depx $cmd"
                        } catch {
                            Write-Host "命令执行失败: $($_.Exception.Message)" -ForegroundColor Red
                            Write-Host "请检查命令格式是否正确" -ForegroundColor Yellow
                        }
                    }
                }
            } while ($true)
        }
        "4" {
            Write-Host "📊 分析当前目录..." -ForegroundColor Blue
            $env:PYTHONIOENCODING = "utf-8"
            & $pythonCmd -m depx info .
        }
        "5" {
            $package = Read-Host "🔍 请输入要搜索的包名"
            if ($package) {
                Write-Host "搜索包: $package (所有包管理器)" -ForegroundColor Blue
                $env:PYTHONIOENCODING = "utf-8"
                & $pythonCmd -m depx search $package
            }
        }
        "6" {
            & $pythonCmd -m depx --help
        }
        "7" {
            Write-Host "👋 感谢使用 Depx！" -ForegroundColor Green
            return $false
        }
        default {
            Write-Host "❌ 无效选项" -ForegroundColor Red
            return $true
        }
    }
    
    return $true
}

# 清理函数
function Remove-TempDirectory {
    param($tempDir)
    
    if (Test-Path $tempDir) {
        Write-Host "🧹 清理临时文件..." -ForegroundColor Blue
        Remove-Item $tempDir -Recurse -Force
    }
}

# 主函数
function Main {
    try {
        Show-Banner
        
        Write-Host "🔍 正在检查系统环境..." -ForegroundColor Blue
        $pythonCmd = Test-Python
        $pipCmd = Test-Pip $pythonCmd
        
        $tempDir = New-TempDirectory
        $depxDir = Get-Depx $tempDir
        Install-Dependencies $pythonCmd $pipCmd
        
        Write-Host "🎉 安装完成！" -ForegroundColor Green
        
        # 循环显示菜单
        do {
            $continue = Show-UsageMenu $pythonCmd
            if ($continue) {
                Write-Host ""
                $continueChoice = Read-Host "是否继续使用？(Y/n)"
                if ($continueChoice -match "^[Nn]$") {
                    Write-Host "👋 感谢使用 Depx！" -ForegroundColor Green
                    break
                }
            }
        } while ($continue)
    }
    catch {
        Write-Host "❌ 发生错误: $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
    finally {
        if ($tempDir) {
            Remove-TempDirectory $tempDir
        }
    }
}

# 运行主函数
Main
