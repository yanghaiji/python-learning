result = 0
try:
    num = int(input("请输入要计算的数字:"))

    result = 8 / num
except ValueError as er:
    print(er)
except Exception as er:
    print(er)
else:
    print("未发异常在会执行的代码")
    print("计算公式为: 8/%s , 结果为: %s" % (num, result))

finally:
    print("无论是否发生异常都将执行")
    print("-" * 20)
