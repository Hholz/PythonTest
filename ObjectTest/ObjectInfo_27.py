"""对象信息"""
import types

# 基本类型，变量指向函数或者类
print(type(123))
print(type('str'))
print(type(None))
print(abs)


# 函数 返回对应的Class类型


# 判断一个对象是否是函数 用types模块中定义的常量
def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# isinstanct 判断是否属于某种类型。或某种类型的子类
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir() 获得一个对象的所有属性和方法
print(dir('str'))


# len()函数内部，它自动去调用该对象的__len__()方法
# 其他方法，getattr()、setattr()以及hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(setattr(obj, 'y', 19))  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y)  # 获取属性'y'

print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print(fn)
