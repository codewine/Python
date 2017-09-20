

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(-1)


#元组  不能修改
classmates = ('Michael', 'Bob', 'Tracy')

t = (1, 2)
print(t)
t = (1,)
print(t)
t = ()
print(t)
t = (1)
print(t)




t = ('a', 'b', ['A', 'B'])
print(t)
