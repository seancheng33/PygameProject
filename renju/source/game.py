'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 
'''
from cocos.layer import Layer, ColorLayer
from cocos.scene import Scene


class GameLayer(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__(255, 140, 0, 128)




def create_game_scene():
    scene = Scene()