#类和实例
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printInfo(self):
        print('name:%s,age:%s' % (self.name,self.age))

t1=Student('Jack',18)
t1.printInfo()
t2=Student('Rose',19)
t2.printInfo()
t2.city='beijing'
print(t2.city)

#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同