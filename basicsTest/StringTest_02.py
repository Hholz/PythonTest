"""
字符串和编码
"""

print("包含中文的str")
# ord() 字符转成整数
print(ord('A'))
print(ord('中'))
# 整数转成字符
print(chr(65))
print('\u4e2d\u6587')
print('======================')

x = b'ABC'
print(x)
print('ABC'.encode('ascii'))
print('中文'.encode('UTF-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print('hello, %s' % 'world')
print('Hi, %s, you have $%d' % ('jack', 1000))
print('整数：%d, 浮点数：%f, 字符串：%s, 十六进制：%x' % (1, 1, 'a', 16))
print('%02d-%2d' % (3, 1))
print('%.2f' % 3.14159)
print('%0.2f' % 3.14159)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (85 / 72 - 1) * 100
print('小明的成绩从去年的%d分提升到了今年的%d分,提升了%.1f %%' % (s1, s2, r))
print('小明的成绩从去年的{0}分提升到了今年的{1}分,提升了{2:.1f} %'.format(s1, s2, r))


def change(x, y):
    x = 2
    y[0] = 'hello'


x = 3
y = [1, 2]
print(change(x, y))
print(x)
print(y)
