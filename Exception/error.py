#错误,异常处理
from functools import reduce

def str2num(s):
    if s.find('.') > -1:
        ret=float(s)
    else:
        ret=int(s)
    return ret

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('except:',e)


main()


