"""
3.6版本后的 string格式化的简介方式
"""
from datetime import datetime

name = 'Peter'
age = 23

print('%s is %d years old' % (name, age))
print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')

# 可以使用 f 字符串中的字典
user = {'name': 'ji', 'age': 23}
print(f'{user["name"]} is a {user["age"]}')

# f 字符串格式化日期时间
now = datetime.now()
print(f'{now:%Y-%m-%d %H:%M}')

# f 字符串格式化浮点数
val = 12.3
print(f'{val:.2f}')
print(f'{val:.5f}')