#使用__slots__
#如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
class Student(object):
    __slots__=('name','age')

t=Student()
t.name='小明'
print(t.name)
t.age=18
#t.city='beijing'  报错,因为定义了__slots__,只允许对Student实例添加name和age属性