

print('生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
print(list(range(1, 11)))


print('[1x1, 2x2, 3x3, ..., 10x10]')
L = []
for x in range(1, 11):
     L.append(x * x)
print(L)
print('or')
print([x * x for x in range(1, 11)])

print('加上判断')
print([x * x for x in range(1, 11) if x % 2 == 0]  )

print('两层循环')
print([m + n for m in 'ABC' for n in 'XYZ'])


import os
print('列出当前目录下的所有文件和目录名')
print([d for d in os.listdir('.')])


#表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

print('把一个list中所有的字符串变成小写：')

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


L = ['Hello', 'World', 18, 'Apple', None]
m = [s.upper() for s in L if isinstance(s, str)]
print(m)