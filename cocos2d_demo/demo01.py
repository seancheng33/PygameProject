"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/29
@Program      : cocos2d的入门练习，根据官网内容
"""
import cocos


class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        label = cocos.text.Label(
            'Cocos2d 测试练习',
            font_name='SimHei',
            font_size=32,
            anchor_x='center',
            anchor_y='center'
        )
        label.position = 320, 240
        self.add(label)


cocos.director.director.init()
hello_layer = HelloWorld()
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
