# 字符串类型时所有语言都有的，python当然也不例外

name = "Yang hai ji"
print(name)

# 看到这里有的朋友也许会问，为啥这样就写就是String类型了呢，这是由于python的语言决定
# 如果你像看某个字段的真是类型乐意通过 type函数
print(type(name))

# 常用的api

# 字符串的长度
print(name.__len__())

# 字符串拆分
print(name.split(" "))

# 查询指定字符串 可以指定查询范围 找不到时会返回-1
print(name.find("hai", 2, name.__len__()))

# 大小写转换
print(name.lower())
print(name.upper())

# 字符串追加
print(name.__add__(" python "))

# 是否可以转换成数组类型
print("13".isnumeric())

# 替换
print(name.replace(" ", '_'))
