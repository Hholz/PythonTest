"""使用dict和set"""
# dict的key必须是不可变对象。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 86}
print(d['Michael'])
print(d)
d['Michael'] = 100
print(d)

# dict是否存在某个key
bool = 'Michael' in d
bool2 = 'Jack' in d
print(bool)
print(bool2)

print(d.get('Michael'))
print(d.get('Jack'))
# 如果jack为空，返回0
print(d.get('Jack', 0))

d['Mary'] = 60
print(d)
d['Mary'] = None
print(d)
print(d.get('Mary'))

d.pop('Mary')
print(d)

d = {1: 10, 2: 20, 3: 30}
print(d)

d = {(1, 10): 10, (2, 20): 20, (2, 20): 30}
print(d)

# dict的key必须是不可变对象
# d = {[1,10]:10, [2,20]:20, [2,20]:30}
# print(d)


print('==============================================')

# set
s = set([1, 2, 3])
print(s)

s = set([1, 1, 2, 2, 3, 3])
print(s)

s.add(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# set不可以放入可变对象，因为无法判断两个可变对象是否相等

print("============================")
a = ['c', 'b', 'a']
a.sort()
print(a)
b = sorted(a, reverse=True)
print(b)
c = reversed(a)  # c只能使用一次
print(c)
print(list(c))
print(tuple(c))
print([i for i in c])

a = 'abc'
print(a.replace('a', 'A'))
