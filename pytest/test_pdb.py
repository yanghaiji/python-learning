"""
debug 模式
# 遇到第一个失败时，调用 PDB 环境，然后退出整个执行过程
$ pytest -x --pdb

# 只有前三个失败用例调用 PDB 环境
$ pytest --pdb --maxfail=3

# 使用 exit 退出 PDB 环境，使用 continue 继续执行下面的步骤
"""


def test_pdb():
    x = 0
    assert x
