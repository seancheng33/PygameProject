"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/1/14
@Program      : 五子棋游戏
"""
import sys
import pygame
from pygame import *

WHITE = 255, 255, 255
BLACK = 0, 0, 0
ORANGE = 255, 165, 0
GRAY = 200, 200, 200


def draw_chess(screen, chess_color, posx, posy):
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
    # 右下角的头像
    pygame.draw.rect(screen, GRAY, (670, 445, 100, 100))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('GoBang version 0.4 --Program by seancheng')

    chess_array = [[0 for i in range(15)] for j in range(15)]  # 存储棋子的状态
    blackdown = True  # 当前是否为黑子下，这个判断条件有多种用途，用在判断现在改谁下子，以及谁下子后获得了胜利。

    while True:
        screen.fill(ORANGE)
        draw_player_icon(screen)
        draw_chessboard(screen)

        for col in range(len(chess_array)):
            for row in range(len(chess_array[col])):
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

        for press in pressed:
            if press == 1:
                # 根据鼠标的坐标计算出数组的位置
                row = (mouseX - 150 - 15) // 35 + 1
                col = (mouseY - 55 - 15) // 35 + 1
                # row和col必须是在0~14之间，不然就会报列表越界异常。
                if -1 < row < 15 and -1 < col < 15 and chess_array[row][col] == 0:
                    if blackdown:
                        chess_array[row][col] = 1
                        blackdown = False
                    else:
                        chess_array[row][col] = 2
                        blackdown = True
                # print(row, col)

        pygame.time.Clock().tick(150)
        pygame.display.update()


if __name__ == '__main__':
    main()
