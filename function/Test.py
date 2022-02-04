"""
用于测试模块的测试类
"""
from function import fibo

if __name__ == '__main__':
    fibo.print_info()
    fibo.fib(5)
    fib2 = fibo.fib2(5)
    print(fib2)
    sh, yu = fibo.dived(5, 2)
    print("商为%d 余数为%d" % (sh, yu))
