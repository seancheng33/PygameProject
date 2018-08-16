'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/15 
@Program  : 全局变量
'''
import pygame

# from RPGGame import ImageLoad


class GlobalSetting:
    def __init__(self):
        self.TILESIZE = 32  # 每个的大小
        self.TILEWIDTH = 25  # 屏幕宽度的格数
        self.TILEHEIGHT = 21  # 屏幕高度的格数

        self.SCREENWIDTH = self.TILESIZE * self.TILEWIDTH
        self.SCREENHEIGHT = self.TILESIZE * self.TILEHEIGHT

        self.COLORDICT = {'bgcolor': (0, 140, 140),
                          'white': (255, 255, 255),
                          }

        # self.IMAGESDICT = {
        #                 'coal': pygame.image.load('img/coal.png'),
        #                 'dirt': pygame.image.load('img/dirt.png'),
        #                 'grass': pygame.image.load('img/grass.png'),
        #                 'lava': pygame.image.load('img/lava.png'),
        #                 'sand': pygame.image.load('img/sand.png'),
        #                 'stone': pygame.image.load('img/stone.png'),
        #                 'water': pygame.image.load('img/water.png')}
        #
        # self.TILEMAPPING = {'c': self.IMAGESDICT['coal'],
        #                     'd': self.IMAGESDICT['dirt'],
        #                     'g': self.IMAGESDICT['grass'],
        #                     'l': self.IMAGESDICT['lava'],
        #                     's': self.IMAGESDICT['sand'],
        #                     '*': self.IMAGESDICT['stone'],
        #                     'w': self.IMAGESDICT['water']}


        self.DESC = {'UP': (0, -1), 'RIGHT': (1, 0), 'DOWN': (0, 1), 'LEFT': (-1, 0)}

        pygame.init()
        self.font_path = 'c:\\Windows\\Fonts\\SimHei.ttf'
        self.INVFONT = pygame.font.Font(self.font_path, 48)
        self.SCREENFACE = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.set_caption('RPG大的地图移动的Demo version: 0.11')

        self.FPSCLOCK = pygame.time.Clock()

        self.TILEMAPPING = self.image_load()

        # {'c': imgdict['x3y2'], 'd': imgdict['x2y2'], 'g': imgdict['x0y2'], 'l': imgdict['x0y2'],
        #                     's': imgdict['x1y2'], '*': imgdict['x2y7'], 'w': imgdict['x0y2']}

    def image_load(self):
        bgimg = pygame.image.load('img/background.png').convert_alpha()  # 这张图片是8列16行

        imgwidth = 8
        imgheight = 16

        imgdict = {}

        for imgx in range(imgwidth):
            for imgy in range(imgheight):
                imgname = 'x' + str(imgx) + 'y' + str(imgy)
                imgdict[imgname] = bgimg.subsurface(imgx * 32, imgy * 32, 32, 32)

        return imgdict