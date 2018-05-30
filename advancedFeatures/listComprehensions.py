#列表生成式
import os
L=list(range(1,11))
print(L)
L=[x*x for x in range(1,11)]
print(L)
#添加条件判断
L=[x*x for x in range(1,11) if x%2==0]
print(L)
#两层循环
L=[m+n for m in 'abc' for n in 'xyz']
print(L)
L=[f for f in os.listdir('.')]
print(L)
#利用字典生成列表
d={'name':'Jack','gender':'M','city':'beijing'}
L=[x+':'+y for x,y in d.items()]
print(L)
L=[x.lower() for x in ['PHP','PYTHON','GO']]
print(L)
#练习
L1=['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)


