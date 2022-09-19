'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2022/9/9
@Program      : 配置文件
'''
import pyglet

class Settings:
    pyglet.resource.path.append("../res/images")
    pyglet.resource.reindex()

    try:
        pyglet.font.add_directory("../res/fonts")
    except Exception as e:
        print(e)


    ROW = 15
    COLUMN = 15
    SQUARE_SIZE = 32


