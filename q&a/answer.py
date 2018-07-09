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
from xml.dom.minidom import parse


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
                close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    close_program()

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


def load_game(gameLevels,current, total_score, total_right_score, total_wrong_score):
    SURFACE.fill(color_dict['black'])
    title_bg = pygame.image.load('img/title.jpg')

    level = gameLevels[current]
    level_question = level['question']
    level_answer = level['answers']
    level_correct = int(level['correct'])

    bt_replay = pygame.Rect((0, 0), (220, 50))
    bt_replay.left = 730
    bt_replay.top = 400
    replay_img = globalFont.render('重新开始', True, color_dict['white'])
    replay_rect = replay_img.get_rect()
    replay_rect.center = bt_replay.center

    bt_exit = pygame.Rect((0, 0), (220, 50))
    bt_exit.left = 730
    bt_exit.top = 480
    exit_img = globalFont.render('结束游戏', True, color_dict['white'])
    exit_rect = exit_img.get_rect()
    exit_rect.center = bt_exit.center

    mouseCursor = pygame.image.load('img/cursor.png').convert_alpha()  # 载入鼠标的图片

    while True:

        SURFACE.blit(title_bg, (0, 0))

        # 显示出问题,按照宽度是25个字符串的规格显示出来。
        for i in range(int(len(level_question) / 25 + 1)):
            start = i * 25
            end = (i + 1) * 25
            question_image = questionFont.render(level_question[start:end], True, color_dict['black'])
            SURFACE.blit(question_image, (50, 80 + (i * 30)))

        # 右侧的内容
        level_image = helpFont.render('当前题目：第 ' + str(current + 1) + ' 题', True, color_dict['orange'])
        SURFACE.blit(level_image, (725, 80))
        score_image = helpFont.render('当前分数：' + str(total_score), True, color_dict['orange'])
        SURFACE.blit(score_image, (725, 120))
        score_image = helpFont.render('正确题数：' + str(total_right_score), True, color_dict['orange'])
        SURFACE.blit(score_image, (725, 160))
        score_image = helpFont.render('错误题数：' + str(total_wrong_score), True, color_dict['orange'])
        SURFACE.blit(score_image, (725, 200))

        # 显示出答案选项
        item1_image = answerFont.render('1 - ' + level_answer[0], True, color_dict['red'])
        item1_rect = item1_image.get_rect()
        item1_rect.left = 50
        item1_rect.top = 310
        item2_image = answerFont.render('2 - ' + level_answer[1], True, color_dict['red'])
        item2_rect = item2_image.get_rect()
        item2_rect.left = 50
        item2_rect.top = 380
        item3_image = answerFont.render('3 - ' + level_answer[2], True, color_dict['red'])
        item3_rect = item3_image.get_rect()
        item3_rect.left = 50
        item3_rect.top = 450
        item4_image = answerFont.render('4 - ' + level_answer[3], True, color_dict['red'])
        item4_rect = item4_image.get_rect()
        item4_rect.left = 50
        item4_rect.top = 520

        SURFACE.blit(item1_image, item1_rect)
        SURFACE.blit(item2_image, item2_rect)
        SURFACE.blit(item3_image, item3_rect)
        SURFACE.blit(item4_image, item4_rect)

        pygame.draw.rect(SURFACE, color_dict['lime'], bt_replay)
        pygame.draw.rect(SURFACE, color_dict['lime'], bt_exit)

        for event in pygame.event.get():
            # 关闭按钮的事件
            if event.type == QUIT:
                close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    close_program()
                # elif event.key == K_BACKSPACE:
                #     # 按回退键，返回到标题界面。
                #     return 'reset'
                # elif event.key == K_RETURN:
                #     # 按回车键，跳到下一题。
                #     return 'next'

        # 鼠标控制事件
        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        # 四个答案区域的内容的鼠标鼠标时间控制
        if item1_rect.left < x < item1_rect.right and item1_rect.top < y < item1_rect.bottom:
            item1_image = answerFont.render('1 - ' + level_answer[0], True, color_dict['gold'])
            SURFACE.blit(item1_image, item1_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 1:
                        return 'yes'
                    else:
                        return 'no'
        if item2_rect.left < x < item2_rect.right and item2_rect.top < y < item2_rect.bottom:
            item2_image = answerFont.render('2 - ' + level_answer[1], True, color_dict['gold'])
            SURFACE.blit(item2_image, item2_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 2:
                        return 'yes'
                    else:
                        return 'no'
        if item3_rect.left < x < item3_rect.right and item3_rect.top < y < item3_rect.bottom:
            item3_image = answerFont.render('3 - ' + level_answer[2], True, color_dict['gold'])
            SURFACE.blit(item3_image, item3_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 3:
                        return 'yes'
                    else:
                        return 'no'
        if item4_rect.left < x < item4_rect.right and item4_rect.top < y < item4_rect.bottom:
            item4_image = answerFont.render('4 - ' + level_answer[3], True, color_dict['gold'])
            SURFACE.blit(item4_image, item4_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 4:
                        return 'yes'
                    else:
                        return 'no'
        # 右侧按键的鼠标事件
        if bt_replay.left < x < bt_replay.right and bt_replay.top < y < bt_replay.bottom:
            pygame.draw.rect(SURFACE, color_dict['orange'], bt_replay)
            for event in pressed:
                if event == 1:
                    return 'reset'
        if bt_exit.left < x < bt_exit.right and bt_exit.top < y < bt_exit.bottom:
            pygame.draw.rect(SURFACE, color_dict['orange'], bt_exit)
            for event in pressed:
                if event == 1:
                    close_program()

        SURFACE.blit(replay_img, replay_rect)
        SURFACE.blit(exit_img, exit_rect)

        # 自定义鼠标样式
        pygame.mouse.set_visible(False)
        x -= 0
        y -= 0
        SURFACE.blit(mouseCursor, (x, y))

        pygame.display.update()
        pygame.time.Clock().tick(30)


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
                close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    close_program()
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
                    close_program()

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
                close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    close_program()
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


def close_program():
    pygame.quit()
    sys.exit(0)


def load_file(filename):
    assert os.path.exists(filename), '题库文件: %s 不存在，游戏无法执行。' % (filename)
    # 读取xml文件中的题库
    question_data = parse(filename)
    # 得到根节点
    root = question_data.documentElement

    game_level = []
    questions = root.getElementsByTagName("question")

    for item in questions:
        q_list = {}
        answerList = []
        question = item.getAttribute("title")
        answer_items = item.getElementsByTagName("answer")  # 返回一个列表
        answerList.append(answer_items[0].getElementsByTagName("a")[0].childNodes[0].data)
        answerList.append(answer_items[0].getElementsByTagName("b")[0].childNodes[0].data)
        answerList.append(answer_items[0].getElementsByTagName("c")[0].childNodes[0].data)
        answerList.append(answer_items[0].getElementsByTagName("d")[0].childNodes[0].data)
        correct = item.getElementsByTagName("correct")[0].childNodes[0].data
        q_list['question'] = question
        q_list['answers'] = answerList
        q_list['correct'] = correct
        game_level.append(q_list)

    # 生产随机指定数量的题集，利用set的去重特性，这样当set的长度是10时，就是10个不重复的数字
    tmp_level = set()
    while len(tmp_level) < totalNum:
        randomNum = random.randint(0, len(game_level) - 1)  # 生产随机数
        tmp_level.add(randomNum)

    new_question = []
    for i in tmp_level:
        new_question.append(game_level[i])

    # 因为set的缘故，提取出来的题目是按顺序排列的，需要打乱一次,形成每次游戏时的题目顺序的独特随机性
    random.shuffle(new_question)

    return new_question


def main():
    # 全局化声明
    global SURFACE, titleFont, globalFont, helpFont, color_dict, questionFont, answerFont, aboutFont, totalNum

    # 颜色字典
    color_dict = {'red': (255, 0, 0),  # 纯红
                  'blue': (255, 0, 0),  # 纯蓝
                  'green': (0, 125, 0),  # 纯绿
                  'lime': (0, 255, 0),  # 酸橙色
                  'gold': (255, 215, 0),  # 金色
                  'orange': (255, 165, 0),  # 橙色
                  'black': (0, 0, 0),  # 纯黑
                  'white': (255, 255, 255),  # 纯白
                  }

    # 初始化
    pygame.init()
    SURFACE = pygame.display.set_mode((1024, 640))
    pygame.display.set_icon(pygame.image.load('img/delbrucks-brain.ico'))
    pygame.display.set_caption('大脑很囧--答题类游戏 Version 1.0.0')

    titleFont = pygame.font.Font('font/YaHei.ttf', 150)
    aboutFont = pygame.font.Font('font/YaHei.ttf', 20)
    globalFont = pygame.font.Font('font/Hei.ttf', 36)
    questionFont = pygame.font.Font('font/HuaKanSong.ttf', 24)
    answerFont = pygame.font.Font('font/HuaKanSong.ttf', 22)
    helpFont = pygame.font.Font('font/HuaKanSong.ttf', 24)

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
            gameLevels = load_file("data.xml")  # 在点开始游戏的时候载入10道题
            pygame.time.wait(1000)  # 和答题同理
            corrent = 0
            result = load_game(gameLevels, corrent, score, right_score, wrong_score)
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
                result = load_game(gameLevels, corrent, score, right_score, wrong_score)
        else:
            pass

        pygame.display.update()
        pygame.time.Clock().tick(30)


if __name__ == '__main__':
    main()
