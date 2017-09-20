
# class 表示类 ,括号表示父类
class Student(object):
    pass



bart = Student()
print(Student)
print(bart)


print('自由地给一个实例变量绑定属性')
bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


law = Student('law',99)
print(law.name)


class Student(object):
    def __init__(self):
         self.name = 'xx'
         self.score = 10

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

print(Student().get_grade())


print('和静态语言不同，Python允许对实例变量绑定任何数据，'
      '也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，'
      '但拥有的变量名称都可能不同')
