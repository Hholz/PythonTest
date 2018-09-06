"""条件判断"""
age = 20
if age >= 18:
    print("your age is", age)
    print("adult")

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# x = None  #False
# x = 1   #True
# x = 0   #False
x = '1'  # True
if x:
    print('True')

# birth = input("birth:")
s = input("birth:")
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 计算BMI指数（体重除以身高的平方）
height = 1.75
weight = 60
bmi = weight / (height * height)
print('bmi = ', bmi)
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
