'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/18
@Program      : 联系用pygame制作一个2048的游戏，
'''

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('2048')

while True:

    screen.fill((127, 89, 127))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)



    pygame.display.update()