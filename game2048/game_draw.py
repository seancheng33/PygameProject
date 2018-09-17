"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/10
@Program      : 绘制游戏的画面，
"""
import pygame
from SettingVar import SettingVar

setting = SettingVar()

def draw_game(screen, tileFont, gameArray):
    """完成游戏元素的绘制"""
    for i in range(len(gameArray)):
        for j in range(len(gameArray[0])):
            if gameArray[i][j] != 0:
                tile = pygame.draw.rect(screen, setting.COLOR_DICT['silver'],
                                        ((setting.TILE_SIZE + 20) * i + 110, (setting.TILE_SIZE + 20) * j + 110,
                                         setting.TILE_SIZE, setting.TILE_SIZE))
                tile_text = str(gameArray[i][j])
                text = tileFont.render(tile_text, True, setting.NUM_COLOR_DICT[tile_text])
                text_rect = text.get_rect()
                text_rect.center = tile.center
                screen.blit(text, text_rect)


def draw_background(screen, titleText, titleRect, btStartText, btStartRect, btResetText, btResetRect, btExitText,
                    btExitRect):
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