"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/4/12
@Program      : 游戏开始的选择界面。显示游戏的标题，开始选项，接收选项。
"""
import pygame
from pygame.locals import *
from gui import draw_chess
from init_var import init_var
from ComputerAI import ai_scan

setting = init_var()

def title(screen, image):
    while True:
        # 添加背景色
        # screen.fill()
        # 添加背景图片
        screen.blit(image, (0, 0))

        return 'play'

def game_play(screen,chess_array,win_font,tip_font):
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

    # 如果游戏胜利，就显示胜利的画面
    if iswin:
        winstr = win_font.render(win_str, True, setting.RED)
        winstrRect = winstr.get_rect()
        winstrRect.center = 400, 300
        screen.blit(winstr, winstrRect)

    if isblack:
        tip_str = tip_font.render('当前落子为黑子', True, setting.BLACK)
    else:
        tip_str = tip_font.render('当前落子为白子', True, setting.BLACK)
    tip_rect = tip_str.get_rect()
    tip_rect.top = 15
    tip_rect.centerx = 400
    screen.blit(tip_str, tip_rect)


def game_win(chess_array, chessColor):
    # 方向横(-)的检查
    for x in range(setting.ROW):
        for y in range(setting.COL - 4):
            if chess_array[x][y] == chessColor and chess_array[x][y + 1] == chessColor and chess_array[x][y + 2] == \
                    chessColor and chess_array[x][y + 3] == chessColor and chess_array[x][y + 4] == chessColor:
                return True
    # 方向竖(-)的检查
    for x in range(setting.ROW - 4):
        for y in range(setting.COL):
            if chess_array[x][y] == chessColor and chess_array[x + 1][y] == chessColor and chess_array[x + 2][y] == \
                    chessColor and chess_array[x + 3][y] == chessColor and chess_array[x + 4][y] == chessColor:
                return True
    # 方向斜(/)的检查
    for x in range(setting.ROW - 4):
        for y in range(4, setting.COL):
            if chess_array[x][y] == chessColor and chess_array[x + 1][y - 1] == chessColor and \
                    chess_array[x + 2][y - 2] == chessColor and chess_array[x + 3][y - 3] == chessColor and \
                    chess_array[x + 4][y - 4] == chessColor:
                return True
    # 方向斜(\)的检查
    for x in range(setting.ROW - 4):
        for y in range(setting.COL - 4):
            if chess_array[x][y] == chessColor and chess_array[x + 1][y + 1] == chessColor and \
                    chess_array[x + 2][y + 2] == chessColor and chess_array[x + 3][y + 3] == chessColor and \
                    chess_array[x + 4][y + 4] == chessColor:
                return True

    return False