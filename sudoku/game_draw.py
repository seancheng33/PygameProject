'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/11/3
@Program      : 绘制游戏的背景和元素
'''
import pygame

from sudoku import function
from sudoku.SetVar import SetVar
from sudoku.function import selected_array

setting = SetVar()


def statistics(gameArray):
    # 统计游戏数组中各个数字出现的次数。
    num_dict = {}
    for item in gameArray:
        for num in item:
            num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


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

    #
    num1Text = setting.TEXTFONT.render('1', True, setting.COLOR_DICT['black'])
    num2Text = setting.TEXTFONT.render('2', True, setting.COLOR_DICT['black'])
    num3Text = setting.TEXTFONT.render('3', True, setting.COLOR_DICT['black'])
    num4Text = setting.TEXTFONT.render('4', True, setting.COLOR_DICT['black'])
    num5Text = setting.TEXTFONT.render('5', True, setting.COLOR_DICT['black'])
    num6Text = setting.TEXTFONT.render('6', True, setting.COLOR_DICT['black'])
    num7Text = setting.TEXTFONT.render('7', True, setting.COLOR_DICT['black'])
    num8Text = setting.TEXTFONT.render('8', True, setting.COLOR_DICT['black'])
    num9Text = setting.TEXTFONT.render('9', True, setting.COLOR_DICT['black'])

    num1Rect = num1Text.get_rect()
    num2Rect = num2Text.get_rect()
    num3Rect = num3Text.get_rect()
    num4Rect = num4Text.get_rect()
    num5Rect = num5Text.get_rect()
    num6Rect = num6Text.get_rect()
    num7Rect = num7Text.get_rect()
    num8Rect = num8Text.get_rect()
    num9Rect = num9Text.get_rect()

    num1Rect.topleft = 620, 520
    num2Rect.topleft = 650, 520
    num3Rect.topleft = 680, 520
    num4Rect.topleft = 710, 520
    num5Rect.topleft = 740, 520
    num6Rect.topleft = 770, 520
    num7Rect.topleft = 800, 520
    num8Rect.topleft = 830, 520
    num9Rect.topleft = 860, 520

    screen.blit(num1Text, num1Rect)
    screen.blit(num2Text, num2Rect)
    screen.blit(num3Text, num3Rect)
    screen.blit(num4Text, num4Rect)
    screen.blit(num5Text, num5Rect)
    screen.blit(num6Text, num6Rect)
    screen.blit(num7Text, num7Rect)
    screen.blit(num8Text, num8Rect)
    screen.blit(num9Text, num9Rect)

    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 500), (880, 500))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 490), (880, 490))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 480), (880, 480))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 470), (880, 470))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 460), (880, 460))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 450), (880, 450))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 440), (880, 440))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 430), (880, 430))
    pygame.draw.line(screen, setting.COLOR_DICT['gray'], (610, 420), (880, 420))
    pygame.draw.line(screen, setting.COLOR_DICT['orange'], (610, 410), (880, 410))


def draw_tile(screen, color, start_posx, start_posy, tile_width, tile_height):
    # 将这个rect给return出去，是为了方便下面的文字可以获取这个rect的信息，做对齐用
    return pygame.draw.rect(screen, color, (start_posx, start_posy, tile_width, tile_height))


def draw_gameArray(screen, gameArray):
    posx, posy = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    for row in range(len(gameArray)):
        for col in range(len(gameArray[row])):
            if gameArray[row][col] != '0':
                # 这里是绘制非空的元素的贴片
                tile = draw_tile(screen, setting.COLOR_DICT['tomato'], setting.TILE_SIZE * col + 30 + 6,
                                 setting.TILE_SIZE * row + 30 + 6, setting.TILE_DRAW_SIZE, setting.TILE_DRAW_SIZE)
                text = setting.TILEFONT.render(gameArray[row][col], True, setting.COLOR_DICT['white'])
                textRect = text.get_rect()
                # textRect.topleft = 60*col+30+16, 60*row+30+16
                textRect.center = tile.center
                screen.blit(text, textRect)
            else:
                # 这里是绘制元素为零的贴片
                tile = draw_tile(screen, setting.COLOR_DICT['ivory'], setting.TILE_SIZE * col + 30 + 6,
                                 setting.TILE_SIZE * row + 30 + 6, setting.TILE_DRAW_SIZE, setting.TILE_DRAW_SIZE)

                # 元素为零的贴片，需要可以点击，然后可以填充数字
                if tile.collidepoint(posx, posy):
                    for event in pressed:
                        if event == 1:
                            pressedX = (posx - 30) // setting.TILE_SIZE
                            pressedY = (posy - 30) // setting.TILE_SIZE
                            selected_array(pressedX, pressedY)
                            print(setting.selectedArray)

    #
    num_dict = statistics(gameArray)

    #
    num1Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (620, 510, 10, num_dict.get('1', 0) * (-10) - 10))
    num2Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (650, 510, 10, num_dict.get('2', 0) * (-10) - 10))
    num3Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (680, 510, 10, num_dict.get('3', 0) * (-10) - 10))
    num4Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (710, 510, 10, num_dict.get('4', 0) * (-10) - 10))
    num5Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (740, 510, 10, num_dict.get('5', 0) * (-10) - 10))
    num6Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (770, 510, 10, num_dict.get('6', 0) * (-10) - 10))
    num7Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (800, 510, 10, num_dict.get('7', 0) * (-10) - 10))
    num8Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (830, 510, 10, num_dict.get('8', 0) * (-10) - 10))
    num9Rect = pygame.draw.rect(screen, setting.COLOR_DICT['tomato'], (860, 510, 10, num_dict.get('9', 0) * (-10) - 10))

def draw_seletced(screen):
    array = setting.selectedArray
    # print(array)
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[col][row] == 1:
                draw_tile(screen, setting.COLOR_DICT['tomato'], setting.TILE_SIZE * col + 30 + 6,
                                 setting.TILE_SIZE * row + 30 + 6, setting.TILE_DRAW_SIZE, setting.TILE_DRAW_SIZE)
