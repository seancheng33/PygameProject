"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/6/30
@Program      : 游戏的初始化数值模块
"""

class init_var:
    def __init__(self):
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0
        self.ORANGE = 255, 165, 0
        self.GRAY = 127, 127, 127
        self.RED = 255, 0, 0

        self.ROW = 15
        self.COL = 15

        self.WINFONT = 'c:/windows/Fonts/SimHei.ttf'
        self.MACFONT = '/System/Library/Fonts/STHeiti Light.ttc'
        self.LINUXFONT = '/usr/share/fonts/'

        self.WHITEFIRST = True
