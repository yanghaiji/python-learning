"""
集合类型
"""

user_name_list = ['yang', 'haiji', 'dylan']
print(user_name_list)

# 循环输出
for name in user_name_list:
    print(name)

# 常用API 演示

# 包含元素的个数
print(user_name_list.count('yang'))

# 第一次出现的位置
print(user_name_list.index('dylan'))
# 指定位置开始，第一次出现的位置
print(user_name_list.index('dylan', 2))

# 反转集合
user_name_list.reverse()
print(user_name_list)
# 添加
user_name_list.append('grape')
print(user_name_list)
# 排序
user_name_list.sort()
print(user_name_list)
# 弹出一个
print(user_name_list.pop())
