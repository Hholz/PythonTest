"""函数式编程，返回函数"""


# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回


def cale_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f)
print(f())
print(f())

# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力

f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1 == f2)
print(f1())
print(f2())


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


ff1, ff2, ff3 = count()
print(ff1())
print(ff2())
print(ff3())


def count2():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


fff1, fff2, fff3 = count2()
print(fff1())
print(fff2())
print(fff3())


def createCounter():
    i = 0

    def counter():
        nonlocal i
        i += 1
        return i

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
