"""
有三个办公室，将若干个老师随机分配在这三间办公室里
"""

# 初始化三件办公室
import random

offices = [[], [], []]

# 初始化老师
nameList = ["A", "B", "C", "D", "E", "F", "G", "H", "M"]

# 进行随机分配
for name in nameList:
    office = random.randint(0, 2)
    offices[office].append(name)

index = 1
# 打印显示
for office in offices:
    print("第%d 办公室的老师为: %s" % (index, office))
    index += 1
