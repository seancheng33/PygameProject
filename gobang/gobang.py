"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/1/14
@Program      : 五子棋游戏，目标为实现可以简单的人机对弈。
"""
import random
import sys
import pygame
from pygame import *

WHITE = 255, 255, 255
BLACK = 0, 0, 0
ORANGE = 255, 165, 0
GRAY = 127, 127, 127
RED = 255, 0, 0

ROW = 15
COL = 15

WINFONT = 'c:/windows/Fonts/SimHei.ttf'
MACFONT = ''
LINUXFONT = ''


def check_put_point(chess_array, row, col):
    point = [0,0]
    # 如果当前位置不是空白的位置，也就是说，有棋子，这个位置就不用去扫描判断它的分值。分值就直接为0
    if chess_array[row][col] != 0:
        return [0, 0]

    # 循环两次，一次是判断黑子，一次是判断白子，得分为两次相加，因为黑白双方的分数高，也就说明该点的重要性
    for chess in range(1, 3):
        chess_count = 0
        for i in range(5):
            # 需要控制下标越界的问题
            if (col + i) < 15 and chess_array[row][col + i] == chess:
                chess_count += 1
        for i in range(5):
            # 需要控制下标越界的问题
            if (col - i) > -1 and chess_array[row][col - i] == chess:
                chess_count += 1
        # if chess == 1:
        #     point[0] += chess_count
        # else:
        #     point[1] += chess_count
        # 判断横
        # chess_count = 0
        for i in range(5):
            # 需要控制下标越界的问题
            if (row + i) < 15 and chess_array[row + i][col] == chess:
                chess_count += 1
        for i in range(5):
            if (row - i) > -1 and chess_array[row - i][col] == chess:
                chess_count += 1
        # if chess == 1:
        #     point[0] += chess_count
        # else:
        #     point[1] += chess_count
        # 判断左斜
        # chess_count = 0
        for i in range(5):
            # 需要控制下标越界的问题
            if (col + i) < 15 and (row + i) < 15 and chess_array[row + i][col + i] == chess:
                chess_count += 1
        for i in range(5):
            if (col - i) > -1 and (row - i) > -1 and chess_array[row - i][col - i] == chess:
                chess_count += 1
        # if chess == 1:
        #     point[0] += chess_count
        # else:
        #     point[1] += chess_count
        # 判断右斜
        # chess_count = 0
        for i in range(5):
            # 需要控制下标越界的问题
            if (col + i) < 15 and (row - i) > -1 and chess_array[row - i][col + i] == chess:
                chess_count += 1
        for i in range(5):
            if (col - i) > -1 and (row + i) < 15 and chess_array[row + i][col - i] == chess:
                chess_count += 1

        if chess == 1:
            point[0] += chess_count
        else:
            point[1] += chess_count
    return point


def ai_scan(chess_array):
    put_point = [[[0, 0] for _ in range(15)] for _ in range(15)]
    for j in range(15):
        for i in range(15):
            put_point[i][j] = check_put_point(chess_array, i, j)
    print(put_point)

    # return row, col


def draw_chess(screen, chess_color, posx, posy):
    # 绘制棋子，传入的参数包括棋子的颜色和位置
    pygame.draw.circle(screen, chess_color, (posx, posy), 12)


def draw_chessboard(screen):
    # 棋盘最外层的粗线
    pygame.draw.line(screen, BLACK, (150, 55), (640, 55), 4)
    pygame.draw.line(screen, BLACK, (150, 545), (640, 545), 4)
    pygame.draw.line(screen, BLACK, (150, 55), (150, 545), 4)
    pygame.draw.line(screen, BLACK, (640, 55), (640, 545), 4)

    # 棋盘内部的细线
    # 横线
    for i in range(14):
        pygame.draw.line(screen, BLACK, (150, 35 * i + 55), (640, 35 * i + 55), 2)

    # 竖线
    for i in range(14):
        pygame.draw.line(screen, BLACK, (35 * i + 150, 55), (35 * i + 150, 545), 2)

    # 棋盘上的点
    pygame.draw.circle(screen, BLACK, (35 * 3 + 150, 35 * 3 + 55), 6)
    pygame.draw.circle(screen, BLACK, (35 * 3 + 150, 35 * 11 + 55), 6)
    pygame.draw.circle(screen, BLACK, (35 * 7 + 150, 35 * 7 + 55), 6)
    pygame.draw.circle(screen, BLACK, (35 * 11 + 150, 35 * 3 + 55), 6)
    pygame.draw.circle(screen, BLACK, (35 * 11 + 150, 35 * 11 + 55), 6)


def draw_player_icon(screen):
    # 左上角的头像
    pygame.draw.rect(screen, GRAY, (20, 55, 100, 100))
    pygame.draw.circle(screen, BLACK, (70, 105), 40)
    # 右下角的头像
    pygame.draw.rect(screen, GRAY, (670, 445, 100, 100))
    pygame.draw.circle(screen, WHITE, (720, 495), 40)


def game_win(chess_array, row, col):
    # 先获取目前下的棋子位置，然后再判断四个可能有连成一线的方向，如果有一个方向达成5颗棋子或以上的目标，就报游戏胜利。
    chess = chess_array[row][col]

    # 判断竖
    chess_count = 0
    for i in range(4):
        # 需要控制下标越界的问题
        if (col + i) < 15 and chess_array[row][col + i] == chess:
            chess_count += 1
        else:
            break
    for i in range(4):
        # 需要控制下标越界的问题
        if (col - i) > -1 and chess_array[row][col - i] == chess:
            chess_count += 1
        else:
            break
    # 当直线上存在5个相同的颜色的棋子时，判定为胜利
    if chess_count > 5:
        return True

    # 判断横
    chess_count = 0
    for i in range(4):
        # 需要控制下标越界的问题
        if (row + i) < 15 and chess_array[row + i][col] == chess:
            chess_count += 1
        else:
            break
    for i in range(4):
        if (row - i) > -1 and chess_array[row - i][col] == chess:
            chess_count += 1
        else:
            break
    # 当直线上存在5个相同的颜色的棋子时，判定为胜利
    if chess_count > 5:
        return True

    # 判断左斜
    chess_count = 0
    for i in range(4):
        # 需要控制下标越界的问题
        if (col + i) < 15 and (row + i) < 15 and chess_array[row + i][col + i] == chess:
            chess_count += 1
        else:
            break
    for i in range(4):
        if (col - i) > -1 and (row - i) > -1 and chess_array[row - i][col - i] == chess:
            chess_count += 1
        else:
            break
    # 当直线上存在5个相同的颜色的棋子时，判定为胜利
    if chess_count > 5:
        return True

    # 判断右斜
    chess_count = 0
    for i in range(4):
        # 需要控制下标越界的问题
        if (col + i) < 15 and (row - i) > -1 and chess_array[row - i][col + i] == chess:
            chess_count += 1
        else:
            break
    for i in range(4):
        if (col - i) > -1 and (row + i) < 15 and chess_array[row + i][col - i] == chess:
            chess_count += 1
        else:
            break
    # 当直线上存在5个相同的颜色的棋子时，判定为胜利
    if chess_count > 5:
        return True

    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('五子棋(GoBang) version 0.9 --Program by Sean Cheng')

    FONTPATH = WINFONT
    win_font = pygame.font.Font(FONTPATH, 120)
    tip_font = pygame.font.Font(FONTPATH, 24)
    win_str = ''

    chess_array = [[0 for i in range(COL)] for j in range(ROW)]  # 存储棋子的状态
    isblack = True  # 当前是否为黑子下，这个判断条件有多种用途，用在判断现在是谁落子，以及谁落子后获得了胜利。
    iswin = False

    while True:
        screen.fill(ORANGE)  # 绘制背景的颜色
        draw_player_icon(screen)
        draw_chessboard(screen)

        # 绘制出游戏中的各棋子位置
        for col in range(COL):
            for row in range(ROW):
                if chess_array[row][col] == 1:
                    draw_chess(screen, BLACK, row * 35 + 150, col * 35 + 55)
                elif chess_array[row][col] == 2:
                    draw_chess(screen, WHITE, row * 35 + 150, col * 35 + 55)

        # 游戏关闭的控制，关闭窗口和按ESC键即可退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

        # 获取游戏的坐标和按键事件
        mouseX, mouseY = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        # 根据鼠标的坐标计算出对应于数组中的位置
        row = (mouseX - 150 - 15) // 35 + 1
        col = (mouseY - 55 - 15) // 35 + 1

        for press in pressed:
            if press == 1:  # 点击左键的鼠标事件
                # row和col必须是在0~14之间，不然就会报列表越界异常。
                if not iswin and -1 < row < 15 and -1 < col < 15 and chess_array[row][col] == 0:
                    if isblack:
                        # 设定黑子在数组中的数值为1
                        chess_array[row][col] = 1
                        if game_win(chess_array, row, col):
                            win_str = '黑子 胜!'
                            iswin = True
                        isblack = False
                        ai_scan(chess_array)
                    else:
                        # 设定白子在数组中的数值为2
                        chess_array[row][col] = 2
                        if game_win(chess_array, row, col):
                            win_str = '白子 胜!'
                            iswin = True
                        isblack = True
                        ai_scan(chess_array)


        # if not iswin and not isblack:
        #     x, y = ai_scan(chess_array, row, col)
        #     # 设定白子在数组中的数值为2
        #     chess_array[x][y] = 2
        #     if game_win(chess_array, x, y):
        #         win_str = 'white win!'
        #         iswin = True
        #     isblack = True

        # 如果游戏胜利，就显示胜利的画面
        if iswin:
            winstr = win_font.render(win_str, True, RED)
            winstrRect = winstr.get_rect()
            winstrRect.center = 400, 300
            screen.blit(winstr, winstrRect)

        if isblack:
            tip_str = tip_font.render('当前落子为黑子', True, BLACK)
        else:
            tip_str = tip_font.render('当前落子为白子', True, BLACK)
        tip_rect = tip_str.get_rect()
        tip_rect.top = 15
        tip_rect.centerx = 400
        screen.blit(tip_str, tip_rect)

        pygame.time.Clock().tick(150)
        pygame.display.update()


if __name__ == '__main__':
    main()
