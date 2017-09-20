
print('装饰器')

def now():
    print('2015-3-25')
f = now
f()

print(f.__name__)
print(now.__name__)

print('这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）')

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')

now()
print(now.__name__)


print('decorator本身需要传入参数')

def logText(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logText('call')
def now1():
    print('2017-4-25')

now1()
print(now1.__name__)


print('因为返回的那个wrapper()函数名字就是"wrapper"，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，'
      '否则，有些依赖函数签名的代码执行就会出错。')

print('一个完整的decorator的写法如下：')

import functools
def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator



#作业
def testLog(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*_args,**kw):
            if (len(args) > 0):
                print('has args %s() ' % func.__name__)
            else:
                print('dont have args %s() ' % func.__name__)
            return func(*_args,**kw)
        return wrapper
    return decorator

@testLog()
def test():
    pass
test()

@testLog('excute')
def test1():
    pass
test1()