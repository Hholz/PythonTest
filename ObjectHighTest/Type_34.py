"""使用元类 type()"""


# 注意有self和没self的区别
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


"""
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
"""
Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print(Hello)
print(h)

"""
metaclass, 元类
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
"""


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


"""
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
__new__()方法接收到的参数依次是：
    1.当前准备创建的类的对象；
    2.类的名字；
    3.类继承的父类集合；
    4.类的方法集合。

metaclass可以隐式地继承到子类，但子类自己却感觉不到
"""
