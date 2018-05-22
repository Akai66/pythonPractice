birth = input('birth:')
birth = int(birth)
if birth > 2000:
    print('00 后')
else:
    print('00 前')

h = 1.76
w = 78.5
bmi = w / pow(h,2)
print(bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else :
    print('过轻')


