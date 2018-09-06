"""迭代器"""
# 直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；  （Iterable）
# 一类是generator，包括生成器和带yield的generator function  （Iterator）
from collections import Iterable, Iterator

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print('=====================')
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([x for x in range(10)], Iterator))
print(isinstance(100, Iterator))

print('=====================')
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abc'), Iterator))
print(isinstance(iter((x for x in range(10))), Iterator))
