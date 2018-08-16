'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/15
@Program      : 自己活动的NPC的功能实现。
'''

import pygame


class NPCRole():
    def __init__(self,image,):
        self.npc_img = pygame.image.load(image).convert_alpha()


    def auto_move(self):
        pass