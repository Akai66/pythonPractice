#迭代器
from collections import Iterable
from collections import Iterator
print(isinstance([1,2],Iterable))
print(isinstance((1,2),Iterable))
print(isinstance({1:'one',2:'two'},Iterable))
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

print(isinstance([1,2],Iterator))
print(isinstance((1,2),Iterator))
print(isinstance({1:'one',2:'two'},Iterator))
print(isinstance('abc',Iterator))
print(isinstance(123,Iterator))
I=(x*x for x in range(10) if x%2==0)
print(isinstance(I,Iterator))

#可通过iter方法将Iterable变为Iterator
print(isinstance(iter([1,2]),Iterator))
print(isinstance(iter((1,2)),Iterator))
print(isinstance(iter({1:'one',2:'two'}),Iterator))
print(isinstance(iter('abc'),Iterator))
print(isinstance(123,Iterator))

while True:
    try:
        print(next(I))
    except StopIteration:
        break

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
