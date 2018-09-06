"""切片"""

L = [1, 2, 3, 4, 5, 6]
print(L[0:6])
print(L[:6])
print(L[:3])
print(L[2:4])
print(L[-2:])
print(L[-2:-3])
print(L[-2:-2])

print(L[-6:])
print(L[-7:])
print(L[-100:])
print(L[:])
print(L[:100])

print('=======================')
print(L[:6:2])

# tuple同理

# 字符串
print('ABCDEFG'[0:3])
print('ABCDEFG'[1:3])


def trim(s):
    if s == '':
        return s
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


print(trim("   ABC   "))
