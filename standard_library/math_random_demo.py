"""
math 模块提供对浮点数学的底层C库函数的访问:
"""
import math
import random
import statistics

nu = math.cos(111 / 33)
print(nu)
nu2 = math.log(100.0323, 5)
print(nu2)

"""
random 模块提供了进行随机选择的工具:
"""

choice = random.choice(['apple', 'pear', 'banana'])
print(choice)

sample = random.sample(range(100), 10)
print(sample)

"""
statistics 模块计算数值数据的基本统计属性（均值，中位数，方差等）:
"""

data = [2, 4, 6]
# 均值
statistics.mean(data)
# 中位数
statistics.median(data)
# 方差等
statistics.variance(data)
