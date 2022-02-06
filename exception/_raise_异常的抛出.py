# 定义一个异常类
class PwdLengthError(Exception):
    pass


def create_password():
    pwd = input("请输入密码:")
    # 密码长度大于8直接返回，否则抛出异常
    if len(pwd) > 8:
        return pwd
    # 通过 raise 主动抛出异常
    pwd_err = PwdLengthError("密码长度不够")
    raise pwd_err


try:
    print(create_password())
except Exception as result:
    print(result)
