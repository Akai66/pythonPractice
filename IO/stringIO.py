from io import StringIO,BytesIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f=StringIO('hello\nworld\nganbade')
while True:
    line=f.readline()
    if line == '':
        break
    print(line.strip())


f=BytesIO()
f.write('加油'.encode('utf-8'))
print(f.getvalue())
