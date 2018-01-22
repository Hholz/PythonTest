"""map/reduce"""
from functools import reduce


# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x ** 2


r = map(f, list(range(1, 10)))
print(next(r))
print(list(r))

r2 = map(f, [a for a in range(1, 10)])
r3 = list(r2)[:]
print(list(r3))
print(list(r3))

# r2是Iterator，只能list一次
# r2 = map(f, [a for a in range(1, 10)])
# print(list(r2))
# print(list(r2))


print(list(map(str, (1, 2, 3))))
print(list(map(str, {"name": "jack", "age": 23})))
print(list(map(str, {"name": "jack", "age": 23}.values())))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
# from functools import reduce
def add(x, y):
    return x + y


print(reduce(add, (1, 2, 3, 4, 5)))


# 把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 把str转换为int的函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# 用lambda函数进一步简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    l = name[1:].lower()
    u = name[0].upper()
    return u+l


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)