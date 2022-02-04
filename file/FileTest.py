"""
对文件的操作
"""

# 打开文件
# w 代表写入模式，如果指定文件不存在将创建文件
import os

f = open("test.txt", "w")

# 将字符串写入文件
f.write("Hello,World!")

# 读取文件内容
# cont = f.read(5)

# 一次读出一行
# f.readline()

# 一次性取出整个文件为一个数据，每行为一个数组
# f.readlines()
print(cont)

# 关闭文件
f.close()

