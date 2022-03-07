import pytest

"""
可以在执行的命令上添加一个 -v参数，查看执行的百分比
如： pytest -v test_parametrize.py
"""


@pytest.mark.parametrize("x,y", [(1, 2), (3, 4)])
def test_two(x, y):
    assert x + 1 == y


@pytest.mark.parametrize('user, passwd',
                         [('jack', 'abcdefgh'),
                          ('tom', 'a123456a')])
def test_passwd_md5(user, passwd):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
    }

    import hashlib

    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]
