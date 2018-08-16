'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/15 
@Program  : 全局变量
'''
import pygame


class GlobalSetting:
    def __init__(self):
        self.TILESIZE = 32  # 每个的大小
        self.TILEWIDTH = 25  # 屏幕宽度的格数
        self.TILEHEIGHT = 21  # 屏幕高度的格数

        self.SCREENWIDTH = self.TILESIZE * self.TILEWIDTH
        self.SCREENHEIGHT = self.TILESIZE * self.TILEHEIGHT

        self.COLORDICT = {'white': (255, 255, 255),  # 白色
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

        self.DESC = {'UP': (0, -1), 'RIGHT': (1, 0), 'DOWN': (0, 1), 'LEFT': (-1, 0)}

        pygame.init()
        self.font_path = 'c:\\Windows\\Fonts\\SimHei.ttf'
        self.INVFONT = pygame.font.Font(self.font_path, 48)
        self.SCREENFACE = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.set_caption('RPG大的地图移动的Demo version: 0.15')

        self.FPSCLOCK = pygame.time.Clock()

        self.TILEMAPPING = self.image_load()

    def image_load(self, filename='img/background.png'):
        bgimg = pygame.image.load(filename).convert_alpha()  # 这张图片是24列38行

        imgwidth = 24
        imgheight = 38

        imgdict = {}

        for imgx in range(imgwidth):
            for imgy in range(imgheight):
                imgname = 'x' + str(imgx) + 'y' + str(imgy)
                imgdict[imgname] = bgimg.subsurface(imgx * self.TILESIZE, imgy * self.TILESIZE, self.TILESIZE,
                                                    self.TILESIZE)

        return imgdict
