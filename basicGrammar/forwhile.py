sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 100
while n > 0:
    sum += n
    n -= 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello, %s!' % name)

n = 1
while n <= 100:
    if(n>10):
        break
    print(n)
    n += 1

n=11
while n>0:
    n -= 1
    if n%2==0:
        continue
    print(n)
print('end')

