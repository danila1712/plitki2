import pygame
import os
import sys

from pygame import font

pygame.init()
WIDTH = 1280
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
lvl_game = 'game'
from load import *

def restart():
    global scorpion_group,tower_group,tower_1_group,bullet_group,bullet_1_group,edit_dir_group,bush_group,bush_tower_group,grass_group,panel_group
    scorpion_group = pygame.sprite.Group()
    tower_group = pygame.sprite.Group()
    tower_1_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    bullet_1_group = pygame.sprite.Group()
    edit_dir_group = pygame.sprite.Group()

    bush_group = pygame.sprite.Group()
    bush_tower_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    panel_group = pygame.sprite.Group()

def drawMaps():
    maps = []
    source = "game lvl/" + str()
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n","").split(",")[0:-1])
    pos = [0,0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j

            if maps[i][j] == '1':
                bottom = Edit_dir_tile(bottom_image, pos, 'bottom')
                edit_dir_group.add(bottom)
            elif maps[i][j] == '2':
                top = Edit_dir_tile(top_image, pos, 'top')
                edit_dir_group.add(top)
            elif maps[i][j] == '3':
                left = Edit_dir_tile(left_image, pos, 'left')
                edit_dir_group.add(left)
            elif maps[i][j] == '4':
                right = Edit_dir_tile(right_image, pos, 'right')
                edit_dir_group.add(right)
            elif maps[i][j] == '5':
                bush = Bush(bush_image, pos)
                bush_group.add(bush)
            elif maps[i][j] == '6':
                bush_tower = Bush_tower(bush_tower_image, pos)
                bush_tower_group.add(bush_tower)
            elif maps[i][j] == '7':
                grass = Grass(grass_image, pos)
                grass_group.add(grass)
            elif panel[i][j] == '8':
                panel = panel(panel_image, pos)
                panel_group.add(panel)

def game_lvl():
    sc.fill('Black')
    scorpion_group.update()
    scorpion_group.draw(sc)
    bush_group.update()
    bush_group.draw(sc)
    bush_tower_group.update()
    bush_tower_group.draw(sc)
    grass_group.update()
    grass_group.draw(sc)
    panel_group.update()
    panel_group.draw(sc)
    tower_group.update()
    tower_group.draw(sc)
    tower_1_group.update()
    tower_1_group.draw(sc)
    bullet_group.update()
    bullet_group.draw(sc)
    bullet_1_group.update()
    bullet_1_group.draw(sc)
    edit_dir_group.update()
    edit_dir_group.draw(sc)

    pygame.display.update()



class Scorpoin(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.dir = 'right'
        self.speedx = 2
        self.speedy = 0

    def update(self):
        if self.dir == 'right':
            self.speedx = 2
            self.speedy = 0
            self.image = pygame.transform.rotate(scorpion_image, 90)
        if pygame.sprite.spritecollide(self,edit_dir_group,False):
            tile = pygame.sprite.spritecollide(self,edit_dir_group,False)[0]
            if abs(self.rect.centerx - tile.rect.centerx) <= 5 and abs(self.rect.centery - tile.rect.centery) <= 5:
                self.dir = tile.dir

class Tower(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Tower_sale(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.buy = False
        self.timer_click = 0

class Tower_1(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Bullet_1(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Edit_dir_tile(pygame.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir


class Bush(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Bush_tower(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Grass(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Panel(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            game()

    clock.tick(FPS)