'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/11/3
@Program      : 常用的一些变量
'''
import sys

import pygame


class SetVar():
    def __init__(self):
        self.SCREEN_WIDTH = 900
        self.SCREEN_HEIGHT = 600
        self.TILE_SIZE = 60
        self.TILE_DRAW_SIZE = 48
        # 颜色词典
        self.COLOR_DICT = {'white': (255, 255, 255),  # 白色
                           'ivory': (255, 255, 240),  # 象牙色
                           'yellow': (255, 255, 0),  # 黄色
                           'seashell': (255, 245, 238),  # 海贝色
                           'bisque': (255, 228, 196),  # 橘黄色
                           'gold': (255, 215, 0),  # 金色
                           'pink': (255, 192, 203),  # 粉红色
                           'lightpink': (255, 182, 193),  # 亮粉红色
                           'orange': (255, 165, 0),  # 橙色
                           'coral': (255, 127, 80),  # 珊瑚色
                           'tomato': (255, 99, 71),  # 番茄色
                           'magenta': (255, 0, 255),  # 洋红色
                           'wheat': (245, 222, 179),  # 小麦色
                           'violet': (238, 130, 238),  # 紫罗兰色
                           'silver': (192, 192, 192),  # 银白色
                           'brown': (165, 42, 42),  # 棕色
                           'gray': (128, 128, 128),  # 灰色
                           'olive': (128, 128, 0),  # 橄榄色
                           'purple': (128, 0, 128),  # 紫色
                           'turquoise': (64, 224, 208),  # 绿宝石色
                           'seagreen': (46, 139, 87),  # 海洋绿色
                           'cyan': (0, 255, 255),  # 青色
                           'green': (0, 128, 0),  # 纯绿色
                           'blue': (0, 0, 255),  # 纯蓝色
                           'darkblue': (0, 0, 139),  # 深蓝色
                           'navy': (0, 0, 128),  # 海军蓝色
                           'black': (0, 0, 0),  # 纯黑色
                           }

        # 元素的数字颜色
        self.NUM_COLOR_DICT = {'1': self.COLOR_DICT['gray'], '2': self.COLOR_DICT['brown'],
                               '3': self.COLOR_DICT['violet'], '4': self.COLOR_DICT['wheat'],
                               '5': self.COLOR_DICT['coral'], '6': self.COLOR_DICT['turquoise'],
                               '7': self.COLOR_DICT['navy'], '8': self.COLOR_DICT['olive'],
                               '9': self.COLOR_DICT['purple']}

        pygame.init()

        # 指定字体的路径，以下方法仅在window下有效
        # 后续再考虑如何判断该路径在mac和linux下显示不同的系统字体，理论很简单，用sys.version即可判断是windows还是linux，还是mac
        self.FONTPATH = 'c:/windows/Fonts/SimHei.ttf'
        self.TITLEFONT = pygame.font.Font(self.FONTPATH, 48)  # 游戏标题用的字体大小
        self.TEXTFONT = pygame.font.Font(self.FONTPATH, 24)  # 一般文字用的字体大小
        self.TILEFONT = pygame.font.Font(self.FONTPATH, 36)  # 贴片元素用的字体大小



    # 关闭游戏函数，监控关闭窗口
    def terminal_window(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

    def game_data_load(self):
        data = []
        with open('gamedata.txt', 'r', encoding='utf-8') as load_file:
            tmp_data = load_file.read().split('\n')
            for i in tmp_data:
                data.append(i.split(','))

        return data

