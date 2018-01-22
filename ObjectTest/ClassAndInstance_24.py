"""类与实例"""


# 面向对象最重要的概念就是类（Class）和实例（Instance），
# 必须牢记类是抽象的模板，比如Student类，而实例是根据类创建
# 出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
class Student(object):
    pass


# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
# 比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
bart = Student()
stu = Student
print(bart)
print(Student)
print(stu)


# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，
# 调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


bart2 = Student2('张三', 80)
print(bart2)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


print(print_score(bart2))
# print(print_score(bart)) # 报错
