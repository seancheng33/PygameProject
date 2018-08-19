'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/18
@Program      : 联系用pygame制作一个2048的游戏，
'''

import pygame
import sys

initArray = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # 初始化的游戏数组

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2048')

while True:

    screen.fill((128, 128, 0))

    # 五条横线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (500, 100), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 200), (500, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 300), (500, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 400), (500, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 500), (500, 500), 2)

    # 五条竖线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (100, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (200, 100), (200, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (300, 100), (300, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (400, 100), (400, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (500, 100), (500, 500), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

    pygame.display.update()
