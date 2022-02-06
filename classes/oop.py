"""
类提供了一种组合数据和功能的方法。 创建一个新类意味着创建一个新的对象 类型，从而允许创建一个该类型的新 实例
 每个类的实例可以拥有保存自己状态的属性。 一个类的实例也可以有改变自己状态的（定义在类中的）方法。
 class ClassName:
    <statement-1>
    .
    .
    <statement-N>

三大特性：封装 继承 多态
"""


class Person:

    # 无参初始化方法
    # def __init__(self):
    #     print("这是一个初始化方法，创建对象时，会自动被调用")

    def __init__(self, name, age):
        print("这是一个初始化方法，创建对象时，会自动被调用")
        self.name = name
        self.age = age
        self.__adder = "私有属性，外部无法调用"

    def __del__(self):
        print("对象被销毁")

    def __str__(self):
        return "name:" + self.name + ",age:" + str(self.age) + ",adder: " + self.__adder

    def run(self, name):
        print(name + "喜欢跑步")

    def eat(self, name):
        print(name + "喜欢吃各种美食")

    # 私有方法
    def __tet(self):
        print("这是一个私有方法，外部无法直接调用...")


x = Person("hai", 18)
print(x.name)
print(x.age)
# print(x.__adder)
print(x)
# print(x.__tet())
print("-" * 10)

"""
 ------ 继承 
 当一个类需要继承一个类是，在类名后添加(),在括号内填写需要继承的类，继承后，子类将具有父类的特性
 如果需要进行多继承，在括号内写多个类即可，用逗号进行分割
 class A:
    ....
    
 B 继承A   
 class B(A):  
    ...
如果继承后，父类的方法无法满足子类的，可以进行重写

"""


class Animal(object):

    def eat(self):
        print("吃....")

    def drink(self):
        print("喝....")

    def sleep(self):
        print("睡...")


class Dog(Animal):

    def call(self):
        print("汪汪汪...")

    def eat(self):
        print("吃骨头...")


dog = Dog()
dog.eat()
dog.drink()
dog.sleep()
dog.call()

"""
类方法，在之前写的都是示例方法，接下我们将定义类方法
当外部需要访问类属性时，可以定义类方法进行访问
"""


class Cat(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # 使用类名访问类属性
        Cat.count += 1

    # 通过类方法，访问类的属性
    @classmethod
    def show_count(cls):
        print("创建Cat类的次数 %d " % cls.count)


cat = Cat("tom")
cat.show_count()

cat2 = Cat("tom")
cat2.show_count()

"""
静态方法
不访问类属性，也不访问实例属性时，可将其定义为静态方法
"""


class Echo(object):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show(name):
        print("静态方法调用...%s " % name)


Echo.show("ddddd")
