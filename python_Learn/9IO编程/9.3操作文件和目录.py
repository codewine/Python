

import os

os.name  # 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 获取详细的系统信息
os.uname()


# 环境变量

# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中

os.environ


# 要获取某个环境变量的值，可以调用os.environ.get('key')：
os.environ.get('PATH')


# 操作文件和目录
# 查看当前目录的绝对路径:
os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')


# 两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
# 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
os.path.split('/Users/michael/testdir/file.txt')

# os.path.splitext()可以直接让你得到文件扩展名
os.path.splitext('/path/to/file.txt')

print('合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作')

# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')

# 复制文件的函数居然在os模块中不存在
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']