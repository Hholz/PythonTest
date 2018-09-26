from io import StringIO
from io import BytesIO

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
