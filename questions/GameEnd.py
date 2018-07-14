'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/14
@Program      : 游戏结束和统计正确率的界面
'''
import pygame
from pygame.locals import *


def end_game(SURFACE, globalVar, score, right_score, totalNum):
    # 游戏的结束界面，对刚才完过的游戏做出一些数据统计。
    score_img = globalVar.globalFont.render('最终总成绩： ' + str(score), True, globalVar.color_dict['orange'])
    score_rect = score_img.get_rect()
    score_rect.top = 150
    score_rect.centerx = SURFACE.get_rect().centerx

    total_right_percent = right_score / totalNum
    right_img = globalVar.globalFont.render('正确率： ' + str(total_right_percent * 100) + ' %', True,
                                            globalVar.color_dict['orange'])
    right_rect = right_img.get_rect()
    right_rect.top = 200
    right_rect.centerx = SURFACE.get_rect().centerx

    right_score_img = globalVar.globalFont.render('正确题数： ' + str(right_score), True, globalVar.color_dict['orange'])
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
    back_img = globalVar.globalFont.render('返回标题', True, globalVar.color_dict['white'])
    back_rect = back_img.get_rect()
    back_rect.center = bt_back.center

    bt_exit = pygame.Rect((0, 0), (180, 60))
    bt_exit.centerx = SURFACE.get_rect().centerx + 120
    bt_exit.bottom = 580
    exit_img = globalVar.globalFont.render('退出游戏', True, globalVar.color_dict['white'])
    exit_rect = exit_img.get_rect()
    exit_rect.center = bt_exit.center

    while True:
        SURFACE.blit(bg_img, bg_rect)
        pygame.draw.rect(SURFACE, globalVar.color_dict['white'], bg_fill)
        pygame.draw.rect(SURFACE, globalVar.color_dict['gold'], bg_fill, 4)
        SURFACE.blit(score_img, score_rect)
        SURFACE.blit(right_score_img, right_score_rect)
        SURFACE.blit(right_img, right_rect)

        pygame.draw.rect(SURFACE, globalVar.color_dict['orange'], bt_back)
        pygame.draw.rect(SURFACE, globalVar.color_dict['orange'], bt_exit)

        for event in pygame.event.get():
            if event.type == QUIT:
                globalVar.close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    globalVar.close_program()
                elif event.key == K_RETURN:
                    return 'reset'
        pygame.mouse.set_visible(True)

        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if bt_back.left < x < bt_back.right and bt_back.top < y < bt_back.bottom:
            pygame.draw.rect(SURFACE, globalVar.color_dict['lime'], bt_back)
            for event in pressed:
                if event == 1:
                    return 'reset'

        if bt_exit.left < x < bt_exit.right and bt_exit.top < y < bt_exit.bottom:
            pygame.draw.rect(SURFACE, globalVar.color_dict['lime'], bt_exit)
            for event in pressed:
                if event == 1:
                    globalVar.close_program()

        SURFACE.blit(back_img, back_rect)
        SURFACE.blit(exit_img, exit_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)
