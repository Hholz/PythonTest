"""给实例绑定一个方法，给类绑定一个方法,   使用__slots__"""
from types import MethodType


# 给实例绑定一个方法，给类绑定一个方法
class Student(object):
    pass


s = Student()


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()  # 创建新的实例


# s2.set_age(25)  # 尝试调用方法


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
s2.set_score(99)
print(s.score)
print(s2.score)


# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student2(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student2()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'


# s.score = 99  # 绑定属性'score'


# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 当子类中没有__slots__时，不受限制
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Student3(Student2):
    __slots__ = ('score',)


s3 = Student3()
s3.score = 1000
s3.age = 30
# s3.city = 'sz'  # 不在父类和子类的__slots__中
print(s3.score)
print(s3.age)


class Student4(Student2):
    pass


class Student5(Student4):
    __slots__ = ('city',)


s5 = Student5()
s5.score = 1
s5.city = 'city'
print(s5.score)
print(s5.city)
print(isinstance(s5, Student2))
print(isinstance(s5, Student4))
print(issubclass(Student4, Student2))
