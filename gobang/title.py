"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/4/12
@Program      : 游戏开始的选择界面。显示游戏的标题，开始选项，接收选项。
"""
import pygame
from pygame.locals import *


def title(screen, image):
    while True:
        # 添加背景色
        # screen.fill()
        # 添加背景图片
        screen.blit(image, (0, 0))

        return 'play'
