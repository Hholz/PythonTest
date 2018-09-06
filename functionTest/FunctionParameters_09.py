"""函数的参数"""


# ===========默认参数=======================
def power(x):
    return x * x


print(power(2))


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2, 3))


# print(power(2))   #原来的函数失效了


def enaoll(name, gender):
    print('name:', name)
    print('gender:', gender)


enaoll("Sarah", "F")


def enaoll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enaoll('Sarah', 'F')
enaoll('Sarah', 'F', 10)
enaoll('Sarah', 'F', 10, 'Shengzhen')
enaoll('Sarah', 'F', city='Shengzhen')
enaoll('Sarah', 'F', 'Shengzhen')  # 深圳变成了age，错误的调用
enaoll('Sarah', 'F', city='Shengzhen', age=10)
enaoll(gender='F', name='Jack', city='Shengzhen', age=30)


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append("END")
    return L


print(add_end([1, 2, 3]))

print(add_end())
print(add_end())
print(add_end())


def add_end2(L):
    L.append("END")
    return L


print(add_end2([1, 2, 3]))


# print(add_end2())   #不报错，后面的代码也不运行

# print(add_end2(1))  #不报错，后面的代码也不运行


def add_end3(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end3())
print(add_end3())

# =========可变参数==============================================
'''参数numbers接收到的是一个tuple'''


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))
print(calc([1, 2, 3, 5, 7]))
print(calc((1, )))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc2(1, 2, 3))
print(calc2(1, 2, 3, 5, 7))
print('===========')
# print(calc2([1,2,3]))  #报错
nums = [1, 2, 3]
print(calc2(nums[1], nums[2]))


# =========关键字参数==============================================
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, other=extra)
person(age=21, name='Kang', other=extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Mary', 18, **extra)


# =========命名关键字参数==============================================
def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。
# 这种方式定义的函数如下：
print('=================================')


def person3(name, age, *, city, job):
    print(name, age, city, job)


person3('Jack', 24, city='Beijing', job='Engineer')
person3('Jack', 24, job='Engineer', city='Beijing')
# person3('Jack', 24, city='Beijing') #报错，必须加上job
# person3('Jack', 24, job='Engineer', city='Beijing' ,zipcode=123456) #无法运行
person3('Mary', 20, **extra)

print('=========person4========================')


def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person4('Mary', 20, **extra)
person4('Jack', 24, city='Shanghi', job='Engineer')
person4('Kang', 24, job='JAVA')

# =========参数组合==============================================
'''参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。'''


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, x=9)
f1(1, 2, 3, 'a', 'b', x=99)
f1(1, 2, '3', (4,), {'f': 7, 'g': 8})
f1(1, 2, '3', (4,), L={'f': 7, 'g': 8})
f1(1, 2, '3', (4,), **{'f': 7, 'g': 8})
f1(1, 2, '3', *(4, 8), **{'f': 7, 'g': 8})

f2(1, 2, d=99, ext=None)


def product(*args):
    if args == ():
        raise TypeError
    x = 1
    for i in args:
        x = x * i
    return x


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
