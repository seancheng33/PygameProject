'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/6/19
@Program      : pygame练习，做一个答题的程序，有游戏的标题界面，鼠标选择答案的形式作答，题库使用xml文件的形式。
'''
import os
import random
import sys

import pygame
from pygame.locals import *
from questions.LoadGame import load_game
from questions.globalVar import GlobalVar


def game_title():
    title_text = '大脑 很囧'
    bt_start_text = '开 始 游 戏'
    bt_about_text = '关 于 游 戏'
    title_bg = pygame.image.load('img/main.jpg')
    title_image = titleFont.render(title_text, True, color_dict['green'])
    title_time = 0
    mouseCursor = pygame.image.load('img/cursor.png').convert_alpha()  # 加载鼠标图片

    while True:
        SURFACE.blit(title_bg, (0, 0))
        if title_time == 0:
            title_image = titleFont.render(title_text, True, color_dict['white'])
            title_time = 1
        elif title_time == 1:
            title_image = titleFont.render(title_text, True, color_dict['green'])
            title_time = 2
        elif title_time == 2:
            title_image = titleFont.render(title_text, True, color_dict['lime'])
            title_time = 0
        title_rect = title_image.get_rect()
        title_rect.centerx = SURFACE.get_rect().centerx
        title_rect.top = 130

        tips_image = globalFont.render(bt_start_text, True, color_dict['orange'])
        tips_rect = tips_image.get_rect()
        tips_rect.centerx = SURFACE.get_rect().centerx - 150
        tips_rect.top = 400

        help_image = globalFont.render(bt_about_text, True, color_dict['orange'])
        help_rect = help_image.get_rect()
        help_rect.centerx = SURFACE.get_rect().centerx + 150
        help_rect.top = 400

        SURFACE.blit(title_image, title_rect)
        SURFACE.blit(tips_image, tips_rect)
        SURFACE.blit(help_image, help_rect)

        for event in pygame.event.get():
            # 关闭按钮的事件
            if event.type == QUIT:
                GlobalVar().close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    GlobalVar().close_program()

        x, y = pygame.mouse.get_pos()
        pressed_array = pygame.mouse.get_pressed()  # 获取鼠标事件的列表

        # 开始按键的鼠标事件，包括了鼠标经过事件和点击事件
        if tips_rect.left < x < tips_rect.right and tips_rect.top < y < tips_rect.bottom:
            tips_image = globalFont.render(bt_start_text, True, color_dict['red'])
            SURFACE.blit(tips_image, tips_rect)
            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    return 'start'

        # 关于按键的鼠标事件
        if help_rect.left < x < help_rect.right and help_rect.top < y < help_rect.bottom:
            help_image = globalFont.render(bt_about_text, True, color_dict['red'])
            SURFACE.blit(help_image, help_rect)
            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    return 'about'

        # 自定义鼠标样式
        pygame.mouse.set_visible(False)

        x -= 0
        y -= 0

        SURFACE.blit(mouseCursor, (x, y))
        pygame.display.update()
        pygame.time.Clock().tick(20)


def end_game(score, right_score, wrong_score):
    # 游戏的结束界面，对刚才完过的游戏做出一些数据统计。
    score_img = globalFont.render('最终总成绩： ' + str(score), True, color_dict['orange'])
    score_rect = score_img.get_rect()
    score_rect.top = 150
    score_rect.centerx = SURFACE.get_rect().centerx

    total_right_percent = right_score / totalNum
    right_img = globalFont.render('正确率： ' + str(total_right_percent * 100) + ' %', True, color_dict['orange'])
    right_rect = right_img.get_rect()
    right_rect.top = 200
    right_rect.centerx = SURFACE.get_rect().centerx

    right_score_img = globalFont.render('正确题数： ' + str(right_score), True, color_dict['orange'])
    right_score_rect = right_score_img.get_rect()
    right_score_rect.top = 250
    right_score_rect.centerx = SURFACE.get_rect().centerx

    bg_img = pygame.image.load('img/end_bg.jpg').convert_alpha()
    bg_rect = bg_img.get_rect()
    bg_rect.center = SURFACE.get_rect().center

    bg_fill = pygame.Rect((0, 0), (400, 300))
    bg_fill.centerx = SURFACE.get_rect().centerx
    bg_fill.top = 80

    bt_back = pygame.Rect((0, 0), (180, 60))
    bt_back.centerx = SURFACE.get_rect().centerx - 120
    bt_back.bottom = 580
    back_img = globalFont.render('返回标题', True, color_dict['white'])
    back_rect = back_img.get_rect()
    back_rect.center = bt_back.center

    bt_exit = pygame.Rect((0, 0), (180, 60))
    bt_exit.centerx = SURFACE.get_rect().centerx + 120
    bt_exit.bottom = 580
    exit_img = globalFont.render('退出游戏', True, color_dict['white'])
    exit_rect = exit_img.get_rect()
    exit_rect.center = bt_exit.center

    while True:
        SURFACE.blit(bg_img, bg_rect)
        pygame.draw.rect(SURFACE, color_dict['white'], bg_fill)
        pygame.draw.rect(SURFACE, color_dict['gold'], bg_fill, 4)
        SURFACE.blit(score_img, score_rect)
        SURFACE.blit(right_score_img, right_score_rect)
        SURFACE.blit(right_img, right_rect)

        pygame.draw.rect(SURFACE, color_dict['orange'], bt_back)
        pygame.draw.rect(SURFACE, color_dict['orange'], bt_exit)

        for event in pygame.event.get():
            if event.type == QUIT:
                GlobalVar().close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    GlobalVar().close_program()
                elif event.key == K_RETURN:
                    return 'reset'
        pygame.mouse.set_visible(True)

        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if bt_back.left < x < bt_back.right and bt_back.top < y < bt_back.bottom:
            pygame.draw.rect(SURFACE, color_dict['lime'], bt_back)
            for event in pressed:
                if event == 1:
                    return 'reset'

        if bt_exit.left < x < bt_exit.right and bt_exit.top < y < bt_exit.bottom:
            pygame.draw.rect(SURFACE, color_dict['lime'], bt_exit)
            for event in pressed:
                if event == 1:
                    GlobalVar().close_program()

        SURFACE.blit(back_img, back_rect)
        SURFACE.blit(exit_img, exit_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)


def about_this():
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

    back_img = globalFont.render('返  回', True, color_dict['white'])
    back_rect = back_img.get_rect()
    back_rect.center = bt_back.center

    while True:
        SURFACE.fill(color_dict['black'])
        SURFACE.blit(bg, (0, 0))

        for item in aboutText:
            font_img = aboutFont.render(item, True, color_dict['red'])
            font_rect = font_img.get_rect()
            font_rect.top = 80 + aboutText.index(item) * 30
            font_rect.left = 80

            SURFACE.blit(font_img, font_rect)

        pygame.draw.rect(SURFACE, color_dict['lime'], bt_back)

        for event in pygame.event.get():
            if event.type == QUIT:
                GlobalVar().close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    GlobalVar().close_program()
                elif event.key == K_RETURN:
                    return 'reset'

        pygame.mouse.set_visible(True)

        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if bt_back.left < x < bt_back.right and bt_back.top < y < bt_back.bottom:
            pygame.draw.rect(SURFACE, color_dict['orange'], bt_back)
            for event in pressed:
                if event == 1:
                    return 'reset'

        SURFACE.blit(back_img, back_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)


def main():
    # 全局化声明
    global SURFACE, titleFont, globalFont, helpFont, color_dict, questionFont, answerFont, aboutFont, totalNum

    globalVar = GlobalVar()

    color_dict =globalVar.color_dict

    SURFACE = globalVar.SCREEN

    titleFont = globalVar.titleFont
    aboutFont = globalVar.aboutFont
    globalFont = globalVar.globalFont
    questionFont = globalVar.questionFont
    answerFont = globalVar.answerFont
    helpFont = globalVar.helpFont

    result = game_title()  # 游戏从初始的标题开始。所以这个直接载入，不需要添加到循环中去。
    totalNum = 8
    corrent = 0
    score = 0
    right_score = 0
    wrong_score = 0
    while True:
        if 'reset' in result:
            # 返回到游戏标题界面
            result = game_title()
        elif 'start' in result:
            gameLevels = globalVar.load_file("data.xml")  # 在点开始游戏的时候载入10道题
            pygame.time.wait(1000)  # 和答题同理
            corrent = 0
            result = load_game(SURFACE, globalVar, gameLevels, corrent, score, right_score, wrong_score)
        elif 'about' in result:
            result = about_this()
        elif result in ('next', 'yes', 'no'):
            pygame.time.wait(1000)  # 答题完成后，给定一个等待时间，有效防止题目下一题刷出来还没有看就点中了答案
            if result in 'yes':
                score += 100
                right_score += 1
            elif result in 'no':
                wrong_score += 1

            # 先计分，否则最后的统计会因为少统计了一条而出错
            if corrent == len(gameLevels) - 1:
                result = end_game(score, right_score, wrong_score)
            else:
                corrent += 1
                result = load_game(SURFACE, globalVar, gameLevels, corrent, score, right_score, wrong_score)
        else:
            pass

        pygame.display.update()
        pygame.time.Clock().tick(30)


if __name__ == '__main__':
    main()
