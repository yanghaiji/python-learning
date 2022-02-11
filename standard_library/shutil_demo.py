"""
对于日常文件和目录管理任务， shutil 模块提供了更易于使用的更高级别的接口:
"""
import shutil

# 文件复制
shutil.copyfile("test1.txt", "test2.txt")

# 文件移动
shutil.move('/build/executables', 'installdir')

