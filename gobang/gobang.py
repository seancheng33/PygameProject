"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/1/14
@Program      : 五子棋游戏
"""
import pygame
from pygame import *

WHITE = 255, 255, 255
BLACK = 0, 0, 0
ORANGE = 255, 165, 0
GRAY = 200, 200, 200


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
    pygame.draw.circle(screen, BLACK, (35 * 3 + 150, 35 * 3 + 55), 10)
    pygame.draw.circle(screen, BLACK, (35 * 3 + 150, 35 * 11 + 55), 10)
    pygame.draw.circle(screen, BLACK, (35 * 7 + 150, 35 * 7 + 55), 10)
    pygame.draw.circle(screen, BLACK, (35 * 11 + 150, 35 * 3 + 55), 10)
    pygame.draw.circle(screen, BLACK, (35 * 11 + 150, 35 * 11 + 55), 10)


def draw_player_icon(screen):
    # 左上角的头像
    pygame.draw.rect(screen, GRAY, (20, 55, 100, 100))
    # 右下角的头像
    pygame.draw.rect(screen, GRAY, (670, 445, 100, 100))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('GoBang version 0.03 --Program by seancheng')

    while True:
        screen.fill(ORANGE)
        draw_player_icon(screen)
        draw_chessboard(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.time.Clock().tick(200)
        pygame.display.update()


if __name__ == '__main__':
    main()
