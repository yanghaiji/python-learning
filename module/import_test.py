"""
测试模块导入
通过import 关键字进行带入
如:
import 模块1
import 模块2
"""

import 测试模块1
import 测试模块2

测试模块1.say_hello()
cat = 测试模块1.Cat()
print(cat)

测试模块2.say_hello()
dog = 测试模块2.Dog()
print(dog)
