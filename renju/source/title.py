'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 标题和进入主游戏的场景
'''
from cocos.layer import MultiplexLayer
from cocos.scene import Scene
from cocos.menu import *
from background import BackgroundLayer
from settings import Settings

class MainMenu(Menu):
    def __init__(self):
        super().__init__("五  子  棋")

        self.font_title["font_name"] = "aoyagireisyosimo2"
        self.font_title["font_size"] = 72
        self.font_title["color"] = (0, 0, 0, 255)
        self.font_title["bold"] = True
        self.font_title["anchor_y"] = TOP


        self.font_item["font_name"] = "Unifont"
        self.font_item["font_size"] = 32
        self.font_item["color"] = (255, 165, 0, 255)

        self.font_item_selected["font_name"] = "Unifont"
        self.font_item_selected["font_size"] = 32
        self.font_item_selected["color"] = (255, 69, 0, 255)

        self.menu_valign = BOTTOM
        self.menu_halign = CENTER

        items = []
        items.append(MenuItem("开 始 游 戏", self.on_play))
        items.append(MenuItem("", self.on_none))
        items.append(MenuItem("关 于 本 游 戏", self.on_about))
        items.append(MenuItem("", self.on_none))
        items.append(MenuItem("退 出 游 戏", self.on_quit))

        self.create_menu(items, zoom_in(), zoom_out())

    def on_play(self):
        pass

    def on_none(self):
        pass

    def on_about(self):
        self.parent.switch_to(1)

    def on_quit(self):
        exit()


class AboutMenu(Menu):
    def __init__(self):
        super().__init__()

        self.font_item["font_name"] = "Unifont"
        self.font_item["font_size"] = 32
        self.font_item["color"] = (255, 165, 0, 255)

        self.font_item_selected["font_name"] = "Unifont"
        self.font_item_selected["font_size"] = 32
        self.font_item_selected["color"] = (255, 69, 0, 255)

        self.menu_valign = BOTTOM
        self

        items = []
        items.append(MenuItem("返 回 主 菜 单", self.on_back))

        self.create_menu(items, shake(), shake_back())

    def on_back(self):
        self.parent.switch_to(0)

def create_title_scene():
    scene = Scene()
    scene.add(BackgroundLayer('title'), z=0)

    scene.add(MultiplexLayer(MainMenu(), AboutMenu()), z=1)

    return scene