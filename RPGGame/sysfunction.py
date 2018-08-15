'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/15 
@Program  : 系统功能
'''
import sys
import pygame
from pygame.locals import *

from RPGGame.GlobalSetting import GlobalSetting

setting = GlobalSetting()


def close_program():
    pygame.quit()
    sys.exit(0)


def system_menu():
    pass


def start_screen():
    setting.SCREENFACE.fill(setting.COLORDICT['bgcolor'])

    title = setting.INVFONT.render('RPG游戏练习', True, (255, 255, 255), setting.COLORDICT['bgcolor'])
    titleRect = title.get_rect()
    titleRect.top = 100
    titleRect.centerx = int(setting.SCREENWIDTH / 2)

    btStart = setting.INVFONT.render('开始游戏', True, (127, 127, 127))
    btStartRect = btStart.get_rect()
    btStartRect.topleft = 220, 250

    while True:
        setting.SCREENFACE.blit(title, titleRect)
        setting.SCREENFACE.blit(btStart, btStartRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit'
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    return 'exit'
        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if btStartRect.collidepoint(x, y):
            btStart = setting.INVFONT.render('开始游戏', True, (107, 107, 107))
            for event in pressed:
                if event == 1:
                    return 'startgame'


        pygame.display.update()
        setting.FPSCLOCK.tick(30)

def can_move(mapObj, x, y, desc):
    moveX, moveY = desc
    newX, newY = x + moveX, y + moveY
    # 判断需要移动的位置是否是可以移动的类型，如果是，角色就移动到该位置，如果不是，角色就返回原来的坐标，不移动。
    # 随着地图的完善，这个元组，可能要定义为一个变量。
    if mapObj[newY][newX] in ('g', 'w'):
        return newX, newY
    else:
        return x, y
