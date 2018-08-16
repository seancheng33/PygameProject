'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/15
@Program      : 运行游戏的函数
'''
import pygame
from pygame.locals import *
from RPGGame import DrawMap, mapdata
from RPGGame.GlobalSetting import GlobalSetting
from RPGGame.sysfunction import can_move

setting = GlobalSetting()


def run_map(mapList, gameStateObj):
    currentMapName = gameStateObj['map name']
    mapObj = mapList[currentMapName]
    showMenu = False

    while True:
        setting.SCREENFACE.fill(setting.COLORDICT['silver'])

        map = DrawMap.draw_map(mapObj, gameStateObj)
        mapRect = map.get_rect()
        mapRect.left = 0
        mapRect.top = 0
        map = DrawMap.redraw_map(map, gameStateObj)

        setting.SCREENFACE.blit(map, mapRect)
        x, y = gameStateObj['player']

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit'
            elif event.type == KEYDOWN:
                # 控制角色的移动
                if event.key == K_LEFT or event.key == K_a:
                    if x > 0:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DIRECTION['LEFT'])
                elif event.key == K_RIGHT or event.key == K_d:
                    if x < len(mapObj[0])-1:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DIRECTION['RIGHT'])
                elif event.key == K_UP or event.key == K_w:
                    if y > 0:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DIRECTION['UP'])
                elif event.key == K_DOWN or event.key == K_s:
                    if y < len(mapObj)-1:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DIRECTION['DOWN'])
                #
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
        setting.FPSCLOCK.tick(60)