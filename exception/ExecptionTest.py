"""
异常处理
"""

# 单一异常的处理方式
try:
    # r 模式下 ，如123.txt不存在的，将产生 FileNotFoundError
    f = open("123.txt", "r")
except IOError as err:
    print("打开文件失败")
    print(err)

# 多个异常的处理方式
try:
    # r 模式下 ，如123.txt不存在的，将产生 FileNotFoundError
    f = open("123.txt", "r")
except (IOError, RuntimeError) as err:
    print("打开文件失败 IOError")
    print(err)

# 如果不确定是什么异常可以，直接使用 Exception
try:
    # r 模式下 ，如123.txt不存在的，将产生 FileNotFoundError
    f = open("123.txt", "r")
except Exception as err:
    print("打开文件失败 Exception")
    print(err)

try:
    f = 1 // a
except Exception as err:
    print("打开文件失败....")
    print(err)
finally:
    print("始终会执行的代码块")


