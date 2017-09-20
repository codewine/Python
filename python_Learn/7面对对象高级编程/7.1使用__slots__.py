
class Student(object):
    pass


s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果


print('给一个实例绑定的方法，对另一个实例是不起作用的：')

# s2 = Student()
# s2.set_age(20)
# print(s2.age) # 测试结果


print('为了给所有实例都绑定方法，可以给class绑定方法：')
def set_score(self, score):
     self.score = score

Student.set_score = set_score



# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
# 来限制该class实例能添加的属性：


class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


print('定义的属性仅对当前类实例起作用，对继承的子类是不起作用的')


class GraduateStudent(Student):
     pass


G = GraduateStudent();
G.score = 999;
print(G.score)

print('除非在子类中也定义__slots__，'
      '这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。')

class GGtudent(Student):
    __slots__ = ()
    pass

G = GGtudent();
G.score = 999999;
print(G.score)

