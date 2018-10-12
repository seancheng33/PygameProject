"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/18
@Program      : 联系用PyGame制作一个2048的游戏，
"""

import pygame
import sys
from SettingVar import SettingVar
from game_draw import draw_background, draw_game
from GameFunction import init_game, add_elem, can_add_elem, can_move, is_win, win_or_lost

setting = SettingVar()


def main():
    global screen, tileFont, titleFont, normalFont

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('游戏2048                  ver 0.28 Program By Sean Cheng')

    font_path = 'c:\\windows\\Fonts\\SimHei.ttf'
    tileFont = pygame.font.Font(font_path, 36)
    titleFont = pygame.font.Font(font_path, 48)
    normalFont = pygame.font.Font(font_path, 24)
    resultFont = pygame.font.Font(font_path,120)

    titleText = titleFont.render('游戏2048', True, setting.COLOR_DICT['gray'])
    titleRect = titleText.get_rect()
    titleRect.topleft = 570, 60

    btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['tomato'])
    btStartRect = btStartText.get_rect()
    btStartRect.topleft = 620, 400
    btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['tomato'])
    btResetRect = btResetText.get_rect()
    btResetRect.topleft = 620, 440
    btExitText = normalFont.render('退出游戏', True, setting.COLOR_DICT['tomato'])
    btExitRect = btExitText.get_rect()
    btExitRect.topleft = 620, 480

    gameArray = init_game()

    gamestatus = None

    while True:

        draw_background(screen, titleText, titleRect, btStartText, btStartRect, btResetText, btResetRect, btExitText,
                        btExitRect)
        # 游戏状态条件的判断
        if gamestatus == 'play':
            gamestatus = win_or_lost(gameArray)
            draw_game(screen, tileFont, gameArray)
        elif gamestatus == 'win':
            # print('win')
            winText = resultFont.render('YOU WIN!!', True, setting.COLOR_DICT['tomato'])
            winRect = winText.get_rect()
            winRect.topleft = 0, 0
        elif gamestatus == 'lost':
            # print('lost')
            lostText = resultFont.render('YOU LOST!!', True, setting.COLOR_DICT['tomato'])
            lostRect = lostText.get_rect()
            lostRect.topleft = 0, 0
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP and gamestatus == 'play':
                # 只有在游戏状态是play的时候，才按键有效。防止没有点击游戏开始就可以开始玩游戏
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    for i in reversed(range(setting.WINDOW_BLOCK_NUM)):  # 要反序从右边开始往左边移动，不然只移动一格
                        if i > 0:
                            for j in range(setting.WINDOW_BLOCK_NUM):
                                # 移动元素
                                while gameArray[i][j] != 0 and gameArray[i - 1][j] == 0:
                                    gameArray[i - 1][j] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                # 合并元素
                                if gameArray[i][j] == gameArray[i - 1][j]:
                                    gameArray[i - 1][j] *= 2
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        if i < setting.WINDOW_BLOCK_NUM - 1:
                            for j in range(setting.WINDOW_BLOCK_NUM):
                                # 移动元素
                                while gameArray[i][j] != 0 and gameArray[i + 1][j] == 0:
                                    gameArray[i + 1][j] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                # 合并元素
                                if gameArray[i][j] == gameArray[i + 1][j]:
                                    gameArray[i + 1][j] *= 2
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

                elif event.key in (pygame.K_w, pygame.K_UP):
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        for j in reversed(range(setting.WINDOW_BLOCK_NUM)):  # 要反序从上面往下面移动，不然只移动一格
                            if j > 0:
                                # 移动元素
                                if gameArray[i][j] != 0 and gameArray[i][j - 1] == 0:
                                    gameArray[i][j - 1] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                # 合并元素
                                if gameArray[i][j] == gameArray[i][j - 1]:
                                    gameArray[i][j - 1] *= 2
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        for j in range(setting.WINDOW_BLOCK_NUM):
                            if j < setting.WINDOW_BLOCK_NUM - 1:
                                # 移动元素
                                if gameArray[i][j] != 0 and gameArray[i][j + 1] == 0:
                                    gameArray[i][j + 1] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                # 合并元素
                                if gameArray[i][j] == gameArray[i][j + 1]:
                                    gameArray[i][j + 1] *= 2
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

            # 右侧的按键的鼠标事件
            x, y = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()

            # 按键的可用和禁用判断
            if gamestatus != 'play':
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['gray'])
            else:
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['gray'])

            # 开始游戏按键的鼠标事件，根据游戏状态来判断按键的颜色，只判断游戏状态是否‘start’即可，
            # 因为就算是游戏胜利或者失败，都可以点开始才更符合使用习惯。
            if btStartRect.collidepoint(x, y) and gamestatus != 'play':
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        gameArray = init_game()  # 初始化的游戏数组
                        gamestatus = 'play'
            elif gamestatus != 'play':
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['tomato'])

            # 重置游戏按键的鼠标事件，于开始按键类似的理由，只有在游戏的时候才需要重置，胜利和失败都不需要。
            if btResetRect.collidepoint(x, y) and gamestatus == 'play':
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        gameArray = init_game()  # 初始化的游戏数组
            elif gamestatus == 'play':
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['tomato'])

            # 退出游戏按键的鼠标事件，不需要有一个游戏状态的判断，因为这个按键是需要任何时间都可用。
            if btExitRect.collidepoint(x, y):
                btExitText = normalFont.render('退出游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        pygame.quit()
                        sys.exit(0)
            else:
                btExitText = normalFont.render('退出游戏', True, setting.COLOR_DICT['tomato'])

        pygame.display.update()
        pygame.time.Clock().tick(30)


if __name__ == '__main__':
    main()

