"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/18
@Program      : 联系用PyGame制作一个2048的游戏，
"""
import random
import pygame
import sys
from SettingVar import SettingVar

setting = SettingVar()


def add_elem():
    """添加元素功能"""
    while can_add_elem():
        # 生产随机位置元素，完成即跳出运行
        x = random.randint(0, setting.WINDOW_BLOCK_NUM - 1)
        y = random.randint(0, setting.WINDOW_BLOCK_NUM - 1)
        if setting.gameArray[x][y] == 0:
            setting.gameArray[x][y] = 2
            break


def can_add_elem():
    """初始化元素为零的元素数量为16个。每查找到一个非零的元素，计数减1. 如果没有是零的元素，不必添加新元素"""
    num_zero = 16
    # 添加一个判断，如果数组全部非0，不添加元素
    for i in range(setting.WINDOW_BLOCK_NUM):
        for j in range(setting.WINDOW_BLOCK_NUM):
            if setting.gameArray[i][j] != 0:
                num_zero -= 1
    if num_zero == 0:
        return False
    return True


def init_game():
    """初始化游戏的数组，于开始新游戏或者重置游戏时调用"""
    setting.gameArray = [[0 for i in range(setting.WINDOW_BLOCK_NUM)] for j in
                         range(setting.WINDOW_BLOCK_NUM)]  # 初始化的游戏数组
    # 初始化两个开始元素在任意位置。
    random_elem = 0
    while random_elem < 2:
        add_elem()
        random_elem += 1


def can_move():
    """检查是否可以移动，逻辑比较简单，就是逐个元素判断上下左右是否有相同的元素，如果可以存在，就是可以移动。否则就是不能移动"""
    for i in range(setting.WINDOW_BLOCK_NUM):
        for j in range(setting.WINDOW_BLOCK_NUM):
            if setting.gameArray[i][j] != 0:
                return True
            elif setting.gameArray[i][j] == setting.gameArray[i][j + 1]:
                return True
            elif setting.gameArray[i][j] == setting.gameArray[i][j - 1]:
                return True
            elif setting.gameArray[i][j] == setting.gameArray[i + 1][j]:
                return True
            elif setting.gameArray[i][j] == setting.gameArray[i - 1][j]:
                return True
            else:
                return False


def is_win():
    """遍历数组，如果里面有一个元素是2048，就表示胜利"""
    for i in range(setting.WINDOW_BLOCK_NUM):
        for j in range(setting.WINDOW_BLOCK_NUM):
            if setting.gameArray[i][j] == 2048:
                return True
            else:
                return False


def draw_game():
    """完成游戏元素的绘制"""
    for i in range(len(setting.gameArray)):
        for j in range(len(setting.gameArray[0])):
            if setting.gameArray[i][j] != 0:
                tile = pygame.draw.rect(screen, setting.COLOR_DICT['silver'],
                                        ((setting.TILE_SIZE + 20) * i + 110, (setting.TILE_SIZE + 20) * j + 110,
                                         setting.TILE_SIZE, setting.TILE_SIZE))
                tile_text = str(setting.gameArray[i][j])
                text = tileFont.render(tile_text, True, setting.NUM_COLOR_DICT[tile_text])
                text_rect = text.get_rect()
                text_rect.center = tile.center
                screen.blit(text, text_rect)


def draw_background():
    """绘制网格和按键，标题等"""
    screen.fill(setting.COLOR_DICT['bisque'])

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


def main():
    global screen, tileFont, titleText, titleRect, \
        btStartText, btStartRect, btResetText, btResetRect, btExitText, btExitRect

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('游戏2048                  ver 0.18 Program By Sean Cheng')

    font_path = 'c:\\windows\\Fonts\\SimHei.ttf'
    tileFont = pygame.font.Font(font_path, 36)
    titleFont = pygame.font.Font(font_path, 48)
    normalFont = pygame.font.Font(font_path, 24)

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

    init_game()

    while True:

        draw_background()
        draw_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    for i in reversed(range(setting.WINDOW_BLOCK_NUM)):  # 要反序从右边开始往左边移动，不然只移动一格
                        if i > 0:
                            for j in range(setting.WINDOW_BLOCK_NUM):
                                while setting.gameArray[i][j] != 0 and setting.gameArray[i - 1][j] == 0:
                                    setting.gameArray[i - 1][j] = setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                                if setting.gameArray[i][j] == setting.gameArray[i - 1][j]:
                                    setting.gameArray[i - 1][j] += setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                    add_elem()
                    if not can_move():
                        print('lost')
                    elif is_win():
                        print('win')

                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        if i < setting.WINDOW_BLOCK_NUM - 1:
                            for j in range(setting.WINDOW_BLOCK_NUM):
                                while setting.gameArray[i][j] != 0 and setting.gameArray[i + 1][j] == 0:
                                    setting.gameArray[i + 1][j] = setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0

                                if setting.gameArray[i][j] == setting.gameArray[i + 1][j]:
                                    setting.gameArray[i + 1][j] += setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                    add_elem()
                    if not can_move():
                        print('lost')
                    elif is_win():
                        print('win')

                elif event.key in (pygame.K_w, pygame.K_UP):
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        for j in reversed(range(setting.WINDOW_BLOCK_NUM)):  # 要反序从上面往下面移动，不然只移动一格
                            if j > 0:
                                if setting.gameArray[i][j] != 0 and setting.gameArray[i][j - 1] == 0:
                                    setting.gameArray[i][j - 1] = setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                                if setting.gameArray[i][j] == setting.gameArray[i][j - 1]:
                                    setting.gameArray[i][j - 1] += setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                    add_elem()
                    if not can_move():
                        print('lost')
                    elif is_win():
                        print('win')

                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        for j in range(setting.WINDOW_BLOCK_NUM):
                            if j < setting.WINDOW_BLOCK_NUM - 1:
                                # 移动元素
                                if setting.gameArray[i][j] != 0 and setting.gameArray[i][j + 1] == 0:
                                    setting.gameArray[i][j + 1] = setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                                # 合并元素
                                if setting.gameArray[i][j] == setting.gameArray[i][j + 1]:
                                    setting.gameArray[i][j + 1] += setting.gameArray[i][j]
                                    setting.gameArray[i][j] = 0
                    add_elem()
                    if not can_move():
                        print('lost')
                    elif is_win():
                        print('win')

            # 右侧的按键的鼠标事件
            x, y = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()

            if btStartRect.collidepoint(x, y):
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        init_game()  # 初始化的游戏数组
            else:
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['tomato'])

            if btResetRect.collidepoint(x, y):
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        init_game()  # 初始化的游戏数组
            else:
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['tomato'])

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

"""
游戏开始后，开始按键应该为不可用。
同理，游戏未开始，应该重置游戏不可用。
"""
