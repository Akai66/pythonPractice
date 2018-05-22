#关于编码问题   python中的字符串默认都是Unicode编码
print(ord('A'))
print(ord('刘'))
print(ord('胡'))
print(chr(65))
print(chr(21016))
print(chr(32993))

print('abc'.encode('ascii'))
print('abc'.encode('utf-8'))
print(b'abc'.decode('ascii'))
print('篮球'.encode('utf-8'))
print(b'\xe7\xaf\xae\xe7\x90\x83'.decode('utf-8'))

print(len('篮球'))
print(len('篮球'.encode('utf-8')))

print('name:%s,age:%d' % ('jack',27))

lscore = 75
tscore = 85
grate = (tscore - lscore) / lscore * 100
print('%s growth rate is %.1f%%' % ('jack',grate))