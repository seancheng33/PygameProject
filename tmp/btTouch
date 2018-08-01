'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/31
@Program      : pygame联系，创建一个按键，当鼠标出现在按键上面的时候，按键随机出现在其他的地方
'''
import random
import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('永远按不到的按键')
CLOCK = pygame.time.Clock()

positionx = 200
positiony = 300

bt_rect = pygame.Rect(0, 0, 200, 60)

while True:
    screen.fill((0, 0, 0))

    bt_rect.topleft = (positionx, positiony)
    pygame.draw.rect(screen, (0, 125, 0), bt_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x, y = pygame.mouse.get_pos()

    if bt_rect.collidepoint(x, y):
        positionx = random.randint(0, 600)
        positiony = random.randint(0, 540)

    pygame.display.update()
    CLOCK.tick(30)
