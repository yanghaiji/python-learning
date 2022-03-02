如果你不想通过控制太知名进行测试，可以通过一下函数进行测试

```python
import pytest

if __name__ == '__main__':
    pytest.main(['-v', 'test_demo01.py', '-s'])
# pytest.main 内传递的为数组，可以时命令，也可以指定文件，或者指定文件的函数 函数的个数为 "test_demo01.py::test_answer
```

## 需要安装插件
```python
pip install pytest-html
```

## fixture 的作用域:
- function: 函数级，每个测试函数都会执行一次固件；
- class: 类级别，每个测试类执行一次，所有方法都可以使用； 对于类使用作用域，需要使用 pytest.mark.usefixtures ,对函数和方法也适用
- module: 模块级，每个模块执行一次，模块内函数和方法都可使用；
- session: 会话级，一次测试只执行一次，所有被找到的函数和方法都可用。
- package: 包级别
> 默认的作用域为 function

## 前置后置处理器
- 函数级别
    - setup_function 
    - teardown_function
- 模块级别
    - setup_module
    - teardown_module