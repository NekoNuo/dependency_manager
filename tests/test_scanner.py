"""
项目扫描器测试
"""

import pytest
import tempfile
import json
from pathlib import Path

from depx.core.scanner import ProjectScanner
from depx.parsers.base import ProjectType


class TestProjectScanner:
    """项目扫描器测试类"""
    
    def setup_method(self):
        """测试前准备"""
        self.scanner = ProjectScanner()
        self.temp_dir = Path(tempfile.mkdtemp())
    
    def teardown_method(self):
        """测试后清理"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_scan_empty_directory(self):
        """测试扫描空目录"""
        projects = self.scanner.scan_directory(self.temp_dir)
        assert projects == []
    
    def test_scan_nodejs_project(self):
        """测试扫描 Node.js 项目"""
        # 创建测试项目
        project_dir = self.temp_dir / "test-project"
        project_dir.mkdir()
        
        # 创建 package.json
        package_json = {
            "name": "test-project",
            "version": "1.0.0",
            "dependencies": {
                "lodash": "^4.17.21"
            },
            "devDependencies": {
                "jest": "^27.0.0"
            }
        }
        
        with open(project_dir / "package.json", "w") as f:
            json.dump(package_json, f)
        
        # 扫描项目
        projects = self.scanner.scan_directory(self.temp_dir)
        
        assert len(projects) == 1
        project = projects[0]
        assert project.name == "test-project"
        assert project.project_type == ProjectType.NODEJS
        assert len(project.dependencies) == 2  # lodash + jest
    
    def test_scan_multiple_projects(self):
        """测试扫描多个项目"""
        # 创建第一个项目
        project1_dir = self.temp_dir / "project1"
        project1_dir.mkdir()
        with open(project1_dir / "package.json", "w") as f:
            json.dump({"name": "project1", "version": "1.0.0"}, f)
        
        # 创建第二个项目
        project2_dir = self.temp_dir / "subdir" / "project2"
        project2_dir.mkdir(parents=True)
        with open(project2_dir / "package.json", "w") as f:
            json.dump({"name": "project2", "version": "1.0.0"}, f)
        
        # 扫描项目
        projects = self.scanner.scan_directory(self.temp_dir)
        
        assert len(projects) == 2
        project_names = {p.name for p in projects}
        assert project_names == {"project1", "project2"}
    
    def test_scan_single_project(self):
        """测试扫描单个项目"""
        # 创建测试项目
        project_dir = self.temp_dir / "single-project"
        project_dir.mkdir()
        
        package_json = {"name": "single-project", "version": "1.0.0"}
        with open(project_dir / "package.json", "w") as f:
            json.dump(package_json, f)
        
        # 扫描单个项目
        project = self.scanner.scan_single_project(project_dir)
        
        assert project is not None
        assert project.name == "single-project"
        assert project.project_type == ProjectType.NODEJS
    
    def test_scan_invalid_path(self):
        """测试扫描无效路径"""
        invalid_path = self.temp_dir / "nonexistent"
        projects = self.scanner.scan_directory(invalid_path)
        assert projects == []
    
    def test_get_supported_project_types(self):
        """测试获取支持的项目类型"""
        types = self.scanner.get_supported_project_types()
        assert ProjectType.NODEJS in types
