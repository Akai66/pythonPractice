
' 一个标准的自定义模块 '
__author__='liukai'
import sys
from functools import reduce
def _getOdd(n):
    return list(filter(lambda x:x%2!=0,range(1,n+1)))
def getOddSum():
    args=sys.argv
    if len(args)<2:
        print('args error')
        args.append(5)
    L=_getOdd(int(args[1]))
    return reduce(lambda x,y:x+y,L)
if __name__ == '__main__':
    print(getOddSum())