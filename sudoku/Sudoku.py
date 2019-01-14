'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/11/3
@Program      : 数独游戏的主入口
'''
import pygame
from pygame import *
from sudoku.SetVar import SetVar
from sudoku.game_draw import draw_gameArray, draw_background, draw_seletced, setting


def main():
    global gameArray, selectedArray
    setting = SetVar()

    pygame.init()
    screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT))
    pygame.display.set_caption('数独游戏 —— 基于PyGame的实现 version 0.12')

    gameArray = setting.game_data_load()
    selectedArray = setting.selectedArray
    # print(gameArray)

    while True:
        # 关闭游戏
        setting.terminal_window()
        draw_background(screen)
        draw_gameArray(screen, gameArray)
        draw_seletced(screen)

        pygame.time.Clock().tick(30)
        pygame.display.update()


if __name__ == '__main__':
    main()