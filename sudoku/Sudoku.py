'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/11/3
@Program      : 数独游戏的主入口
'''
import pygame
from pygame import *

from sudoku.SetVar import SetVar
from sudoku.game_draw import draw_gameArray, draw_background


def main():

    setting = SetVar()

    pygame.init()
    screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT))
    pygame.display.set_caption('数独游戏 —— 基于PyGame的实现 version 0.11')

    gameArray = setting.game_data_load()
    # print(gameArray)
    # 被选择的点的数组
    selectedArray = [[0 for j in range(len(gameArray[i]))] for i in range(len(gameArray))]
    # print(selectedArray)
    while True:
        # 关闭游戏
        setting.terminal_window()
        draw_background(screen)

        draw_gameArray(screen, gameArray, selectedArray)

        pygame.time.Clock().tick(30)
        pygame.display.update()


if __name__ == '__main__':
    main()