"""继承和多态"""


# 定义的时候 * 的作用 将位置实参 装配成元组，** 的作用 将关键字实参 装配成字典
# 函数功能相同，但参数个数不同，python 如何处理？答案就是缺省参数。对那些缺少的参数设定为缺省参数即可解决问题。因为你假设函数功能相同，那么那些缺少的参数终归是需要用的。


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Cat meat...')


cat = Cat()
print(cat.run())
