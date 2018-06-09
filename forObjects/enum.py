from enum import Enum,unique

# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

Gender=Enum('Gender',('Male','Female'))
for name,member in Gender.__members__.items():
    print(name,member,member.value)
print(Gender['Male'])
print(Gender['Male'].value)
print(Gender.Male)
print(Gender.Male.value)
print(Gender(1))
print(Gender(1).value)
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')