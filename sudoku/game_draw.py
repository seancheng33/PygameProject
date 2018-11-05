'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/11/3
@Program      : 绘制游戏的背景和元素
'''
import pygame

from sudoku.SetVar import SetVar

setting = SetVar()


def draw_background(screen):
    # 背景板颜色
    screen.fill(setting.COLOR_DICT['ivory'])

    # 绘制9x9的游戏空间格
    for i in range(10):
        # 加粗第0、3、6、9条线，让里面的9个九宫格比较明显的显示出来
        if i % 3 == 0:
            lineW = 4
        else:
            lineW = 2

        pygame.draw.line(screen, setting.COLOR_DICT['black'], (setting.TILE_SIZE * i + 30, 30),
                         (setting.TILE_SIZE * i + 30, 570), lineW)
        pygame.draw.line(screen, setting.COLOR_DICT['black'], (30, setting.TILE_SIZE * i + 30),
                         (570, setting.TILE_SIZE * i + 30), lineW)

    titleText = setting.TITLEFONT.render('数独游戏', True, setting.COLOR_DICT['coral'])
    titleRect = titleText.get_rect()
    titleRect.topleft = 650, 50
    screen.blit(titleText, titleRect)


def draw_tile(screen, color, start_posx, start_posy, tile_width, tile_height):
    # 将这个rect给return出去，是为了方便下面的文字可以获取这个rect的信息，做对齐用
    return pygame.draw.rect(screen, color, (start_posx, start_posy, tile_width, tile_height))


def draw_gameArray(screen, gameArray):
    posx,posy = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    selected = False
    for row in range(len(gameArray)):
        for col in range(len(gameArray[row])):
            if gameArray[row][col] != '0':
                # 这里是绘制非空的元素的贴片
                tile = draw_tile(screen, setting.COLOR_DICT['tomato'], 60*col+30+6, 60*row+30+6, 48, 48)
                text = setting.TILEFONT.render(gameArray[row][col], True, setting.COLOR_DICT['white'])
                textRect = text.get_rect()
                # textRect.topleft = 60*col+30+16, 60*row+30+16
                textRect.center = tile.center
                screen.blit(text, textRect)

            else:
                # 这里是绘制元素为零的贴片
                tile = draw_tile(screen, setting.COLOR_DICT['yellow'], 60 * col + 30 + 6, 60 * row + 30 + 6,
                                 48, 48)
                # 元素为零的贴片，需要可以点击，然后可以填充数字
                if tile.collidepoint(posx, posy):
                    for event in pressed:
                        if event == 1:
                            selected = True


