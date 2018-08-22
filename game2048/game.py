'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/18
@Program      : 联系用pygame制作一个2048的游戏，
'''
import random

import pygame
import sys


def add_elem():
    # 生产随机位置元素，完成即跳出运行
    x = random.randint(0, WINDOW_BLOCK_NUM - 1)
    y = random.randint(0, WINDOW_BLOCK_NUM - 1)

    if gameArray[x][y] == 0:
        gameArray[x][y] = 2


COLOR_DICT = {'white': (255, 255, 255),  # 白色
              'ivory': (255, 255, 240),  # 象牙色
              'yellow': (255, 255, 0),  # 黄色
              'seashell': (255, 245, 238),  # 海贝色
              'bisque': (255, 228, 196),  # 橘黄色
              'gold': (255, 215, 0),  # 金色
              'pink': (255, 192, 203),  # 粉红色
              'lightpink': (255, 182, 193),  # 亮粉红色
              'orange': (255, 165, 0),  # 橙色
              'coral': (255, 127, 80),  # 珊瑚色
              'tomato': (255, 99, 71),  # 番茄色
              'magenta': (255, 0, 255),  # 洋红色
              'wheat': (245, 222, 179),  # 小麦色
              'violet': (238, 130, 238),  # 紫罗兰色
              'silver': (192, 192, 192),  # 银白色
              'brown': (165, 42, 42),  # 棕色
              'gray': (128, 128, 128),  # 灰色
              'olive': (128, 128, 0),  # 橄榄色
              'purple': (128, 0, 128),  # 紫色
              'turquoise': (64, 224, 208),  # 绿宝石色
              'seagreen': (46, 139, 87),  # 海洋绿色
              'cyan': (0, 255, 255),  # 青色
              'green': (0, 128, 0),  # 纯绿色
              'blue': (0, 0, 255),  # 纯蓝色
              'darkblue': (0, 0, 139),  # 深蓝色
              'navy': (0, 0, 128),  # 海军蓝色
              'black': (0, 0, 0),  # 纯黑色
              }

NUM_COLOR_DICT = {'2': COLOR_DICT['gray'], '4': COLOR_DICT['brown'], '8': COLOR_DICT['violet'],
                  '16': COLOR_DICT['wheat'], '32': COLOR_DICT['coral'], '64': COLOR_DICT['turquoise'],
                  '128': COLOR_DICT['navy'], '256': COLOR_DICT['olive'], '512': COLOR_DICT['orange'],
                  '1024': COLOR_DICT['seagreen'], '2048': COLOR_DICT['purple']}

TILE_SIZE = 80
WINDOW_BLOCK_NUM = 4

gameArray = [[0 for i in range(WINDOW_BLOCK_NUM)] for j in range(WINDOW_BLOCK_NUM)]  # 初始化的游戏数组

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('游戏2048                  ver 0.8 Program By Sean Cheng')

font_path = 'c:\\windows\\Fonts\\SimHei.ttf'
tileFont = pygame.font.Font(font_path, 36)
titleFont = pygame.font.Font(font_path, 48)
normalFont = pygame.font.Font(font_path, 24)

# 初始化两个开始元素在任意位置。
random_elem = 0
while random_elem < 2:
    add_elem()
    random_elem += 1
# print(gameArray)

titleText = titleFont.render('游戏2048', True, COLOR_DICT['gray'])
titleRect = titleText.get_rect()
titleRect.topleft = 570, 60

btStartText = normalFont.render('开始游戏', True, COLOR_DICT['tomato'])
btStartRect = btStartText.get_rect()
btStartRect.topleft = 620, 400
btResetText = normalFont.render('重置游戏', True, COLOR_DICT['tomato'])
btResetRect = btResetText.get_rect()
btResetRect.topleft = 620, 440
btExitText = normalFont.render('退出游戏', True, COLOR_DICT['tomato'])
btExitRect = btExitText.get_rect()
btExitRect.topleft = 620, 480

while True:

    screen.fill(COLOR_DICT['bisque'])

    screen.blit(titleText, titleRect)
    screen.blit(btStartText, btStartRect)
    screen.blit(btResetText, btResetRect)
    screen.blit(btExitText, btExitRect)

    # 五条横线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (500, 100), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 200), (500, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 300), (500, 300), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 400), (500, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 500), (500, 500), 2)

    # 五条竖线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (100, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (200, 100), (200, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (300, 100), (300, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (400, 100), (400, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (500, 100), (500, 500), 2)

    # 完成游戏元素的绘制
    for i in range(len(gameArray)):
        for j in range(len(gameArray[0])):
            if gameArray[i][j] != 0:
                tile = pygame.draw.rect(screen, COLOR_DICT['silver'],
                                        ((TILE_SIZE + 20) * i + 110, (TILE_SIZE + 20) * j + 110, TILE_SIZE, TILE_SIZE))
                tile_text = str(gameArray[i][j])
                text = tileFont.render(tile_text, True, NUM_COLOR_DICT[tile_text])
                text_rect = text.get_rect()
                text_rect.center = tile.center
                screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                for i in range(WINDOW_BLOCK_NUM):
                    if i > 0:
                        for j in range(WINDOW_BLOCK_NUM):
                            while gameArray[i][j] != 0 and gameArray[i - 1][j] == 0:
                                gameArray[i - 1][j] = gameArray[i][j]
                                gameArray[i][j] = 0
                            if gameArray[i][j] == gameArray[i - 1][j]:
                                gameArray[i - 1][j] += gameArray[i][j]
                                gameArray[i][j] = 0
                add_elem()

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                for i in range(WINDOW_BLOCK_NUM):
                    if i < WINDOW_BLOCK_NUM - 1:
                        for j in range(WINDOW_BLOCK_NUM):
                            while gameArray[i][j] != 0 and gameArray[i + 1][j] == 0:
                                gameArray[i + 1][j] = gameArray[i][j]
                                gameArray[i][j] = 0

                            if gameArray[i][j] == gameArray[i + 1][j]:
                                gameArray[i + 1][j] += gameArray[i][j]
                                gameArray[i][j] = 0
                add_elem()

            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                for i in range(WINDOW_BLOCK_NUM):
                    for j in range(WINDOW_BLOCK_NUM):
                        if j > 0:
                            if gameArray[i][j] != 0 and gameArray[i][j - 1] == 0:
                                gameArray[i][j - 1] = gameArray[i][j]
                                gameArray[i][j] = 0
                            if gameArray[i][j] == gameArray[i][j - 1]:
                                gameArray[i][j - 1] += gameArray[i][j]
                                gameArray[i][j] = 0
                add_elem()

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                for i in range(WINDOW_BLOCK_NUM):
                    for j in range(WINDOW_BLOCK_NUM):
                        if j < WINDOW_BLOCK_NUM - 1:
                            # 移动元素
                            if gameArray[i][j] != 0 and gameArray[i][j + 1] == 0:
                                gameArray[i][j + 1] = gameArray[i][j]
                                gameArray[i][j] = 0
                            # 合并元素
                            if gameArray[i][j] == gameArray[i][j + 1]:
                                gameArray[i][j + 1] += gameArray[i][j]
                                gameArray[i][j] = 0
                add_elem()

    pygame.display.update()
    pygame.time.Clock().tick(30)
