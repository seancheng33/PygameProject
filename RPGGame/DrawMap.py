'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/13
@Program      : 绘制地图的功能
'''
import pygame
from pygame.locals import *
from GlobalSetting import GlobalSetting

setting = GlobalSetting()


def draw_map(mapObj, gameStateObj):
    # 绘制整个地图
    mapWidth = len(mapObj[0]) * setting.TILESIZE
    mapHeight = len(mapObj) * setting.TILESIZE
    mapSurface = pygame.Surface((mapWidth, mapHeight))

    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            mapSurface.blit(setting.TILEMAPPING[mapObj[x][y]], (y * setting.TILESIZE, x * setting.TILESIZE))

    # 游戏的角色是绘制在这里的吗？
    x, y = gameStateObj['player']
    role = pygame.image.load('img/horngirl.png')
    role_rect = pygame.Rect(x * setting.TILESIZE, y * setting.TILESIZE, setting.TILESIZE, setting.TILESIZE)
    mapSurface.blit(role, role_rect)

    return mapSurface


def redraw_map(mapObj, gameStateObj):
    # 这段重绘地图的概念是，获取角色的坐标，然后如果角色的坐标不是在正中间的话，计算偏移值，就移动地图。
    # 现在的地图移动可以移动一般，接近界限的地方的移动是个问题。需要再收集资料。
    x, y = gameStateObj['player']
    mapwidth = mapObj.get_width() / setting.TILESIZE  # 算出原始地图的宽度
    mapheight = mapObj.get_height() / setting.TILESIZE  # 算出原始地图的高度

    half_x = int(setting.TILEWIDTH // 2) + 1  # 屏幕的宽一半的位置，作为角色的中间点
    half_y = int(setting.TILEHEIGHT // 2) + 1  # 屏幕的高一半的位置，作为角色的中间点

    if half_x < x < setting.TILEWIDTH:
        if half_x >= setting.TILEWIDTH - x:
            offsetX = (mapwidth - setting.TILEWIDTH) * setting.TILESIZE
        else:
            offsetX = (x - half_x) * setting.TILESIZE
    else:
        offsetX = 0 * setting.TILESIZE

    if half_y < y < setting.TILEHEIGHT:
        if half_y >= setting.TILEHEIGHT - y:
            offsetY = (mapheight - setting.TILEHEIGHT) * setting.TILESIZE
        else:
            offsetY = (y - half_y) * setting.TILESIZE
    else:
        offsetY = 0 * setting.TILESIZE


    if mapwidth > setting.TILEWIDTH and mapheight > setting.TILEHEIGHT:
        sub_map = Rect(offsetX, offsetY, setting.SCREENWIDTH, setting.SCREENHEIGHT)
        mapSurface = mapObj.subsurface(sub_map)
        return mapSurface

    return mapObj
