#json
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
print(json.loads(json.dumps(d)))

#格式化类
class Student(object):
    def __init__(self, name, age, score):
        self.name=name
        self.age=age
        self.score=score

    def __str__(self):
        return 'name:%s,age:%s,score:%s' % (self.name,self.age,self.score)

s=Student('Jack',18,90)
def std2dict(std):
    return {'name':std.name,'age':std.age,'score':std.score}
print(json.dumps(s,default=std2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2std(d):
    return Student(d['name'],d['age'],d['score'])
str='{"name": "Jack", "age": 18, "score": 90}'
s=json.loads(str,object_hook=dict2std)
print(s)


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
