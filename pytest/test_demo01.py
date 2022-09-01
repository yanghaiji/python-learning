"""
pytest 入门小案例

执行 pytest test_demo01.py
"""


def fun(x, y):
    return x * y


def test_answer():
    assert fun(3, 5) == 15
    assert fun(3, 5) != 15
