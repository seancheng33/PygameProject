'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 
'''

from cocos.layer import Layer
from pyglet.gl import *


class BackgroundLayer(Layer):
    def __init__(self, background):
        super().__init__()
        if background == "title":
            self.img = pyglet.resource.image("title.png")
        elif background == "game":
            self.img = pyglet.resource.image("background.png")

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0, 0)
        glPopMatrix()