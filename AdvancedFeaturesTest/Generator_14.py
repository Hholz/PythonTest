"""
生成器
"""
# 列表生成器
L = [x * x for x in range(10)]

# 生成器
g = (x * x for x in range(10))
print(next(g))
print(next(g))

print('============')
for i in g:  # g从4开始了
    print(i)

print('============')


# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(3))


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib2(3))
print(next(fib2(3)))
g = fib2(3)
for i in g:
    print("g.next=", i)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib2(3)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def triangles():
    num = [1]
    while True:
        yield num
        num = [num[i] + num[i - 1] for i in range(len(num)) if i != 0]
        num.append(1)
        num.insert(0, 1)


trian = triangles()
print(next(trian))
print(next(trian))
print(next(trian))
print(next(trian))
print(next(trian))