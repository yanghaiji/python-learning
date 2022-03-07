import pytest

"""
实现可预见的错误
"""


@pytest.mark.xfail(Exception,
                   reason='not supported until v0.2.0')
def test_api():
    assert 1 != 1
