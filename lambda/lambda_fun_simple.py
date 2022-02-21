# 非lambda的方式求平方


def ds_fun(x):
    return x * x


# 用lambda的方式求x的乘机
lam_fun = lambda x: x * x

print(ds_fun(10))
print(lam_fun(4))
