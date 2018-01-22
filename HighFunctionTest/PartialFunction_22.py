"""偏函数"""

import functools

int2 = functools.partial(int, base=2)
print(int2("11111"))

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
print(int2('11111', base=2))
