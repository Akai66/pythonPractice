#内建的filter()函数用于过滤序列
#过滤偶数
def is_odd(n):
    return n%2!=0
print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))

#去除None或者空字符串
def is_not_empty(s):
    return s and s.strip()
print(list(filter(is_not_empty,['A', '', 'B', None, 'C', '  '])))

#埃氏筛法计算素数
def odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def is_not_divisible(n):
    #将匿名函数作为返回值返回
    return lambda x:x%n!=0
def primes():
    yield 2
    it=odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(is_not_divisible(n),it)
for x in primes():
    if x < 100:
        print(x)
    else:
        break

#练习 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    s=str(n)
    return s==s[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')