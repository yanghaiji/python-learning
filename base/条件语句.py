"""
python 与其他语言，都是有着条件语句的
if :
else :
"""

# 这是一个条件语句的示例

if __name__ == '__main__':
    age = 20

    if age < 8:
        print("少先队员...")
    elif age < 18:
        print("青少年...")
    elif age < 30:
        print("青年...")
    else:
        print("成年人")
