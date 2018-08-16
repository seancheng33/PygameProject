'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/14 
@Program  : 练习rpg的游戏，这个是主入口文件。
'''
import pygame
from RPGGame import mapdata
from RPGGame.GlobalSetting import GlobalSetting
from RPGGame.RunGame import run_map
from RPGGame.sysfunction import close_program, start_screen, can_move

setting = GlobalSetting()


def main():
    mapList = {'base': mapdata.mapBase, 'sea': mapdata.mapSea}

    gameStateObj = {
        'player': mapdata.role_postion['base'],
        'map name': 'base',
    }
    # print(ImageLoad.imgdict)
    setting.SCREENFACE.fill(setting.COLORDICT['silver'])
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
