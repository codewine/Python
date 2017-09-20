

print("基本类型都可以用type()函数")
print(type(123))

print(type(123)==type(456))

print(type(123)==int)

print(type('abc')==type('123'))

print('判断一个对象是否是函数')
import types

def fn():
    pass

print(type(fn)==types.FunctionType)

print(type(abs)==types.BuiltinFunctionType)

print(type(lambda x: x)==types.LambdaType)

print(type((x for x in range(10)))==types.GeneratorType)

print('判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple')
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


print('如果要获得一个对象的所有属性和方法，可以使用dir()函数')
print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，下面的代码是等价的

len('ABC')
'ABC'.__len__()

###
print('配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：')

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()


print('# 有属性x吗？')
print(hasattr(obj, 'x'))
# 获取属性'x'
print(getattr(obj, 'x'))

fn = getattr(obj, 'power')

print(fn)
print(fn())

# 只有在不知道对象信息的时候，我们才会去获取对象信息
# 一个正确的用法的例子如下：

def readImage(fp):
    if hasattr(fp, 'read'):
        #首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流
        # return readData(fp)
    return None
