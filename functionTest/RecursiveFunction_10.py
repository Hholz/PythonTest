"""递归函数"""

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

'''使用递归函数需要注意防止栈溢出。
在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：'''

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式


def fact(n):
    return fact_iter(n,1)


def fact_iter(num, product):
    if num==1:
        return product
    return fact_iter(num - 1,num * product)


# 优化
def fact2(n,m=1):
    if n==1:
        return m
    return fact2(n - 1,n*m)


print(fact2(5))