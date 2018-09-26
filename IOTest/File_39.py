"""文件操作"""

f = open('1.txt', 'r')
print(f.read())
f.close()
try:
    f = open('1.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('1.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

print('=============================')
with open('1.txt', 'r') as f:
    done = 0
    while not done:
        aLine = f.readline()
        if (aLine != ''):
            print(aLine)
        else:
            done = 1

f = open('1.txt', 'r', encoding='gbk', errors='ignore')
with open('1.txt', 'w') as f:
    f.write('Hello, world!')
