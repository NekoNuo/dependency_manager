"""
Depx 解析器模块

包含各种编程语言项目的配置文件解析器
"""

from .base import BaseParser, ProjectInfo, DependencyInfo
from .nodejs import NodeJSParser

__all__ = [
    "BaseParser",
    "ProjectInfo", 
    "DependencyInfo",
    "NodeJSParser",
]
