"""
python 内置的标准模块
"""

import os

# 系统模块
# 返回当前系统的工作目录
cwd = os.getcwd()
print(cwd)
# 在指定目录创建文件夹
os.chdir("/python-learning/standard_library")
os.system("mkdir today")

# 赋权
# os.chmod()

# 下载文件
version = input('请输入安装包版本:')
cmd = fr'/usr/ wget http://mirrors.sohu.com/nginx/nginx-{version}.zip'
os.system(cmd)

print('下载完毕')

# 打开文件
os.startfile('/usr/xxx_mm.xlsx')
