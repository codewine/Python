def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x




print(my_abs(-100))


#空函数
def nop():
    pass  #作为占位符,可以保持语法正确

def sunAge(age):
    if age >= 18:
        pass
    else:
        pass
    return


#参数检查
def my_abs_serious(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs_serious(123))



#

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x)
print(x,y)
print(r)

