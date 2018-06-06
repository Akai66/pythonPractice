#函数作为返回值
def my_sum(*nums):
    sum=0
    for n in nums:
        sum=sum+n
    return sum

print(my_sum(1,2,3,4))


def lazy_sum(*nums):
    def sum():
        sn=0
        for n in nums:
            sn=sn+n
        return sn
    return sum
L=[2,3,4,5]
f=lazy_sum(*L)
print(f())

def count():
    fs=[]
    for n in range(1,4):
        def double():
            return n*n
        fs.append(double)
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

#练习 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    n=0
    def count():
        nonlocal n
        n=n+1
        return n
    return count

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
