'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 
'''
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.text import Label, HTMLLabel, RichLabel
from cocos.menu import *
from pyglet.window import key

from background import BackgroundLayer

class AboutLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        width, height = director.get_window_size()
        about_txt = "本游戏基于PYTHON和COCOS2D制作，为练习\n COCOS2D的游戏练习作品。\n \n 作者：seancheng \n 邮箱：aya234@163.com"
        about_msg = self.create_text(about_txt, 26, 135, 500)

    def create_text(self, msg, size, x, y):
        text = RichLabel(msg,
                     font_name="Unifont",
                     font_size=size,
                     color=(20, 20, 20, 255),
                     width=100,
                     multiline=True,
                     anchor_x="center",
                     anchor_y="top")
        text.position = (x, y)
        self.add(text)

        return text


class AboutMenu(Menu):
    def __init__(self):
        super().__init__()

        self.font_item["font_name"] = "Unifont"
        self.font_item["font_size"] = 28
        self.font_item["color"] = (255, 165, 0, 255)

        self.font_item_selected["font_name"] = "Unifont"
        self.font_item_selected["font_size"] = 28
        self.font_item_selected["color"] = (255, 69, 0, 255)

        self.menu_valign = BOTTOM
        self.menu_halign = CENTER

        items = []
        items.append(MenuItem("返 回 主 菜 单", self.on_back))
        items.append(MenuItem("", self.on_none))
        items.append(MenuItem("退 出 游 戏", self.on_quit))

        self.create_menu(items, zoom_in(), zoom_out())

    def on_none(self):
        pass

    def on_back(self):
        director.pop()

    def on_quit(self):
        exit()



def create_about_scene():
    scene = Scene()
    scene.add(BackgroundLayer("title"), z=0)
    scene.add(AboutLayer(), z=1)
    scene.add(AboutMenu(), z=2)


    return scene