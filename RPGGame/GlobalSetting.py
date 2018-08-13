'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/15 
@Program  : 全局变量
'''
import pygame


class GlobalSetting:
    def __init__(self):
        self.TILESIZE = 32
        self.TILEWIDTH = 24
        self.TILEHEIGHT = 20

        self.SCREENWIDTH = self.TILESIZE * self.TILEWIDTH
        self.SCREENHEIGHT = self.TILESIZE * self.TILEHEIGHT

        self.COLORDICT = {'bgcolor': (0, 140, 140)}

        self.IMAGESDICT = {
                        'coal': pygame.image.load('img/coal.png'),
                        'dirt': pygame.image.load('img/dirt.png'),
                        'grass': pygame.image.load('img/grass.png'),
                        'lava': pygame.image.load('img/lava.png'),
                        'sand': pygame.image.load('img/sand.png'),
                        'stone': pygame.image.load('img/stone.png'),
                        'water': pygame.image.load('img/water.png')}

        self.TILEMAPPING = {'c': self.IMAGESDICT['coal'],
                            'd': self.IMAGESDICT['dirt'],
                            'g': self.IMAGESDICT['grass'],
                            'l': self.IMAGESDICT['lava'],
                            's': self.IMAGESDICT['sand'],
                            '*': self.IMAGESDICT['stone'],
                            'w': self.IMAGESDICT['water']}

        pygame.init()
        self.font_path = 'c:\\Windows\\Fonts\\SimHei.ttf'
        self.INVFONT = pygame.font.Font(self.font_path, 48)
        self.SCREENFACE = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.set_caption('RPG大的地图移动的Demo')

        self.FPSCLOCK = pygame.time.Clock()
