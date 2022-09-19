'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 游戏的主要入口
'''

from cocos.director import director

import title

def GameRun():
    director.init(resizable=True, width=800, height=600, caption="五子棋游戏 version--0.5")
    director.run(title.create_title_scene())


if __name__ == '__main__':
    GameRun()