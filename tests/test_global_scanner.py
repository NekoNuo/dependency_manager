"""
全局依赖扫描器测试
"""

import pytest
from unittest.mock import patch, MagicMock
import json

from depx.core.global_scanner import GlobalScanner
from depx.parsers.base import PackageManagerType


class TestGlobalScanner:
    """全局依赖扫描器测试类"""
    
    def setup_method(self):
        """测试前准备"""
        self.scanner = GlobalScanner()
    
    def test_init(self):
        """测试初始化"""
        assert self.scanner.home_dir.exists()
        assert len(self.scanner.detected_managers) == 0
    
    @patch('subprocess.run')
    def test_scan_npm_global_success(self, mock_run):
        """测试成功扫描 npm 全局依赖"""
        # 模拟 npm --version 成功
        mock_run.side_effect = [
            MagicMock(returncode=0),  # npm --version
            MagicMock(  # npm list -g --json
                returncode=0,
                stdout=json.dumps({
                    "dependencies": {
                        "typescript": {
                            "version": "5.3.0",
                            "description": "TypeScript compiler"
                        },
                        "nodemon": {
                            "version": "3.0.0",
                            "description": "Simple monitor script"
                        }
                    }
                })
            ),
            MagicMock(  # npm root -g
                returncode=0,
                stdout="/usr/local/lib/node_modules\n"
            )
        ]
        
        dependencies = self.scanner._scan_npm_global()
        
        assert len(dependencies) == 2
        assert PackageManagerType.NPM in self.scanner.detected_managers
        
        # 检查第一个依赖
        ts_dep = next(d for d in dependencies if d.name == "typescript")
        assert ts_dep.version == "5.3.0"
        assert ts_dep.package_manager == PackageManagerType.NPM
        assert ts_dep.description == "TypeScript compiler"
    
    @patch('subprocess.run')
    def test_scan_npm_global_command_not_available(self, mock_run):
        """测试 npm 命令不可用"""
        mock_run.side_effect = FileNotFoundError()
        
        dependencies = self.scanner._scan_npm_global()
        
        assert len(dependencies) == 0
        assert PackageManagerType.NPM not in self.scanner.detected_managers
    
    @patch('subprocess.run')
    def test_scan_pip_global_success(self, mock_run):
        """测试成功扫描 pip 全局依赖"""
        # 模拟 pip --version 成功
        mock_run.side_effect = [
            MagicMock(returncode=0),  # pip --version
            MagicMock(  # pip list --format=json
                returncode=0,
                stdout=json.dumps([
                    {"name": "requests", "version": "2.31.0"},
                    {"name": "numpy", "version": "1.24.0"},
                    {"name": "pandas", "version": "2.0.0"}
                ])
            )
        ]
        
        dependencies = self.scanner._scan_pip_global()
        
        assert len(dependencies) == 3
        assert PackageManagerType.PIP in self.scanner.detected_managers
        
        # 检查第一个依赖
        requests_dep = next(d for d in dependencies if d.name == "requests")
        assert requests_dep.version == "2.31.0"
        assert requests_dep.package_manager == PackageManagerType.PIP
    
    @patch('subprocess.run')
    def test_scan_yarn_global_success(self, mock_run):
        """测试成功扫描 yarn 全局依赖"""
        # 模拟 yarn --version 成功
        mock_run.side_effect = [
            MagicMock(returncode=0),  # yarn --version
            MagicMock(  # yarn global list --json
                returncode=0,
                stdout='{"type":"info","data":"@vue/cli@5.0.0"}\n{"type":"info","data":"create-react-app@5.0.1"}\n'
            )
        ]
        
        dependencies = self.scanner._scan_yarn_global()
        
        assert len(dependencies) == 2
        assert PackageManagerType.YARN in self.scanner.detected_managers
        
        # 检查依赖
        vue_dep = next(d for d in dependencies if d.name == "@vue/cli")
        assert vue_dep.version == "5.0.0"
        assert vue_dep.package_manager == PackageManagerType.YARN
    
    def test_get_detected_package_managers(self):
        """测试获取检测到的包管理器"""
        self.scanner.detected_managers.add(PackageManagerType.NPM)
        self.scanner.detected_managers.add(PackageManagerType.PIP)
        
        managers = self.scanner.get_detected_package_managers()
        
        assert len(managers) == 2
        assert PackageManagerType.NPM in managers
        assert PackageManagerType.PIP in managers
    
    @patch.object(GlobalScanner, '_scan_npm_global')
    @patch.object(GlobalScanner, '_scan_yarn_global')
    @patch.object(GlobalScanner, '_scan_pip_global')
    def test_scan_all_global_dependencies(self, mock_pip, mock_yarn, mock_npm):
        """测试扫描所有全局依赖"""
        # 模拟各个扫描器的返回值
        mock_npm.return_value = [MagicMock(name="typescript")]
        mock_yarn.return_value = [MagicMock(name="vue-cli")]
        mock_pip.return_value = [MagicMock(name="requests"), MagicMock(name="numpy")]
        
        dependencies = self.scanner.scan_all_global_dependencies()
        
        assert len(dependencies) == 4
        mock_npm.assert_called_once()
        mock_yarn.assert_called_once()
        mock_pip.assert_called_once()
    
    @patch.object(GlobalScanner, '_scan_npm_global')
    def test_scan_by_package_manager(self, mock_npm):
        """测试按包管理器扫描"""
        mock_npm.return_value = [MagicMock(name="typescript")]
        
        dependencies = self.scanner.scan_by_package_manager(PackageManagerType.NPM)
        
        assert len(dependencies) == 1
        mock_npm.assert_called_once()
    
    def test_scan_by_unsupported_package_manager(self):
        """测试扫描不支持的包管理器"""
        dependencies = self.scanner.scan_by_package_manager(PackageManagerType.CARGO)
        
        assert len(dependencies) == 0
