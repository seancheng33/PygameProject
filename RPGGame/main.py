'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/14 
@Program  : 练习rpg的游戏，这个是主入口文件。
'''
import pygame
from pygame.locals import *

import DrawMap
import mapdata
from GlobalSetting import GlobalSetting
from sysfunction import close_program


def startscreen():
    setting.SCREENFACE.fill(setting.COLORDICT['bgcolor'])

    title = setting.INVFONT.render('中文的标题', True, (255, 255, 255), setting.COLORDICT['bgcolor'])
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


def run_map(mapList, gameStateObj):
    global currentMapName

    currentMapName = gameStateObj['map name']
    mapObj = mapList[currentMapName]
    showMenu = False

    while True:
        setting.SCREENFACE.fill(setting.COLORDICT['bgcolor'])

        map = DrawMap.draw_map(mapObj, gameStateObj)
        mapRect = map.get_rect()
        mapRect.left = 0
        mapRect.top = 0
        map = DrawMap.redraw_map(map, gameStateObj)

        setting.SCREENFACE.blit(map, mapRect)
        x, y = gameStateObj['player']

        # role = pygame.image.load('img/horngirl.png')
        # role_rect = pygame.Rect(x * setting.TILESIZE, y * setting.TILESIZE, setting.TILESIZE, setting.TILESIZE)
        # setting.SCREENFACE.blit(role, role_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit'
            elif event.type == KEYDOWN:
                # 控制角色的移动
                if event.key == K_LEFT:
                    if x > 0:
                        gameStateObj['player'] = (x - 1, y)
                elif event.key == K_RIGHT:
                    if x < len(mapObj[0])-1:
                        gameStateObj['player'] = (x + 1, y)
                elif event.key == K_UP:
                    if y > 0:
                        gameStateObj['player'] = (x, y - 1)
                elif event.key == K_DOWN:
                    if y < len(mapObj)-1:
                        gameStateObj['player'] = (x, y + 1)

                # elif event.key == K_m:
                #     if not showMenu:
                #         showMenu = True
                #         show_menu()
                #     else:
                #         showMenu = False

                elif event.key == K_ESCAPE:
                    return 'exit'
                elif event.key == K_BACKSPACE:
                    return 'title'

        for item in mapdata.inter_postion[currentMapName].items():
            if (x, y) == item[1]:
                currentMapName = item[0][2:]
                gameStateObj['map name'] = currentMapName
                gameStateObj['player'] = mapdata.role_postion[currentMapName]
                mapObj = mapList[currentMapName]

        pygame.display.update()
        setting.FPSCLOCK.tick()


def main():
    global setting, mapList, gameStateObj
    setting = GlobalSetting()

    mapList = {'base': mapdata.mapBase, 'sea': mapdata.mapSea}

    gameStateObj = {
        'player': mapdata.role_postion['base'],
        'map name': 'base',
    }

    setting.SCREENFACE.fill(setting.COLORDICT['bgcolor'])
    result = startscreen()
    while True:
        if result == 'exit':
            # 收到返回的结果是exit的话，就关闭整个程序
            close_program()
        elif result == 'title':
            # 收到返回的结果是title的话，就返回到title界面
            result = startscreen()
        elif result == 'startgame':
            # 收到返回的结果是startgame的话，就开始新游戏
            result = run_map(mapList, gameStateObj)

        pygame.display.update()
        setting.FPSCLOCK.tick()


if __name__ == '__main__':
    main()
