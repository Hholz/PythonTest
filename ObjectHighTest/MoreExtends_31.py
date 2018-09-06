"""多重继承, 可以看出调用哪个父类的方法"""
import inspect


# 请记住python多重继承的三大原则（3.x版本），再复杂的继承关系也不会混淆

# 1.子类永远在父类前面
# 2.如果有多个父类，会根据它们在列表中的顺序被检查
# 3.如果对下一个类存在两个合法的选择，选择第一个父类


# 类的继承问题http://python.jobbole.com/85685/
# 现在python3已经都是新式类了，就讲下新式类的继承
class D(object):
    pass


class E(object):
    pass


class F(object):
    pass


class C(D, F):
    pass


class B(E, D):
    pass


class A(B, C):
    pass


"""
A BED CDF
A B E C D F
"""
if __name__ == '__main__':
    print(inspect.getmro(A))
'''
C3 MRO算法
http://www.codeweblog.com/python-mro-c3%E7%AE%97%E6%B3%95/
C3 算法过程
A BED CDF
A B ED CDF
A B E D CDF
A B E CDF
A B E C DF
A B E C D F

类似完全遍历左根，再右根，去除前面的重复
A B E D C D F
去除重复D
A B E C D F 
'''


# 比如说这么一个多重继承，那么继承顺序就是，A-B-E-C-D-F


class G(object):
    pass


class D(object):
    def __init__(self):
        print("D")


class E(object):
    def __init__(self):
        print("E")


class F(object):
    def __init__(self):
        print("F")


class C(D, F):
    def __init__(self):
        print("C")


class B(E, G):
    def __init__(self):
        print("B")


class A(B, C):
    def __init__(self):
        print("A")


"""
A BEG CDF
A B E G C D F
"""

if __name__ == '__main__':
    print(inspect.getmro(A))
