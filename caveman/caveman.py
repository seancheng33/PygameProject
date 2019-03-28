"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/3/16
@Program      : 小野人快跑的小游戏
"""
import pygame
from pygame.locals import *
from itertools import cycle
import random

SCREENWIDTH = 800
SCREENHEIGHT = 270

FPS = 30


class GameMap():
    def __init__(self, x, y):
        self.bg = pygame.image.load('images/bg.jpg')
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < - 790:
            self.x = 800
        else:
            self.x -= 5

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


class CaveMan():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpStatus = False
        self.jumpHeight = 140
        self.lowest_y = 140
        self.jumpValue = 0
        self.cavemanIndex = 0
        self.cavemanIndexGem = cycle([0, 1, 2])
        self.caveman_img = (pygame.image.load('images/caveman1.png').convert_alpha(),
                            pygame.image.load('images/caveman2.png').convert_alpha(),
                            pygame.image.load('images/caveman3.png').convert_alpha())
        self.jump_audio = pygame.mixer.Sound('audio/jump.wav')
        self.rect.size = self.caveman_img[0].get_size()
        self.x = 50
        self.y = self.lowest_y
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpStatus = True

    def move(self):
        if self.jumpStatus:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpStatus = False

    def draw_caveman(self):
        cavemanIndex = next(self.cavemanIndexGem)
        SCREEN.blit(self.caveman_img[cavemanIndex], (self.x, self.rect.y))


class Obstacle():
    score = 1

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.stone = pygame.image.load('images/Rock.png').convert_alpha()
        self.treeTall = pygame.image.load('images/Tree_Tall.png').convert_alpha()
        self.numbers = (pygame.image.load('images/0.png').convert_alpha(),
                        pygame.image.load('images/1.png').convert_alpha(),
                        pygame.image.load('images/2.png').convert_alpha(),
                        pygame.image.load('images/3.png').convert_alpha(),
                        pygame.image.load('images/4.png').convert_alpha(),
                        pygame.image.load('images/5.png').convert_alpha(),
                        pygame.image.load('images/6.png').convert_alpha(),
                        pygame.image.load('images/7.png').convert_alpha(),
                        pygame.image.load('images/8.png').convert_alpha(),
                        pygame.image.load('images/9.png').convert_alpha())
        self.score_audio = pygame.mixer.Sound('audio/score.wav')
        r = random.randint(0, 1)
        if r == 0:
            self.image = self.stone
        else:
            self.image = self.treeTall
        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size
        self.x = 800
        self.y = 200 - (self.height / 2)
        self.rect.center = (self.x, self.y)

    def obstacle_move(self):
        self.rect.x -= 5

    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def getScore(self):
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()
        self.score = 0
        return tmp

    def showScore(self, score):
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0
        for digit in self.scoreDigits:
            totalWidth += self.numbers[digit].get_width()
        Xoffset = (SCREENWIDTH - totalWidth) / 2
        for digit in self.scoreDigits:
            SCREEN.blit(self.numbers[digit], (Xoffset, SCREENHEIGHT * 0.1))
            Xoffset += self.numbers[digit].get_width()


def game_over():
    bump_audio = pygame.mixer.Sound('audio/gameover.wav')
    bump_audio.play()

    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    over_img = pygame.image.load('images/gameover.png').convert_alpha()

    SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2, (screen_h - over_img.get_height()) / 2))


def mainGame():
    score = 0
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption('小野人快跑')
    bg1 = GameMap(0, 0)
    bg2 = GameMap(800, 0)
    caveman = CaveMan()

    addObstacleTime = 0
    list = []

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                over = True
                pygame.quit()
                exit(0)
            if event.type == KEYUP and event.key == K_SPACE:
                if caveman.rect.y >= caveman.lowest_y:
                    caveman.jump()
                    caveman.jump_audio.play()
                if over == True:
                    mainGame()

        if over == False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()

            caveman.move()
            caveman.draw_caveman()
            if addObstacleTime >= 1300:
                r = random.randint(0, 100)
                if r > 40:
                    obstacle = Obstacle()
                    list.append(obstacle)
                addObstacleTime = 0
            for i in range(len(list)):
                list[i].obstacle_move()
                list[i].draw_obstacle()
                if pygame.sprite.collide_rect(caveman, list[i]):
                    over = True
                    game_over()
                else:
                    if (list[i].rect.x + list[i].rect.width) < caveman.rect.x:
                        score += list[i].getScore()

                list[i].showScore(score)

        addObstacleTime += 20

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    mainGame()
