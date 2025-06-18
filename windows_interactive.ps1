# Windows Depx 交互式界面
# 专为 Windows PowerShell 优化的交互脚本

param(
    [string]$PythonCmd = "python"
)

# 设置错误处理
$ErrorActionPreference = "Stop"

# 设置编码
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONLEGACYWINDOWSSTDIO = "1"

# 尝试设置控制台编码
try {
    chcp 65001 | Out-Null
} catch {
    # 忽略编码设置错误
}

function Show-Banner {
    Write-Host "=" * 60 -ForegroundColor Cyan
    Write-Host "                    Depx v0.8.9" -ForegroundColor Cyan
    Write-Host "               跨语言依赖管理工具" -ForegroundColor Cyan
    Write-Host "                Windows 交互模式" -ForegroundColor Cyan
    Write-Host "=" * 60 -ForegroundColor Cyan
    Write-Host ""
}

function Show-Menu {
    Write-Host ""
    Write-Host "请选择要执行的操作：" -ForegroundColor White
    Write-Host ""
    Write-Host "1. 分析项目依赖 (info)" -ForegroundColor White
    Write-Host "2. 搜索包 (search) - 搜索所有包管理器" -ForegroundColor White
    Write-Host "3. 安装包 (install)" -ForegroundColor White
    Write-Host "4. 卸载包 (uninstall)" -ForegroundColor White
    Write-Host "5. 更新包 (update)" -ForegroundColor White
    Write-Host "6. 清理依赖 (clean)" -ForegroundColor White
    Write-Host "7. 扫描全局依赖 (scan)" -ForegroundColor White
    Write-Host "8. 导出结果 (export)" -ForegroundColor White
    Write-Host "9. 配置管理 (config)" -ForegroundColor White
    Write-Host "0. 退出" -ForegroundColor White
    Write-Host ""
}

function Get-PathInput {
    $path = Read-Host "请输入项目路径 (默认为当前目录 '.')"
    if ([string]::IsNullOrWhiteSpace($path)) {
        return "."
    }
    return $path.Trim()
}

function Get-PackageInput {
    $package = Read-Host "请输入包名"
    return $package.Trim()
}

function Execute-DepxCommand {
    param([string[]]$Args)
    
    try {
        $cmdString = "$PythonCmd -m depx " + ($Args -join " ")
        Write-Host "执行命令: $cmdString" -ForegroundColor Blue
        Write-Host "-" * 50
        
        & $PythonCmd -m depx @Args
        
        Write-Host "-" * 50
        Write-Host "命令执行完成" -ForegroundColor Green
    } catch {
        Write-Host "命令执行失败: $($_.Exception.Message)" -ForegroundColor Red
    }
}

function Test-DepxAvailable {
    try {
        & $PythonCmd -m depx --version | Out-Null
        return $true
    } catch {
        return $false
    }
}

function Main {
    Show-Banner
    
    # 检查 Depx 是否可用
    if (-not (Test-DepxAvailable)) {
        Write-Host "错误: 无法找到 Depx 模块" -ForegroundColor Red
        Write-Host "请确保已正确安装 Depx" -ForegroundColor Yellow
        Write-Host "安装命令: pip install depx --user" -ForegroundColor Yellow
        Read-Host "按 Enter 键退出..."
        exit 1
    }
    
    Write-Host "Windows 交互模式 - 简化版本" -ForegroundColor Green
    Write-Host "如果遇到问题，请使用命令行模式: $PythonCmd -m depx --help" -ForegroundColor Yellow
    
    while ($true) {
        try {
            Show-Menu
            $choice = Read-Host "请输入选项编号 (0-9)"
            
            switch ($choice) {
                "0" {
                    Write-Host "感谢使用 Depx！" -ForegroundColor Green
                    return
                }
                "1" {
                    # 分析项目依赖
                    $path = Get-PathInput
                    Write-Host ""
                    Write-Host "正在分析项目: $path" -ForegroundColor Blue
                    Execute-DepxCommand @("info", $path)
                }
                "2" {
                    # 搜索包
                    $package = Get-PackageInput
                    if (-not [string]::IsNullOrWhiteSpace($package)) {
                        Write-Host ""
                        Write-Host "正在搜索包: $package (所有包管理器)" -ForegroundColor Blue
                        Execute-DepxCommand @("search", $package)
                    }
                }
                "3" {
                    # 安装包
                    $package = Get-PackageInput
                    if (-not [string]::IsNullOrWhiteSpace($package)) {
                        Write-Host ""
                        Write-Host "正在安装包: $package" -ForegroundColor Blue
                        Execute-DepxCommand @("install", $package)
                    }
                }
                "4" {
                    # 卸载包
                    $package = Get-PackageInput
                    if (-not [string]::IsNullOrWhiteSpace($package)) {
                        Write-Host ""
                        Write-Host "正在卸载包: $package" -ForegroundColor Blue
                        Execute-DepxCommand @("uninstall", $package)
                    }
                }
                "5" {
                    # 更新包
                    $package = Read-Host "请输入包名 (留空检查所有过时包)"
                    Write-Host ""
                    if ([string]::IsNullOrWhiteSpace($package)) {
                        Write-Host "正在检查过时的包..." -ForegroundColor Blue
                        Execute-DepxCommand @("update", "--check")
                    } else {
                        Write-Host "正在更新包: $package" -ForegroundColor Blue
                        Execute-DepxCommand @("update", $package.Trim())
                    }
                }
                "6" {
                    # 清理依赖
                    $path = Get-PathInput
                    Write-Host ""
                    Write-Host "正在清理项目: $path" -ForegroundColor Blue
                    Execute-DepxCommand @("clean", $path)
                }
                "7" {
                    # 扫描全局依赖
                    Write-Host ""
                    Write-Host "正在扫描全局依赖..." -ForegroundColor Blue
                    Execute-DepxCommand @("scan")
                }
                "8" {
                    # 导出结果
                    $path = Get-PathInput
                    Write-Host ""
                    Write-Host "正在导出分析结果: $path" -ForegroundColor Blue
                    Execute-DepxCommand @("export", $path)
                }
                "9" {
                    # 配置管理
                    Write-Host ""
                    Write-Host "配置管理" -ForegroundColor Blue
                    Execute-DepxCommand @("config")
                }
                default {
                    Write-Host "无效选项，请输入 0-9 之间的数字" -ForegroundColor Red
                }
            }
            
            # 等待用户按键继续
            if ($choice -ne "0") {
                Write-Host ""
                Read-Host "按 Enter 键继续..."
                Write-Host ""
                Write-Host "=" * 60
            }
            
        } catch {
            Write-Host "发生错误: $($_.Exception.Message)" -ForegroundColor Red
            Read-Host "按 Enter 键继续..."
        }
    }
}

# 运行主函数
Main
