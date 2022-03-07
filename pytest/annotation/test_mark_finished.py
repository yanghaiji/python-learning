"""
标记函数
"""
import pytest


def pytest_configure(config):
    marker_list = ["test1", "test2", "test3"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )


@pytest.mark.finished
def test_func1():
    assert 1 == 1


@pytest.mark.unfinished
def test_func2():
    assert 1 != 1

# 通过 -m 参数指定执行的标签
# pytest test_mark_finished.py -m unfinished


if __name__ == '__main__':
    pytest.mian(['-s', 'test_mark_finished.py', '-m finished'])
