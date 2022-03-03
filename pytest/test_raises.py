"""
编写触发期望异常的断言
"""

import pytest
from _pytest._code import ExceptionInfo


def my_func():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError):
        my_func()
    assert '123' in str(ExceptionInfo.value)