"""
利用我们学过的 input函数以及条件分支语句，实现一个找女朋友的小游戏
"""

"""
找女朋友的要求:
1. 理想型 : 身高 170 体重 98 年龄 22~28
2. 现实型 : 身高 160 体重 115 年龄 > 28 
"""
print("相亲开始...")

age = int(input("您的年龄是?"))
height = int(input("您的身高是?"))
weight = int(input("您的体重是?"))

if age < 18:
    print("未成年人慎入")
elif 22 < age < 28 and weight <= 98 and height >= 170:
    print("您是我的理想型，我们在一起吧！")
elif age > 28 and weight > 98 and not height <= 160:
    print("这就是现实，我只能接受！")
else:
    print("不在我的考虑范围之内...")
    pass
