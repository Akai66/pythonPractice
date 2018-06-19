from collections import deque,defaultdict,OrderedDict,Counter
#deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
dq=deque(['c','d','e'])
dq.append('f')
print(dq)
dq.appendleft('b')
print(dq)
dq.appendleft('a')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)

#defaultdict 可以设置默认值的dict
dd=defaultdict(lambda :'N/A')
dd['key1']='test'
print(dd['key2'])

#OrderedDict 保持key顺序的dict,
od=OrderedDict()
od['z']=1
od['y']=2
od['x']=3
print(list(od.keys()))

#Counter  统计字符出现的个数
c=Counter()
for x in 'programming':
    c[x] = c[x] + 1
print(c)


