#类的基本使用和继承
class car():
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price

    def printInfo(self):
        print('name:%s,brand:%s,price:%s万' % (self.name,self.brand,self.price))

bbm = car('宝马','bba','30')
bbm.printInfo()

#类的继承
class byd(car):
    def __init__(self,name,brand,price,model):
        super().__init__(name,brand,price)
        self.model = model

    def printModel(self):
        print('我的型号是%s' % (self.model))

bydt = byd('比亚迪','byd','20','byd唐')
bydt.printInfo()
bydt.printModel()