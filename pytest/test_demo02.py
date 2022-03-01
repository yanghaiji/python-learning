"""
在一个类中组织多个测试用例

测试类要符合特定的规则，pytest 才能发现它：

测试类的命名要符合Test*规则；
测试类中不能有__init__()方法，否则 pytest 无法采集到其中的测试用例；
PytestCollectionWarning: cannot collect test class 'TestClass' because it has a __init__ constructor.
"""


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

