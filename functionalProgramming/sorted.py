#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
#默认由小到大排序
print(sorted([36, 5, -12, 9, -21]))
#反转
print(sorted([36, 5, -12, 9, -21],reverse=True))
#指定按某种计算方法排序
print(sorted([36, 5, -12, 9, -21],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))
#练习 请用sorted()对下面列表按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda x:x[0].lower()))
#按成绩从高到低排序
print(sorted(L,key=lambda x:x[1],reverse=True))