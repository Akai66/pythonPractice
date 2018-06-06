#高阶函数
#map()和reduce()函数
from functools import reduce
def mpos(x,y=2):
    n=0
    ret=1
    while n<y:
        ret=ret*x
        n=n+1
    return ret
L=[1,2,3,4,5,6,7]
print(list(map(mpos,L)))

#加和
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5,6]))

#字符串转整数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(c):
    return DIGITS[c]
def fn(x,y):
    return x*10+y
def fl(x,y):
    return x*0.1+y
def str2int(str):
    return reduce(fn,list(map(char2num,str)))
print(str2int('1350'))
print(isinstance(str2int('1350'),int))

#练习1 利用map 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    def mtitle(s):
        return s.title()
    return list(map(mtitle,name))
print(normalize(['adam', 'LISA', 'barT']))

#练习2 编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def mult(x,y):
        return x*y
    return reduce(mult,L)
print(prod([1,2,3,4]))

#练习3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    arr=s.split('.')
    ivalue=reduce(fn,map(char2num,arr[0]))
    fvalue=0.1*reduce(fl,map(char2num,arr[1][::-1]))
    return ivalue+fvalue
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')






