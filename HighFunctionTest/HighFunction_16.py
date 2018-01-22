"""高阶函数"""
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式

print(abs(-3))
print(abs)

f2 = abs;
print(f2(-4))


def add(x, y, f):
    return f(x) + f(y)


print(add(-4, 5, abs))
