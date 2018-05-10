#函数的使用
#Python 中一切皆为对象，数字是对象，列表是对象，函数也是对象，任何东西都是对象。而变量是对象的一个引用（又称为名字或者标签），对象的操作都是通过引用来完成的
#如果需要传递副本,可以test = onelist[:]
#函数中，参数的传递本质上是一种赋值操作，而赋值操作是一种名字到对象的绑定过程
testlist = [1,2,3,4]
def double(onelist):
    onelist[0] = 3
    onelist = [3,3,3]
    print(onelist)
double(testlist)
print(testlist)


