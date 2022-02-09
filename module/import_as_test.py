"""
测试模块导入
通过import 关键字进行带入,如果模块的名字过长，可以通过as 进行别名设置,需要满足大驼峰命名规则
如:
import 模块1 as Model1
import 模块2 as Model2
"""

import 测试模块1 as Model1
import 测试模块2 as Model2

Model1.say_hello()
cat = Model1.Cat()
print(cat)

Model2.say_hello()
dog = Model2.Dog()
print(dog)
