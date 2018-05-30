#递归函数
#在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出,解决办法有二:
#1.将递归改为循环实现
#2.改为尾递归实现
#递归
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))

#尾递归
def fact2(n):
    return factIter(n,1)
def factIter(n,product):
    if n==1:
        return product
    return factIter(n-1,n*product)
print(fact2(3))
#循环
def fact3(n):
    ret=1
    for x in range(1,n+1):
        ret=ret*x
    return ret
print(fact3(3))

#练习  汉诺塔问题
def move(n, a, b, c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
move(4,'A','B','C')


