'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/15
@Program      : 游戏的主入口
'''
import pygame

pygame.init()
SCREEN = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('RPG游戏的测试demo')

IMAGEDICTS = {'road': pygame.image.load('img/city/road01.png'),
              'grass': pygame.image.load('img/city/grass01.png'),
              'seawall': pygame.image.load('img/city/seawall01.png'),
              'sea': pygame.image.load('img/city/sea.png'),
              }

while True:



    pygame.display.update()
