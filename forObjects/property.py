#property装饰器的运用
class Screen(object):

    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        if value<1000 or value>2000:
            raise ValueError('width must between 1000 ~ 2000!')
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an integer!')
        if value<500 or value>1000:
            raise ValueError('height must between 500 ~ 1000!')
        self._height=value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen(3000,560) #初始化的时候,setter里面的判断无效
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


