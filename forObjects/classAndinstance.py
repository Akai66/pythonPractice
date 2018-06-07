#类和实例
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getInfo(self):
        print('name:%s,age:%s' % (self.name,self.age))

t1=Student()