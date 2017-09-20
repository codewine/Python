def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s



def power1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s



print(power(3,4))

print(power1(3))


#
def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())

def add_end_t(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end_t())
print(add_end_t())
print(add_end_t())



# 可变参数
#
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2
# 个到任意个，还可以是0个。
#
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc((1,2,3,4)))
print(calc([]))

def calc_t(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc_t())
print(calc_t(1,2,3,4))

#
nums = [1, 2, 3]
print(calc_t(nums[0], nums[1], nums[2]))

nums = [1, 2, 3]
print(calc_t(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)

person('Bob', 35, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')
#
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 限制关键字参数的名字
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, city='Beijing', job='Engineer',addr='Chaoyang')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')


# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
#
print('类似func(*args, **kw)的形式调用')
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

print('*args是可变参数，args接收的是一个tuple；\n**kw是关键字参数，kw接收的是一个dict')