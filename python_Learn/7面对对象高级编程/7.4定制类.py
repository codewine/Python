
# 定制类


print('__slots__')
print('__len__')

class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))


  # __str__


class Student1(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student1('Michael'))



# print('这是因为直接显示变量调用的不是__str__()，而是__repr__()，'
#       '两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，'
#       '也就是说，__repr__()是为调试服务的。解决办法是再定义一个__repr__()。'
#       '但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法')

# __repr__
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
print(Student1('Michael'))



# print('__iter__()方法，该方法返回一个迭代对象，'
#       '然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，'
#       '直到遇到StopIteration错误时退出循环')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)


# print('__getitem__ '
#       'Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：')

# print(Fib()[5])

# print('表现得像list那样按照下标取出元素，需要实现__getitem__()方法：')

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

print(Fib()[5])

# __getitem__ 与list不同
a = list(range(100))[5:10]
print(a)


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L



# '以上方法可以模仿系统自带的list'


# print('__getattr__可以获取未定义的属性 在没有找到属性的情况下，才调用__getattr__')

# 返回值
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
s = Student()
print(s.score)

# 返回函数
class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25


s = Student()
print(s.age())

# s.abc都会返回None  定义的__getattr__默认返回就是None
# 例子当 age 时 ,返回错误
class Student5(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# Student5().abc
print(Student5().age)


#
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


a = Chain().status.user.timeline.list
print(a)



# __call__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)



s = Student('Michael')
s()
# 需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(Student('')))
print(callable('str'))