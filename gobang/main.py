"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/1/14
@Program      : 五子棋游戏，目标为实现可以简单的人机对弈。
"""
import pygame
from pygame.locals import *
from gobang.ComputerAI import ai_scan
from gobang.init_var import init_var

from gobang.func import game_win
from gobang.gui import draw_player_icon, draw_chessboard, draw_chess

setting = init_var()


def game_play(screen, chess_array, tip_font, iswin, isblack):
    # 绘制出游戏中的各棋子位置
    for col in range(setting.COL):
        for row in range(setting.ROW):
            if chess_array[row][col] == 'black':
                draw_chess(screen, setting.BLACK, row * 35 + 150, col * 35 + 55)
            elif chess_array[row][col] == 'white':
                draw_chess(screen, setting.WHITE, row * 35 + 150, col * 35 + 55)

    # 游戏关闭的控制，关闭窗口和按ESC键即可退出
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            exit(0)
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                quit()
                exit(0)

    # 获取游戏的坐标和按键事件
    mouseX, mouseY = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    # 根据鼠标的坐标计算出对应于数组中的位置
    row = (mouseX - 150 - 15) // 35 + 1
    col = (mouseY - 55 - 15) // 35 + 1

    for press in pressed:
        if press == 1:  # 点击左键的鼠标事件
            # row和col必须是在0~14之间，不然就会报列表越界异常。
            if not iswin and -1 < row < 15 and -1 < col < 15 and chess_array[row][col] == None:
                if isblack:
                    # 设定黑子在数组中的数值为1
                    chess_array[row][col] = 'black'
                    if game_win(chess_array, 'black'):
                        win_str = '黑子 胜!'
                        iswin = True
                    isblack = False
                # else:
                #     # 设定白子在数组中的数值为2
                #     chess_array[row][col] = 'white'
                #     if game_win(chess_array, 'white'):
                #         win_str = '白子 胜!'
                #         iswin = True
                #     isblack = True

        if not iswin and not isblack:
            x, y = ai_scan(chess_array)
            # 设定白子在数组中的数值为2
            chess_array[x][y] = 'white'
            if game_win(chess_array, 'white'):
                win_str = '白子 胜!'
                iswin = True
            isblack = True

        if isblack:
            tip_str = tip_font.render('当前落子为黑子', True, setting.BLACK)
        else:
            tip_str = tip_font.render('当前落子为白子', True, setting.BLACK)

        tip_rect = tip_str.get_rect()
        tip_rect.top = 15
        tip_rect.centerx = 400
        screen.blit(tip_str, tip_rect)


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

        game_play(screen, chess_array, tip_font, iswin, isblack)


        pygame.time.Clock().tick(150)
        pygame.display.update()


if __name__ == '__main__':
    main()
