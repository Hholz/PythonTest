'''操作文件和目录'''

import os

print(os.name)  # 操作系统类型
# print(os.uname())# 操作系统类型
print(os.environ)  # 环境变量
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
print(os.path.join('/Users/michael', 'testdir'))
# os.mkdir('/testdir')  # 创建文件夹
# os.rmdir('/testdir')  # 删除文件夹

# 分割地址
print(os.path.split('/Users/michael/testdir/file.txt'))

# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
