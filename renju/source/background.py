'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 
'''

from cocos.layer import Layer
from pyglet.gl import *


class BackgroundLayer(Layer):
    def __init__(self, bg_name):
        super().__init__()

        if bg_name == "title":
            self.img = pyglet.resource.image("title.png")
        elif bg_name == "gameing":
            self.img = pyglet.resource.image("background.png")

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0, 0)
        glPopMatrix()