'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/14
@Program      : 关于游戏的界面
'''
import pygame
from pygame.locals import *


def about_this(SURFACE, globalVar):
    productName = '游戏名称：大脑很囧'
    programBy = '程序设计：Sean Cheng'
    guiDesing = 'UI设计：Sean Cheng'
    copyRight = 'CopyRight © Sean Cheng'

    aboutText = [productName, programBy, guiDesing, copyRight, '',
                 '本游戏使用python+pygame制作。', '此游戏算是本人的一个pygame的练习制作，仅凭个人爱好制作，精力有限。',
                 '难免存在一些瑕疵的地方，也可能存在暂时未能发现的BUG，', '如果您有什么宝贵的建议，可以与我联系 aya234@163.com',
                 '', '', '若本游戏感兴趣欢迎扫右方的二维码码打赏。']

    bg = pygame.image.load('img/about.png')

    bt_back = pygame.Rect((0, 0), (180, 60))
    bt_back.left = 300
    bt_back.bottom = 580

    back_img = globalVar.globalFont.render('返  回', True, globalVar.color_dict['white'])
    back_rect = back_img.get_rect()
    back_rect.center = bt_back.center

    while True:
        SURFACE.fill(globalVar.color_dict['black'])
        SURFACE.blit(bg, (0, 0))

        for item in aboutText:
            # font_img = globalVar.aboutFont.render(item, True, globalVar.color_dict['red'])
            # font_rect = font_img.get_rect()
            font_img, font_rect=globalVar.maketext(globalVar.aboutFont, item, globalVar.color_dict['red'])
            font_rect.top = 80 + aboutText.index(item) * 30
            font_rect.left = 80

            SURFACE.blit(font_img, font_rect)

        pygame.draw.rect(SURFACE, globalVar.color_dict['lime'], bt_back)

        for event in pygame.event.get():
            if event.type == QUIT:
                globalVar.close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    globalVar.close_program()
                # elif event.key == K_RETURN:  # 这个可以不用，已经做了按键
                #     return 'reset'

        pygame.mouse.set_visible(True)

        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if bt_back.left < x < bt_back.right and bt_back.top < y < bt_back.bottom:
            pygame.draw.rect(SURFACE, globalVar.color_dict['orange'], bt_back)
            for event in pressed:
                if event == 1:
                    return 'reset'

        SURFACE.blit(back_img, back_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)
