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
# 添加2
# extend 将指定集合中的元素追加到到另一个集合中
# append 将当作一个整体进行添加，extend会解析
user_pwd = ['hai', 'ji']
user_name_list.extend(user_pwd)
print(user_name_list)

# 弹出一个
print(user_name_list.pop())

# 删除  del
del user_pwd[0]
print(user_pwd)
# 删除  remove
user_pwd.remove("ji")
print(user_pwd)

# 修改
user_pwd.append('test')
print(user_pwd)
user_pwd[0] = 'update'
print(user_pwd)

# 排序 默认是升序，如想实现降序，可以在sort内添加reverse=True
# user_name_list.sort(reverse=True)
user_name_list.sort()
print(user_name_list)
