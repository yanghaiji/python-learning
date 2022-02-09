"""
测试模块导入
如果只需要导入模块中的某个类或者工具，可以通过《 from 模块 import 需要导入的工具》 的方式进行导入，这样就不需要 **.的方式在使用

"""

from 测试模块2 import Dog
from 测试模块1 import say_hello

say_hello()
dog = Dog()
print(dog)

