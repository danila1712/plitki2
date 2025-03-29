import pygame
import sys

pygame.init()
WIDTH = 1280
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
lvl_game = 'game'
from load import *
timer_spawn = 0
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

def drawMaps(file):
    maps = []
    source = "game lvl/" + str(file)
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
                bush = Bush(bush_image, pos)
                bush_group.add(bush)

            elif maps[i][j] == '3':
                bush_tower = Bush_tower(bush_tower_image, pos)
                bush_tower_group.add(bush_tower)
            elif maps[i][j] == '4':
                left = Edit_dir_tile(left_image, pos, 'left')
                edit_dir_group.add(left)
            elif maps[i][j] == '5':
                grass = Grass(grass_image, pos)
                grass_group.add(grass)
            elif maps[i][j] == '6':
                right = Edit_dir_tile(right_image, pos, 'right')
                edit_dir_group.add(right)
            elif maps[i][j] == '7':
                top = Edit_dir_tile(top_image, pos, 'top')
                edit_dir_group.add(top)
            elif maps[i][j] == '8':
                panel = Panel(panel_image, pos)
                panel_group.add(panel)

def game_lvl():
    sc.fill('Blue')

    bush_group.update()
    bush_group.draw(sc)
    grass_group.update()
    grass_group.draw(sc)
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
    panel_group.update()
    panel_group.draw(sc)
    scorpion_group.update()
    scorpion_group.draw(sc)
    panel_group.update()
    panel_group.draw(sc)
    bush_tower_group.update()
    bush_tower_group.draw(sc)
    pygame.display.update()

class Scorpoin(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.dir = 'right'
        self.speedx = 2
        self.speedy = 0

        self.timer_spawn = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.dir == 'right':
            self.speedx = 2
            self.speedy = 0
            self.image = pygame.transform.rotate(scorpion_image[0], 90)
        if self.dir == 'top':
            self.speedx = 0
            self.speedy = -2
            self.image = pygame.transform.rotate(scorpion_image[0], 90)
        if self.dir == 'left':
            self.speedx = -2
            self.speedy = 0
            self.image = pygame.transform.rotate(scorpion_image[0], 90)
        if self.dir == 'bottom':
            self.speedx = 0
            self.speedy = 2
            self.image = pygame.transform.rotate(scorpion_image[0], 90)
        if pygame.sprite.spritecollide(self,edit_dir_group,False):
            tile = pygame.sprite.spritecollide(self,edit_dir_group,False)[0]
            if abs(self.rect.centerx - tile.rect.centerx) <= 5 and abs(self.rect.centery - tile.rect.centery) <= 5:
                self.dir = tile.dir

class Hp(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image

class Money(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image



class Tower(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

class Tower_1(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
    def update(self):
         pass

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
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_lvl()
    timer_spawn+=1
    if timer_spawn / FPS >1:
        scorpion = Scorpoin(scorpion_image, (10,360))
        scorpion_group.add(scorpion)
        timer_spawn = 0
    clock.tick(FPS)