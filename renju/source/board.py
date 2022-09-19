'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/19
@Program      : 
'''
from cocos.scene import Scene

from renju.source.settings import Settings


class Board():
    def __int__(self):
        array = [[0 for col in range(Settings.COLUMN)] for row in range(Settings.ROW)]


def create_game_scena():
    scene = Scene()