#偏函数
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
import functools
print(int('12345',base=8))
int2=functools.partial(int,base=2)
print(int2('1000'))
max2=functools.partial(max,10)
print(max2(1,2,3,4))