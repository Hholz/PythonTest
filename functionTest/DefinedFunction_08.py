"""定义函数"""
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-2))


def nop():
    pass


age = 1
if age >= 18:
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    #    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,int,float))):
    #       raise TypeError('Pleae type right int or float')
    if a == 0:
        return ('相同，非二元一次方程式')
    else:
        r = b * b - 4 * a * c
        if r < 0:
            return ('复数')
        else:
            x1 = (-b + math.sqrt(r)) / (2 * a)
            x2 = (-b - math.sqrt(r)) / (2 * a)
            return x1, x2


a = float(input('请输入系数a:'))
b = float(input('请输入系数b:'))
c = float(input('请输入系数c:'))
print('%dx^2+%dx+%d=0的解为%s' % (a, b, c, quadratic(a, b, c)))
