"""调用函数"""
#https://docs.python.org/3/library/functions.html#abs

print(abs(100))
print(abs(-20))
print(abs(3.14))

print(max(1,2))
print(max(3,2,5,1))
print(min(-1,0,1))
print(sum([12.3,3]))

print(int('1323'))
print(float('3.14'))
print(float(3.14))
print(str(1323))

print(bool(1))  #True
print(bool(0))   #False
print(bool('5'))  #True
print(bool(None))
print(bool('None'))
print(bool(''))


a = abs # 变量a指向abs函数
print(a(-1))  # 所以也可以通过a调用abs函数


print(str(hex(255)))
print(hex(255))