
#
# i = 0
# while i < 100:
#
#     print(i%2)
#     if i%2==0:
#         print('let on')
#
#     else:
#         print('let off')
#
#
#     i += 1

a = 'm'
ord = ord(a)  #ASCII
print(ord)

b = bytes('许','utf-8')
print(b)

c = bytes('m','utf-8')
print(c)

d = b'd'
print(d)

print(b[0])
print(b[0:2])


b = bytearray('中文','utf-8')
print(len(b))

c = bytearray(2) #长度
print(c)

d = bytearray([1,2,3])
print(d)



