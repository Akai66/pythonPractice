#切片
#列表切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:1])
print(L[:3])
print(L[1:3])
print(L[-1:])
print(L[1:-1])
print(L[-2:-1])
L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[:10:2])
print(L[::10])
print(L[::-1])
#元组切片
T = ('Michael', 'Sarah', 'Tracy', 'Bob', 'Jack')
print(T[-3:])
#字符串切片
str='ABCDEFGHIJKLMN'
print(str[:3])
print(str[-100::2])

#练习,切片实现去除字符串两端的空格
def trim(str):
    while str[:1] == ' ':
        str = str[1:]
    while str[-1:] == ' ':
        str = str[:-1]
    return str
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')





