"""循环"""

# for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(range(10))
list = list(range(10))
print(list)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
n = 0
while n < len(L):
    print(L[n])
    n = n + 1

# n = 1
# while n <= 100:
#     print(n)
#     n = n + 1
# print('END')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
