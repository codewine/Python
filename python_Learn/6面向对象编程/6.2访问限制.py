


print('如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，'
      '在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），'
      '只有内部可以访问，外部不能访问')


class Students(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score



    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 允许外部代码修改私有变量
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Students('Bart Simpson', 98)
bart.print_score()


bart.set_score(90)


print('注意')
print('1/变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，'
      '特殊变量是可以直接访问的，不是private变量')

print('2/一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，'
      '但是，按照约定俗成的规定，当你看到这样的变量时，'
      '意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问')


print('3/双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。'
      '不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，'
      '所以，仍然可以通过_Student__name来访问__name变量')

print('4/不同版本的Python解释器可能会把__name改成不同的变量名')


