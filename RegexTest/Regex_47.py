'''正则表达式'''

import re

r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(r)
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 切分字符串
print(re.split(r'\s+', 'a b   c'))

# 分组 用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
print(m.group(0))
for match in m.groups():
    print(match)

# 贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()
