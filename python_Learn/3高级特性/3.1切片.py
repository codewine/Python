#1
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])
#2
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
#3
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])

#
L = list(range(100))

print(L[:10:2]) #0-10每两个取一个
print(L[::5] )  #0-10每5个取一个

#元组切片 ()
#字符串切片
L= 'ABCDEFG'
print(L[1:3])