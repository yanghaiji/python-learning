# 数字类型
# Python 支持四种不同的数值类型：
#
# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
# 长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
# 浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

age = 29
print(age)

num = -9

# 常用api演示

# 加法计算， 自带了加法计算器,是不是很神奇
print(age.__add__(9))

# 取绝对值
print(num.__abs__())

# 将number 转换成字符串
print(type(num.__str__()))

# 值对比操作
print(age.__le__(num))
print(num.__lt__(age))
print(num.__ge__(age))
print(num.__gt__(age))
print(age.__eq__(num))

#
print(age.__doc__)

