from json import loads

import pygame
import os
import sys
import random

from pygame.examples.cursors import image

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
camera_group = pygame.sprite.Group()

from load import *


class Portal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):
        self.animation()
        self.rect.x += step

    def animation(self):
        key = pygame.key.get_pressed()
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1


class StopEnemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):
        self.animation()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):
        self.animation()
        self.rect.x += step
        if self.dir == 1:
            self.rect.x += self.speed
        elif self.dir == -1:
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, stop_group, False):
            self.dir *= -1


class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):
        self.rect.x += step


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):

        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.earth - player.rect.earth) < 50):
                player.rect.left = self.rect.right


class Monetka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self, step):

        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):

                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.earth - player.rect.earth) < 50):
                player.rect.left = self.rect.right


class Fireball(pygame.sprite.Sprite):
    def __init__(self, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = fireball_image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.anime = True
        self.timer_anime = 0
        if dir == 'left':
            self.speed = -5
        else:
            self.speed = 5

    def update(self, step):
        self.animation()
        self.rect.x += step + self.speed
        if self.speed > 0:
            self.image = fireball_image[self.frame]
        else:
            self_image = pygame.transform.flip(fireball_image[self.frame], True, False)

    def animatoin(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(fireball_image) - 1:
                    self.kill()
                else:
                    self.frame += 1
                self.timer_anime = 0


class Hp(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


class Mp(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


class Qwest_1(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


class Flag(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


class Fire(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


class Nps(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = True
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
        self.key = pygame.key.get_pressed()
        self.dir = 'right'
        self.timer_attack = 0

    def update(self):

        self.animation()
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            print(self.rect.x)
            self.anime = True
            self.rect.x += self.speed
            self.image = player_image[self.frame]
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        if key[pygame.K_a]:
            self.anime = True
            self.rect.x -= self.speed
            self.image = player_image[-self.frame]
            if self.rect.left > 1000:
                self.rect.left = 1000
                camera_group.update(self.speed)
        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10

    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


def drawMaps(nameFile):
    maps = []
    source = str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == "3":
                earth = Earth(earth_image, pos)
                earth_group.add(earth)
                camera_group.add(earth)
            elif maps[i][j] == "1":
                box = Box(box_image, pos)
                box_group.add(box)
                camera_group.add(box)
            elif maps[i][j] == "2":
                center = Center(center_image, pos)
                center_group.add(center)
                camera_group.add(center)
            elif maps[i][j] == "4":
                water = Water(water_image, pos)
                water_group.add(water)
                camera_group.add(water)


def move(self):
    if self.key[pygame.K_d]:
        self.dir = 'right'
        self.anime = True
        self.image = player_image[self.frame]
        self.rect.x += self.speed
        if self.rect.right > 1000:
            self.rect.right = 1000
            camera_group.update(-self.speed)
    elif self.key[pygame.K_a]:
        self.image = pygame.transform.flip(player_image[self.frame], True, False)
        self.anime = True
        self.dir = 'left'
        self.rect.x -= self.speed
        if self.rect.left < 200:
            self.rect.left = 200
            camera_group.update(self.speed)
    else:
        self.anime = False


def jump(self):
    if self.key[pygame.K_SPACE] and self.on_ground:
        self.velocity_y = -15
        self.on_ground = False
    self.rect.y += self.velocity_y
    self.velocity_y += 1
    if self.velocity_y > 10:
        self.velocity_y = 10


def attack(self):
    self.timer_attack += 1
    if self.key[pygame.K_RETURN] and self.timer_attack / FPS > 1:
        fireball = Fireball(self.rect.center, self.dir)
        fireball_group.add(fireball)
        camera_group.add(fireball)
        self.timer_attack


def update(self, step):
    self.animation()
    self.attack()
    self.move()
    self.jump()
    self.key = pygame.key.get_pressed()


def draw_stats(self):
    width_hp = 96 * (self.hp / 180)
    width_mp = 96 * (self.mp / 180)
    pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 52, 180, 20), 2)
    pygame.draw.rect(sc, 'green', (self.rect.x - 27, self.rect.y - 50, width_hp, 15))

    pygame.draw.rect(sc, 'black', (self.rect.x - 30, self.rect.y - 30, 100, 10), 2)
    pygame.draw.rect(sc, 'blue', (self.rect.x - 27, self.rect.y - 27, width_mp, 6))





def restart():
    global player_group, earth_group, box_group, water_group, center_group, enemy_group, stop_group, monetka_group, portal_group, flag, hp, mp, qwest, player
    global flag_group,hp_group,mp_group,qwest_1_group,fireball_group,nps_group
    player_group = pygame.sprite.Group()
    earth_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    stop_group = pygame.sprite.Group()
    monetka_group = pygame.sprite.Group()
    flag_group = pygame.sprite.Group()
    hp_group = pygame.sprite.Group()
    mp_group = pygame.sprite.Group()
    qwest_1_group = pygame.sprite.Group()
    nps_group = pygame.sprite.Group()
    fireball_group = pygame.sprite.Group()

    nps = Nps(nps_image, (0, 480))
    nps_group.add(nps)
    player = Player(player_image, (300, 300))
    player_group.add(player)


def game_lvl():
    sc.fill('black')
    player_group.update()
    player_group.draw(sc)
    earth_group.update(0)
    earth_group.draw(sc)
    water_group.update(0)
    water_group.draw(sc)
    box_group.update(0)
    box_group.draw(sc)
    center_group.update(0)
    center_group.draw(sc)
    portal_group.update(0)
    portal_group.draw(sc)
    enemy_group.update(0)
    enemy_group.draw(sc)
    stop_group.update(0)
    stop_group.draw(sc)
    monetka_group.update(0)
    monetka_group.draw(sc)
    flag_group.update(0)
    flag_group.draw(sc)
    hp_group.update(0)
    hp_group.draw(sc)
    mp_group.update(0)
    mp_group.draw(sc)
    qwest_1_group.update(0)
    qwest_1_group.draw(sc)
    nps_group.update(0)
    nps_group.draw(sc)

    pygame.display.update()


restart()
drawMaps('1.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
