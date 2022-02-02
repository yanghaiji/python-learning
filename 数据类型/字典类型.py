"""
Python 內置数据类型是 字典 ，字典在其他语言里可能会被叫做 联合内存 或 联合数组。与以连续整数为索引的序列不同，字典是以 关键字 为索引的，
关键字可以是任意不可变类型，通常是字符串或数字。如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。
但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字。列表不能用作关键字，因为列表可以通过索引、切片或 append() 和 extend() 之类的方法来改变。

理解字典的最好方式，就是将它看做是一个 键: 值 对的集合（了解Java的同学可以回想一下Map这个数据结构），键必须是唯一的（在一个字典中）。一对花括号可以创建一个空字典：{} 。
另一种初始化字典的方式是在一对花括号里放置一些以逗号分隔的键值对，而这也是字典输出的方式。
"""

# 字典类型

# 定义字典类型
tel = {'jack': 4098, 'sape': 4139}

# 添加元素
tel['guido'] = 4127

print(tel)
# 根据key获取value
print("guido 的值为: " + str(tel['guido']))

# 删除元素
del tel['sape']
print(tel)

# 获取所有的key
print(list(tel))

# 排序
sorted(tel)

# 判断指定的key是否存在
flag = 'guido' in tel
print(flag)

# dict() 构造函数可以直接从键值对序列里创建字典
tel_dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel_dict)

# 循环获取数据
# 当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出
for k, v in tel_dict.items():
    print("-------")
    print(k)
    print(v)

# 当在序列中循环时，用 enumerate() 函数可以将索引位置和其对应的值同时取出
for i, v in enumerate(['tic', 'tac', 'toe']):
    print("------")
    print(i)
    print(v)

# 更多的大家可以多了解一下 ，如 zip，sorted，reversed