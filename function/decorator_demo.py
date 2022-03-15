def log(func):
    def wrapper(*ages, **kw):
        print('call %s():' % func.__name__)
        return func(*ages, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')



