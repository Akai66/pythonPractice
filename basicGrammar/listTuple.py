#列表和元组
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[1])
print(classmates[-1])

classmates.append('Jack')
classmates.insert(3,'Rose')
print(classmates)
print(len(classmates))

classmates[4] = 'Kimi'
print(classmates)

classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)

#元组,"指向不变"
t = ('a','b',['c','d'])
t[2][0] = 'C'
print(t)


#二维列表
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
