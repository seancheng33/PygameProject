'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/31
@Program      : 
'''
import sys

import pygame


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('测试移动的按键')
CLOCK = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update()
    CLOCK.tick(30)