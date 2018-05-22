#字典是无序的,key只能是不可变对象,查询速度快,占用空间大
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

d['Bob'] = 60
print(d)
print(d.get('Jack',-1))
d.pop('Bob')
print(d)
if 'Tracy' in d:
    print(d['Tracy'])

#集合是无序的,没有value,key不可以重复,key只能是不可变对象
s = set([1,2,3,3])
s.add(4)
print(s)
s.remove(4)
print(s)
s1 = set([1,2,3])
s2 = set([2,3,4])
#交集
print(s1 & s2)
#并集
print(s1 | s2)

#没问题,元组中不包含可变对象
s= set([(1,3),4,5])
#报错,元组中包含列表,列表是可变对象
s= set([(1,3,[1,2]),4,5])



