"""
Java 解析器测试
"""

import tempfile
import unittest
from pathlib import Path

from depx.parsers.java import JavaParser
from depx.parsers.base import DependencyType, ProjectType


class TestJavaParser(unittest.TestCase):
    """Java 解析器测试类"""

    def setUp(self):
        """测试前准备"""
        self.parser = JavaParser()
        self.temp_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        """测试后清理"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_project_type(self):
        """测试项目类型"""
        self.assertEqual(self.parser.project_type, ProjectType.JAVA)

    def test_config_files(self):
        """测试配置文件列表"""
        expected_files = [
            "pom.xml",
            "build.gradle",
            "build.gradle.kts",
            "gradle.properties",
        ]
        self.assertEqual(self.parser.config_files, expected_files)

    def test_can_parse_maven_project(self):
        """测试识别 Maven 项目"""
        # 创建 pom.xml 文件
        pom_file = self.temp_dir / "pom.xml"
        pom_file.write_text("""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>test-project</artifactId>
    <version>1.0.0</version>
</project>""")

        self.assertTrue(self.parser.can_parse(self.temp_dir))

    def test_can_parse_gradle_project(self):
        """测试识别 Gradle 项目"""
        # 创建 build.gradle 文件
        gradle_file = self.temp_dir / "build.gradle"
        gradle_file.write_text("""
plugins {
    id 'java'
}

dependencies {
    implementation 'org.springframework:spring-core:5.3.21'
}
""")

        self.assertTrue(self.parser.can_parse(self.temp_dir))

    def test_cannot_parse_non_java_project(self):
        """测试不识别非 Java 项目"""
        # 创建非 Java 项目文件
        package_json = self.temp_dir / "package.json"
        package_json.write_text('{"name": "test"}')

        self.assertFalse(self.parser.can_parse(self.temp_dir))

    def test_parse_maven_project(self):
        """测试解析 Maven 项目"""
        # 创建 pom.xml 文件
        pom_file = self.temp_dir / "pom.xml"
        pom_content = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>test-project</artifactId>
    <version>1.0.0</version>
    
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>5.3.21</version>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>"""
        pom_file.write_text(pom_content)

        project_info = self.parser.parse_project(self.temp_dir)

        self.assertIsNotNone(project_info)
        self.assertEqual(project_info.name, "test-project")
        self.assertEqual(project_info.project_type, ProjectType.JAVA)
        self.assertEqual(len(project_info.dependencies), 2)

        # 检查依赖信息
        spring_dep = next(
            (dep for dep in project_info.dependencies 
             if dep.name == "org.springframework:spring-core"), None
        )
        self.assertIsNotNone(spring_dep)
        self.assertEqual(spring_dep.version, "5.3.21")
        self.assertEqual(spring_dep.dependency_type, DependencyType.PRODUCTION)

        junit_dep = next(
            (dep for dep in project_info.dependencies 
             if dep.name == "junit:junit"), None
        )
        self.assertIsNotNone(junit_dep)
        self.assertEqual(junit_dep.version, "4.13.2")
        self.assertEqual(junit_dep.dependency_type, DependencyType.DEVELOPMENT)

    def test_parse_gradle_project(self):
        """测试解析 Gradle 项目"""
        # 创建 build.gradle 文件
        gradle_file = self.temp_dir / "build.gradle"
        gradle_content = """
plugins {
    id 'java'
}

dependencies {
    implementation 'org.springframework:spring-core:5.3.21'
    testImplementation 'junit:junit:4.13.2'
    api 'com.google.guava:guava:31.1-jre'
}
"""
        gradle_file.write_text(gradle_content)

        project_info = self.parser.parse_project(self.temp_dir)

        self.assertIsNotNone(project_info)
        self.assertEqual(project_info.project_type, ProjectType.JAVA)
        self.assertEqual(len(project_info.dependencies), 3)

        # 检查依赖类型
        spring_dep = next(
            (dep for dep in project_info.dependencies 
             if dep.name == "org.springframework:spring-core"), None
        )
        self.assertIsNotNone(spring_dep)
        self.assertEqual(spring_dep.dependency_type, DependencyType.PRODUCTION)

        junit_dep = next(
            (dep for dep in project_info.dependencies 
             if dep.name == "junit:junit"), None
        )
        self.assertIsNotNone(junit_dep)
        self.assertEqual(junit_dep.dependency_type, DependencyType.DEVELOPMENT)

    def test_parse_invalid_xml(self):
        """测试解析无效的 XML 文件"""
        # 创建无效的 pom.xml 文件
        pom_file = self.temp_dir / "pom.xml"
        pom_file.write_text("invalid xml content")

        project_info = self.parser.parse_project(self.temp_dir)

        # 应该能创建项目信息，但依赖列表为空
        self.assertIsNotNone(project_info)
        self.assertEqual(len(project_info.dependencies), 0)

    def test_detect_build_tool(self):
        """测试检测构建工具"""
        # Maven 项目
        pom_file = self.temp_dir / "pom.xml"
        pom_file.write_text("<project></project>")
        self.assertEqual(self.parser._detect_build_tool(self.temp_dir), "maven")

        # 清理
        pom_file.unlink()

        # Gradle 项目
        gradle_file = self.temp_dir / "build.gradle"
        gradle_file.write_text("// gradle build file")
        self.assertEqual(self.parser._detect_build_tool(self.temp_dir), "gradle")

    def test_has_wrapper(self):
        """测试检测包装器脚本"""
        # 创建 Maven 包装器
        mvnw_file = self.temp_dir / "mvnw"
        mvnw_file.write_text("#!/bin/bash")
        self.assertTrue(self.parser._has_wrapper(self.temp_dir))

        # 清理
        mvnw_file.unlink()

        # 创建 Gradle 包装器
        gradlew_file = self.temp_dir / "gradlew"
        gradlew_file.write_text("#!/bin/bash")
        self.assertTrue(self.parser._has_wrapper(self.temp_dir))

        # 清理
        gradlew_file.unlink()

        # 无包装器
        self.assertFalse(self.parser._has_wrapper(self.temp_dir))


if __name__ == "__main__":
    unittest.main()
