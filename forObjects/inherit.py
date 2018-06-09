#继承和多态
class Animal(object):
    def run(self):
        print('animal is run')

class Dog(object):
    def run(self):
        print('dog is run')

a=Animal()
d=Dog()
def doRun(animal):
    animal.run()
doRun(a)
doRun(d)
