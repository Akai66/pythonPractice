#迭代
from collections import Iterable
d={'name':'Jack','age':18,'gender':'M'}
if isinstance(d,Iterable):
    for key in d:
        print(key)
    for value in d.values():
        print(value)
    for key,value in d.items():
        print(str(key)+':'+str(value))

#字符串也是可迭代对象
str='abc'
if isinstance(str,Iterable):
    for s in str:
        print(s)

#如何对list进行下标循环
L = ['Jack','Rose','Bob']
if isinstance(L,Iterable):
    for i,v in enumerate(L):
        print('%d-->%s' % (i,v))

#练习  迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) <= 0:
        return None,None
    min=max=L[0]
    for v in L:
        if v>max:
            max=v
        if v<min:
            min=v
    return min,max
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')