

# 调试


# 1/print()
# 2/断言
# 3/logging
# 4/pdb
# 5/pdb.set_trace()
# 6/IDE

#2断言（assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# Python解释器时可以用 - O参数来关闭assert

# $ python3 -O err.py
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero

# 3 logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# logging.basicConfig(level=logging.INFO)
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning


# 4 pdb
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# err.py
s = '0'
n = int(s)
print(10 / n)

然后启动：

# $ python3 -m pdb err.py
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

# (Pdb) l
#   1     # err.py
#   2  -> s = '0'
#   3     n = int(s)
#   4     print(10 / n)

# 输入命令n可以单步执行代码：
#
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
# -> n = int(s)
# (Pdb) n
# > /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
# -> print(10 / n)

#  db.set_trace()

# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，
# 在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：


# 6 IDE
# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm：
#
# http://www.jetbrains.com/pycharm/
#
# 另外，Eclipse加上pydev插件也可以调试Python程序。