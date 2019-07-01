"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/1/14
@Program      : 五子棋游戏，目标为实现可以简单的人机对弈。
"""
import pygame

from gobang.init_var import init_var

from gobang.func import game_play
from gobang.gui import draw_player_icon, draw_chessboard

setting = init_var()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('五子棋(GoBang) version 0.26 --Program by Sean Cheng')
    pygame.display.set_icon(pygame.image.load('img/TitleIcon.png'))

    title_bg_img = pygame.image.load('img/title.png')

    FONTPATH = setting.WINFONT
    win_font = pygame.font.Font(FONTPATH, 120)
    tip_font = pygame.font.Font(FONTPATH, 24)
    win_str = None

    chess_array = [[None for i in range(setting.COL)] for j in range(setting.ROW)]  # 存储棋子的状态
    isblack = True  # 当前是否为黑子下，这个判断条件有多种用途，用在判断现在是谁落子，以及谁落子后获得了胜利。
    iswin = False

    result = 'title'

    while True:
        screen.fill(setting.ORANGE)  # 绘制背景的颜色

        # if result == 'title':
        #     title(screen, title_bg_img)
        # elif result == 'play':
        draw_player_icon(screen)
        draw_chessboard(screen)

        game_play(screen, chess_array, win_font, tip_font, iswin, isblack)

        pygame.time.Clock().tick(150)
        pygame.display.update()


if __name__ == '__main__':
    main()
