

# 变量从内存中变成可存储或传输的过程称之为序列化


# Python提供了pickle模块来实现序列化


import pickle

d = dict(name='Bob', age=20, score=88)

pickle.dumps(d)


# pickle.dumps()方法把任意对象序列化成一个bytes，
# 然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

print('Pickle 只能用于Python，并且可能不同版本的Python彼此都不兼容，'
      '因此，只能用Pickle保存那些不重要的数据')

# JSON

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json

d = dict(name='Bob', age=20, score=88)
a = json.dumps(d)
print(a)

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

# JSON反序列化为Python对象，用loads()或者对应的load()方法
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)


# JSON进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

# 对象使用方法序列化
print(json.dumps(s, default=student2dict))

# 偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。

# 要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))






