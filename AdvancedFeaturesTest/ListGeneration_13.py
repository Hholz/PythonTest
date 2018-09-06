"""
列表生成器
"""
import os

L = list(range(1, 11))
print(L)

L2 = []
for x in range(1, 11):
    L2.append(x * x)
print(L2)

L3 = [x * x for x in range(1, 11)]
print(L3)
L4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L4)

L5 = [m + n for n in 'ABC' for m in 'abc']
print(L5)

dir = [d for d in os.listdir('.')]
print(dir)

dir2 = os.listdir('.')  # os.listdir可以列出文件和目录
print(dir2)

d = {'x': 'A', 'y': 'B', 'r': 'C'}
dd = [k + '=' + v for k, v in d.items()]
print(dd)

low = ['Hello', 'World', 'IBM', 'Apple']
low2 = [s.lower() for s in low]
print(low2)

LL = ['Hello', 'World', 18, 'Apple', None]
LL2 = [s.lower() for s in LL if isinstance(s, str)]
print(LL2)
if LL2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
