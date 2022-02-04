"""
函数
"""


# 无参的函数
def print_info():
    print("-" * 30)
    print("      人生苦短，我用Python   ")
    print("-" * 30)


# 有惨的函数
def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# 有参数，且有返回值的函数
def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


#  有入参，且有多个返回值的
def dived(a, b):
    sh = a // b
    yu = a % b
    return sh, yu

