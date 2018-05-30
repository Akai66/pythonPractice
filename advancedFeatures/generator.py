#生成器
g=(x*x for x in range(1,11))
print(g)
#print(next(g))
for x in g:
    print(x)
#斐波那契
def fib(n):
    x,a,b=0,0,1
    while x<n:
        yield b
        tmp=b
        b=a+b
        a=tmp
        x=x+1
f=fib(5)
for x in f:
    print(x)

#循环
def fib2(n):
    if n<=2:
        return 1
    else:
        x,a,b=0,1,1
        while x<(n-2):
            tmp=b
            b=a+b
            a=tmp
            x=x+1
        return b
print(fib2(5))

#递归
def fib3(n):
    if n<=2:
        return 1
    else:
        return fib3(n-1)+fib3(n-2)
print(fib3(5))

#练习  杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
def triangles(n):
    L=[1]
    x=0
    while x<n:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(x)]+[1]
        x=x+1
results=[]
for m in triangles(10):
    results.append(m)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


