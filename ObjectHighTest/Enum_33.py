"""枚举类型"""
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
print(Month.Jan)
print(Month.Jan.value)  # 值是从1开始
print(Month.Jan.name)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
# Weekday(7)
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

for week in Weekday:
    print(week)
    print(week.value)
    print(week.name)

