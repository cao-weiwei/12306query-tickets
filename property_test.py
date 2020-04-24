class Screen(object):
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        

    def get_width(self):
         return self._width

    def set_width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self._width = value
    
    def get_height(self):
        return self._height
    
    def set_height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

    width = property(get_width, set_width)
    height = property(get_height, set_height)

if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
