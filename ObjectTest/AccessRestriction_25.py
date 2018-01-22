"""访问限制"""


# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


# __xxx__    双下划线开头，并且以双下划线结尾的    特殊变量   特殊变量是可以直接访问的
# __xxx       private  私有变量，     在外部可以_Student__name访问
# _xxx        实例变量外部是可以访问     但不建议外部访问
