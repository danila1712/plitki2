import pygame
import os
import sys
from math import cos, sin, radians
from random import randint
import random


#from RPG 2d .loadimport player_image

pygame.init()
FPS = 60
WIDTH = 1200
HEIGHT = 800
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
from load import *
class Camera():
    def camera_move(self,stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy
def game_lvl():
    sc.fill('grey')
    spider_group.update()
    spider_group.draw(sc)
    spawner_group.update()
    spawner_group.draw(sc)
    block_group.update()
    block_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    topor_group.update()
    topor_group.draw(sc)
    pygame.display.update()


def restart():
    global topor_group, player_group, player, spawner_group, block_group, camera_group, spider_group
    spider_group = pygame.sprite.Group()
    topor_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    spawner_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    camera_group = SuperGroup()
    player = Player(player_image_b[0], (100,100))
    player.add_topor()
    player_group.add(player)


def drawmaps(nameFile):
    maps = []
    source = "" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 100):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j

            if maps[i][j] == '1':
                block = Block(block_image, pos)
                block_group.add(block)
                camera_group.add(block)

            elif maps[i][j] == '2':
                spawner = Spawner(spawner_image, pos)
                spawner_group.add(spawner)
                camera_group.add(spawner)

class Spider(pygame.sprite.Sprite,Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.timer_move = 0
        self.speedx = random.choice((-1, 1))
        self.speedy = random.choice((-1, 1))
        self.timer_anime = 0
        self.frame = 0
        self.anime = True
        self.bonus_topor = 0

    def update(self):
        self.move()
        self.collide()
        self.animation()

    def move(self):
        self.timer_move += 1
        if self.timer_move / FPS > 2:
            self.speedx = random.choice((-1,1))
            self.speedy = random.choice((-1,1))
            self.timer_move = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if pygame.sprite.spritecollide(self, topor_group, False):
        
            self.kill()

    def collide(self):
        if pygame.sprite.spritecollide(self,block_group, False):
            self.speedy *= -1
            self.speedx *= -1

    def animation(self):
        self.image = spider_image[self.frame]
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(spider_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class SuperGroup(pygame.sprite.Group):
    def camera_update(self, stepx, stepy):
        for sprite in self.sprites():
            sprite.camera_move(stepx,stepy)


class Spawner(pygame.sprite.Sprite,Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.timer_spawn = 0

    def update(self):
        if 0 < self.rect.centerx < 1200 and 0 < self.rect.centery < 800:
            self.timer_spawn += 1
            if self.timer_spawn / FPS > 1:
                spider = Spider(spider_image[0],self.rect.center)
                spider_group.add(spider)
                camera_group.add(spider)
                self.timer_spawn = 0

class Block(pygame.sprite.Sprite,Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.dir = 0

    def update(self):

        if pygame.sprite.spritecollide(self, player_group, False):
                if player.dir == "left":
                    player.rect.left = self.rect.right
                if player.dir == "right":
                    player.rect.right = self.rect.left
                if player.dir == "top":
                    player.rect.top = self.rect.bottom
                if player.dir == "bottom":
                    player.rect.bottom = self.rect.top


class Bonus_topor(pygame.sprite.Sprite,Camera):
    def __init__(self, image, pos, start_deg):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]


class Topor(pygame.sprite.Sprite):
    def __init__(self, image, pos, start_deg):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.deg_rotate = 0
        self.deg = start_deg
        self.timer_attack = 0
    def update(self):
        self.rotate()
        self.move()
    def rotate(self):
        self.deg_rotate -= 20
        self.image = pygame.transform.rotate(topor_image, self.deg_rotate)

    def move(self):
        self.deg += 3
        self.rect.centerx = 150 * cos(radians(self.deg)) + player.rect.centerx
        self.rect.centery = 150 * sin(radians(self.deg)) + player.rect.centery

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.key = pygame.key.get_pressed()
        self.speed = 5
        self.timer_anime = 0
        self.anime = False
        self.frame = 0
        self.pos_maps = [0, 0]
        self.score = 0
        self.topor = 1
        self.animation()
        self.speed = 10
        self.dir = 'bottom'

    def add_topor(self):
        global topor_group
        topor_group = pygame.sprite.Group()
        for i in range(self.topor):
            topor = Topor(topor_image, (self.rect.centerx + 70, self.rect.centery + 70), (360 // self.topor * i))
            topor_group.add(topor)


    def update(self):
        self.animation()
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_a]:
            self.dir = 'left'
            self.rect.x -= self.speed
            if self.rect.left < 300 and self.pos_maps[0] < 0:
                self.pos_maps[0] += self.speed
                camera_group.camera_update(self.speed, 0)
                self.rect.left = 300

        elif self.key[pygame.K_d]:
            self.dir = 'right'
            self.rect.x += self.speed
            if self.rect.right > 900 and self.pos_maps[0] > -6800:
                self.pos_maps[0] -= self.speed
                camera_group.camera_update(-self.speed, 0)
                self.rect.right = 900

        elif self.key[pygame.K_w]:
            self.dir = 'top'
            self.rect.y -= self.speed
            if self.rect.top < 300 and self.pos_maps[1] < 0:
                self.pos_maps[1] += self.speed
                camera_group.camera_update(0, self.speed)
                self.rect.top = 300

        elif self.key[pygame.K_s]:
            self.dir = 'bottom'
            self.rect.y += self.speed
            if self.rect.bottom > 600 and self.pos_maps[1] > -7200:
                self.pos_maps[1] -= self.speed
                camera_group.camera_update(0,-self.speed)
                self.rect.bottom = 600

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image_b) + 1:
                    self.frame = 0
                elif self.frame == len(player_image_t) - 1:
                    self.timer_anime = 0
                elif self.frame == len(player_image_l) - 1:
                    self.timer_anime = 0
                elif self.frame == len(player_image_r) + 1:
                    self.timer_anime = 0



restart()
drawmaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_lvl()
    clock.tick(FPS)
