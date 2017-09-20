

# 读文件

f = open('/Users/michael/test.txt', 'r')

f.read()

f.close()


try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()


#Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    print(f.read())


# read()会一次性读取文件的全部内容
# 1反复调用read(size)
# 2readline()可以每次读取一行内容
# 3readlines()一次读取所有内容并按行返回list

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

# file - like Object

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file - likeObject。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file - like
# Object不要求从特定类继承，只要写个read()方法就行。

# StringIO就是在内存中创建的file - like Object，常用作临时缓冲。

# 读取二进制文件
f = open('/Users/michael/test.jpg', 'rb')
# 非UTF-8编码的文本文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# 直接忽略 UnicodeDecodeError
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

#   写文件

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()

# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')