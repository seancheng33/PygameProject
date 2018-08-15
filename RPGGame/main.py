'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/14 
@Program  : 练习rpg的游戏，这个是主入口文件。
'''
import pygame
from pygame.locals import *

from RPGGame import DrawMap, mapdata
from RPGGame.GlobalSetting import GlobalSetting
from RPGGame.sysfunction import close_program, start_screen, can_move

setting = GlobalSetting()

def run_map(mapList, gameStateObj):
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

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit'
            elif event.type == KEYDOWN:
                # 控制角色的移动
                if event.key == K_LEFT or event.key == K_a:
                    if x > 0:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DESC['LEFT'])
                        # gameStateObj['player'] = (x - 1, y)
                elif event.key == K_RIGHT or event.key == K_d:
                    if x < len(mapObj[0])-1:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DESC['RIGHT'])
                        # gameStateObj['player'] = (x + 1, y)
                elif event.key == K_UP or event.key == K_w:
                    if y > 0:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DESC['UP'])
                        # gameStateObj['player'] = (x, y - 1)
                elif event.key == K_DOWN or event.key == K_s:
                    if y < len(mapObj)-1:
                        gameStateObj['player'] = can_move(mapObj, x, y, setting.DESC['DOWN'])
                        # gameStateObj['player'] = (x, y + 1)


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
    mapList = {'base': mapdata.mapBase, 'sea': mapdata.mapSea}

    gameStateObj = {
        'player': mapdata.role_postion['base'],
        'map name': 'base',
    }

    setting.SCREENFACE.fill(setting.COLORDICT['bgcolor'])
    result = start_screen()
    while True:
        if result == 'exit':
            # 收到返回的结果是exit的话，就关闭整个程序
            close_program()
        elif result == 'title':
            # 收到返回的结果是title的话，就返回到title界面
            result = start_screen()
        elif result == 'startgame':
            # 收到返回的结果是startgame的话，就开始新游戏
            result = run_map(mapList, gameStateObj)

        pygame.display.update()
        setting.FPSCLOCK.tick(120)


if __name__ == '__main__':
    main()
