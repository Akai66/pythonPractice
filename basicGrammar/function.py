#函数的使用
#Python 中一切皆为对象，数字是对象，列表是对象，函数也是对象，任何东西都是对象。而变量是对象的一个引用（又称为名字或者标签），对象的操作都是通过引用来完成的
#如果需要传递副本,可以test = onelist[:]
#函数中，参数的传递本质上是一种赋值操作，而赋值操作是一种名字到对象的绑定过程
import math
testlist = [1,2,3,4]
def double(onelist):
    onelist[0] = 3
    onelist = [3,3,3]
    print(onelist)
double(testlist)
print(testlist)

n1 = 255
print(str(hex(n1)))
n2 = 1000
print(str(hex(n2)))

#校验参数类型
def myabs(num):
    if not isinstance(num,(int,float)):
        raise TypeError('bad arg type,please input int or float')
    if num > 0:
        return num
    else:
        return -num

print(myabs(19))

#多个返回值  函数可以同时返回多个值，但其实就是一个tuple
def move(x,y,step,angle=0):
    x = x + step * math.cos(angle)
    y = y - step * math.sin(angle)
    return x,y

x,y=move(100,100,30,math.pi/6)
print(x,y)

#计算二元一次方程的解  ax2 + bx + c = 0
def quadratic(a,b,c):
    args = [a,b,c]
    #先校验参数
    for arg in args:
        if not isinstance(arg,(int,float)):
            raise TypeError('bad arg type,please input int or float')
    #判断是否有解
    if pow(b,2)-4*a*c < 0:
        return '无解'
    x1 = (-b+math.sqrt(pow(b,2)-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(pow(b,2)-4*a*c))/(2*a)
    return x1,x2

print(quadratic(1,1,-2))


#默认参数必须指向不变对象,否则连续调用会出现大坑
def addEnd(L=[]):
    L.append('end')
    return L
print(addEnd())    #结果 ['end']
print(addEnd())    #结果 ['end', 'end']

def addEnd2(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print(addEnd2())   #结果 ['end']
print(addEnd2())   #结果 ['end']

def mypow(x,y=2):
    ret = 1
    n = 0
    while n < y:
        ret = ret * x
        n +=1
    return ret
print(mypow(3))


#可变参数  可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + mypow(n)
    return sum
print(calc(1,2,3))
print(calc(1,2))
L = [1,2,3,4]
print(calc(*L))

#关键字参数
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack',18)
person('Jack',18,gender='m')
person('Jack',18,gender='m',city='beijing')
otherkw = {'job':'php','city':'beijing'}
person('Jack',18,**otherkw)

#命名关键字参数
def person2(name,age,*,job,city):
    print('name:', name, 'age:', age, 'other:','job:',job,'city:',city)
person2('Rose',20,job='js',city='beijing')

#带默认值
def person3(name,age,*,job='c++',city):
    print('name:', name, 'age:', age, 'other:','job:',job,'city:',city)
person3('Rose',20,city='hangzhou')

#练习
def product(*numbers):
    if len(numbers) <= 0:
        raise TypeError('bad arg type,please input int or float')
    for n in numbers:
        if not isinstance(n,(int,float)):
            raise TypeError('bad arg type,please input int or float')
    ret = 1
    for n in numbers:
        ret = ret * n
    return ret
print(product(5,6,7,8))









