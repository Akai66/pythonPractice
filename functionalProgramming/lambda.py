#匿名函数
from functools import reduce
L=list(map(lambda x:x*x,[1,2,3,4]))
print(L)
#将匿名函数赋值给变量
f=lambda x:pow(x,3)
print(f(3))
#将匿名函数作为函数返回值
def add():
    return lambda x,y:x+y
L=[1,2,3]
print(reduce(add(),L))

#练习 请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda n:n%2==1,range(1,20)))
print(L)