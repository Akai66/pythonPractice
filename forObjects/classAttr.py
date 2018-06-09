#类属性
#实例属性属于各个实例所有，互不干扰；
#类属性属于类所有，所有实例共享一个属性；
#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误
class Student(object):
    #类属性
    count=0

    def __init__(self,name):
        self.name=name
        Student.count = self.count + 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

