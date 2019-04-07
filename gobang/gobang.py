"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/1/14
@Program      : 五子棋游戏，目标为实现可以简单的人机对弈。
"""
import pygame
from pygame.locals import *
import ComputerAI

WHITE = 255, 255, 255
BLACK = 0, 0, 0
ORANGE = 255, 165, 0
GRAY = 127, 127, 127
RED = 255, 0, 0

ROW = 15
COL = 15

WINFONT = 'c:/windows/Fonts/SimHei.ttf'
MACFONT = '/System/Library/Fonts/'
LINUXFONT = '/usr/share/fonts'

WHITEFIRST = True


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


def game_win(chess_array, chessColor):
    # 方向横(-)的检查
    for x in range(ROW):
        for y in range(COL - 4):
            if chess_array[x][y] == chessColor and chess_array[x][y + 1] == chessColor and chess_array[x][y + 2] == \
                    chessColor and chess_array[x][y + 3] == chessColor and chess_array[x][y + 4] == chessColor:
                return True
    # 方向竖(-)的检查
    for x in range(ROW - 4):
        for y in range(COL):
            if chess_array[x][y] == chessColor and chess_array[x + 1][y] == chessColor and chess_array[x + 2][y] == \
                    chessColor and chess_array[x + 3][y] == chessColor and chess_array[x + 4][y] == chessColor:
                return True
    # 方向斜(/)的检查
    for x in range(ROW - 4):
        for y in range(4, COL):
            if chess_array[x][y] == chessColor and chess_array[x + 1][y - 1] == chessColor and \
                    chess_array[x + 2][y - 2] == chessColor and chess_array[x + 3][y - 3] == chessColor and \
                    chess_array[x + 4][y - 4] == chessColor:
                return True
    # 方向斜(\)的检查
    for x in range(ROW - 4):
        for y in range(COL - 4):
            if chess_array[x][y] == chessColor and chess_array[x + 1][y + 1] == chessColor and \
                    chess_array[x + 2][y + 2] == chessColor and chess_array[x + 3][y + 3] == chessColor and \
                    chess_array[x + 4][y + 4] == chessColor:
                return True

    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('五子棋(GoBang) version 0.26 --Program by Sean Cheng')
    pygame.display.set_icon(pygame.image.load('img/TitleIcon.png'))

    FONTPATH = WINFONT
    win_font = pygame.font.Font(FONTPATH, 120)
    tip_font = pygame.font.Font(FONTPATH, 24)
    win_str = None

    chess_array = [[None for i in range(COL)] for j in range(ROW)]  # 存储棋子的状态
    isblack = True  # 当前是否为黑子下，这个判断条件有多种用途，用在判断现在是谁落子，以及谁落子后获得了胜利。
    iswin = False

    while True:
        screen.fill(ORANGE)  # 绘制背景的颜色
        draw_player_icon(screen)
        draw_chessboard(screen)

        # 绘制出游戏中的各棋子位置
        for col in range(COL):
            for row in range(ROW):
                if chess_array[row][col] == 'black':
                    draw_chess(screen, BLACK, row * 35 + 150, col * 35 + 55)
                elif chess_array[row][col] == 'white':
                    draw_chess(screen, WHITE, row * 35 + 150, col * 35 + 55)

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
            x, y = ComputerAI.ai_scan(chess_array)
            # 设定白子在数组中的数值为2
            chess_array[x][y] = 'white'
            if game_win(chess_array, 'white'):
                win_str = '白子 胜!'
                iswin = True
            isblack = True

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
