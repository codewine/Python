
list = (1,2,3,4)
for key in list:
     print(key)


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

print('---')
for key,value in d.items():
    print(key,value)

print('---')
for key in d.keys():
     print(key)

print('---')
for value in d.values():
     print(value)


 # 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from collections import Iterable


print(isinstance('abc', Iterable))  # str是否可迭代

print(isinstance([1,2,3], Iterable))  # list是否可迭代

print(isinstance(123, Iterable) ) # 整数是否可迭代


print('下标 循环')
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)

print('引用了两个变量')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)