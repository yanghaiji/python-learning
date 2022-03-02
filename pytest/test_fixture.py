"""
这里的函数会先调用 conftest.py内定义的函数，并对拿到返回值
"""
import pytest


def test_fixture_01(haiji):
    print(f'\n haiji 的年龄为 {haiji}')
    assert haiji == '28'

#
# def search_user(user_id):
#     d = {
#         '001': 'xiaoming'
#     }
#     print("search user")
#     return d[user_id]
#
#
# def test_search(db):
#     assert search_user('001') == 'xiaoming'


"""
前置与后置处理
"""


def setup_function():
    print('前置')


def teardown_function():
    print('后置')


"""
module级别
"""


def setup_module():
    print(' setup_module前置')


def teardown_module():
    print('teardown_model 后置')


class TestDemo:

    def setup(self):
        print('setup 前置-----')

    def teardown(self):
        print('teardown 后置')

    def create(self):
        print('test model')

    def setup_class(self):
        print('class 前置')

    def teardown_class(self):
        print('class 后置')

    def setup_method(self):
        print('class 前置')

    def teardown_method(self):
        print('class 后置')


if __name__ == '__main__':
    # pytest.main(['-s', '-rA', '-q'])
    # pytest.main(['-s', 'test_fixture.py'])
    pytest.main(['-s', 'test_fixture.py'])
