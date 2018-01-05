"""使用list和tuple"""

#list
classmates = ['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[-1])
print(classmates[-2])

classmates.append('Adam')
print(classmates)

classmates.insert(1,'jack')
print(classmates)

#删除末尾
classmates.pop()
print(classmates)

classmates.pop(0)
print(classmates)

classmates[0] = 'jack2'
print(classmates)

L = ['Apple', 123 ,True]
print(L)
print("L = {0} {1} {2}".format(L[0],L[1],L[2]))

LL = ['python','java',['asp','php'],'scheme']
print(len(LL))
print(LL)

p = ['asp','php']
s = ['python','java',['asp','php'],'scheme']
print(s[2][0])

L2 = []
print(L2)

L2 = [1]
print(L2)

L2 = [1,]
print(L2)


#tuple
t = (1,2)
print(t)
print(t[0])

t = ()
print(t)

t = (1)
print(t) #定义的不是tuple

t = (1,)
print(t)

'''
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
tuple一开始指向的list并没有改成别的list
'''
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])