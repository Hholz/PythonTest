"""定制类"""
'''
__slots__()
__len__()
__str__()
__repr__()
__iter__()
__next__()
__getitem__()
__setitem__()
__delitem__()
__getattr__()
__call__()
'''


# 在没找到属性的情况下调用__getattr__   调用类的方法或属性

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):  # __getattr__返回一个Chain类的实例，所以后面继续使用点符访问属性也是可以的，这就是链式调用的本质
        self._path = '{0}/{1}'.format(self._path, path)
        return self
        # return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __call__ = __getattr__
    __repr__ = __str__


print(Chain('/status').users('michael').repos)


# __call__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
print(s())  # self参数不要传入
print(callable(s))  # 是否是个可调用的
