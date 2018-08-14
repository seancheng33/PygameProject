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

def startscreen():
    setting.SCREENFACE.fill(setting.COLORDICT['bgcolor'])

    title = setting.INVFONT.render('RPG游戏练习', True, (255, 255, 255), setting.COLORDICT['bgcolor'])
    titleRect = title.get_rect()
    titleRect.top = 100
    titleRect.centerx = int(setting.SCREENWIDTH / 2)


    while True:
        setting.SCREENFACE.blit(title, titleRect)
        pygame.draw.rect(setting.SCREENFACE,(0,125,0),(220, 250, 120,50))
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit'
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    return 'exit'
            elif event.type == MOUSEBUTTONUP:
                if 220 < x < 340 and 250 < y < 300:
                    return 'startgame'
        x, y = pygame.mouse.get_pos()

        if 220 < x < 340 and 250 < y < 300:
            pygame.draw.rect(setting.SCREENFACE, (0, 125, 125), (220, 250, 120, 50))

        pygame.display.update()
        setting.FPSCLOCK.tick()