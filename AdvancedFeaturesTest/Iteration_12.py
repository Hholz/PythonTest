"""迭代"""
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

for ch in 'ABC':
    print(ch)

print('=====================')
print(isinstance('abc', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代

# 循环的下标问题
# Python内置的enumerate函数可以把一个list变成索引-元素对(从0开始)
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

for x, y, z in [(1, 1, 1), (2, 4, 8), (3, 9, 27)]:
    print(x, y, z)


# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
