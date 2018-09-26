'''datetime'''
from datetime import datetime, timedelta, timezone

# 获取当前时间
print(datetime.now())
# 获取指定日期和时间
print(datetime(2015, 4, 19, 12, 20))
print(datetime(2015, 4, 19, 12))
print(datetime(2015, 4, 19))
# 获取时间戳
print(datetime.now().timestamp())  # Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# timestamp转换为datetime
t = 1536659504.554733
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))  # UTC时间
# str转换为datetime
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
print(datetime.strptime('2015-06-01 18:19:59', '%Y-%m-%d %H:%M:%S'))
# datetime转换为str
print(datetime.now().strftime('%a, %b %d %H:%M'))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
year = str(int(datetime.now().strftime('%Y')))
month = str(int(datetime.now().strftime('%m')))
day = str(int(datetime.now().strftime('%d')))
print(year + '-' + month + '-' + day)
# datetime加减
now = datetime.now()
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=1, hours=2, minutes=2, seconds=10, weeks=12))
# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8)
datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=timezone(timedelta(0, 28800)))
# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 拿到UTC时间，并强制设置时区为UTC+0:00:
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # astimezone()将转换时区为北京时间:
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(datetime.utcnow().astimezone(timezone(timedelta(hours=8))))