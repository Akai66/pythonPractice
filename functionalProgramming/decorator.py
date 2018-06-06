#装饰器
import functools
import datetime
import time
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call func:%s' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def hello():
    print('hello world!')
hello()

#带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s func:%s' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('exec')
def hello2():
    print('hello world!')
hello2()

#练习  设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        starttime = datetime.datetime.now()
        ret=fn(*args,**kw)
        endtime = datetime.datetime.now()
        print('%s executed in %s ms' % (fn.__name__,(endtime-starttime).microseconds))
        return ret
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


