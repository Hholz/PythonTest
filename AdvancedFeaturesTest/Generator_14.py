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

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。