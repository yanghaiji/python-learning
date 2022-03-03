"""
pytest 的预制函数，放在其他的文件内，调用时，可之间返回，由于前期的数据准备


fixture 的作用域:
    function: 函数级，每个测试函数都会执行一次固件；
    class: 类级别，每个测试类执行一次，所有方法都可以使用； 对于类使用作用域，需要使用 pytest.mark.usefixtures ,对函数和方法也适用
    module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
    session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。
    package: 包级别，
    > 默认的作用域为 function

前置后置处理器
函数级别
    setup_function
    teardown_function
模块级别
    setup_module
    teardown_module
"""
import pytest


@pytest.fixture(scope='class')
def haiji():
    return '28'


# @pytest.fixture()
# def db():
#     print('Connection successful')
#
#     yield
#
#     print('Connection closed')
