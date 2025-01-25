import pygame
import os
import sys
import random



pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 1000
FPS = 60
sc = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont('aria', 40)
lvl = 'menu'
clock = pygame.time.Clock()
from load import *

def startMenu():
    sc.fill('black')
    button_group.draw(sc)
    button_group.update()
    pygame.display.update()

def lvlGame():
    sc.fill("black")
    brick_group.update()
    brick_group.draw(sc)
    bush_group.update()
    bush_group.draw(sc)
    iron_group.update()
    iron_group.draw(sc)
    water_group.update()
    water_group.draw(sc)
    enemy_group.update()
    enemy_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    flag_group.update()
    flag_group.draw(sc)
    bullet_player_group.update()
    bullet_player_group.draw(sc)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(sc)
    pygame.display.update()

def drawMaps(nameFile):
    maps = []
    source = "game lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 25):
            maps.append(file.readline().replace("\n","").split(",")[0:-1])
    pos = [0,0]
    for i in range(0, len(maps)):
        pos[1] = i * 40
        for j in range(0, len(maps[0])):
            pos[0] = 40 * j

            if maps[i][j] == '1':
                brick = Brick(brick_image, pos)
                brick_group.add(brick)
            elif maps[i][j] == '2':
                bush = Bush(bush_image, pos)
                bush_group.add(bush)
            elif maps[i][j] == '3':
                iron = Iron(iron_image, pos)
                iron_group.add(iron)
            elif maps[i][j] == '4':
                water = Water(water_image, pos)
                water_group.add(water)
            elif maps[i][j] == '5':
                enemy = Enemy(enemy_image, pos)
                enemy_group.add(enemy)
            elif maps[i][j] == '7':
                flag = Flag(flag_image, pos)
                flag_group.add(flag)

class Brick(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self,player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player. dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "bottom":
                player.rect.bottom = self.rect.top
            if player.dir == "top":
                player.rect.top = self.rect.bottom
        if pygame.sprite.spritecollide(self, bullet_player_group, True):
            self.kill()
        if pygame.sprite.spritecollide(self, enemy_bullet_group, True):
            self.kill()
class Bush(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Iron(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "bottom":
                player.rect.bottom = self.rect.top
            if player.dir == "top":
                player.rect.top = self.rect.bottom


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self,player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player. dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "bottom":
                player.rect.bottom = self.rect.top
            if player.dir == "top":
                player.rect.top = self.rect.bottom


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.dir = "top"
        self.timer_shot = 0
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self):
        print(self.frame)
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.image = pygame.transform.rotate(player_image[self.frame], 90)
            self.rect.x -= self.speed
            self.dir = "left"
            self.anime = True

        elif key[pygame.K_s]:
            self.image = pygame.transform.rotate(player_image[self.frame], +180)
            self.rect.y += self.speed
            self.dir = "bottom"
            self.anime = True
        elif key[pygame.K_w]:
            self.image = pygame.transform.rotate(player_image[self.frame], 0)
            self.rect.y -= self.speed
            self.dir = "top"
            self.anime = True
        elif key[pygame.K_d]:
            self.image = pygame.transform.rotate(player_image[self.frame], -90)
            self.rect.x += self.speed
            self.dir = "right"
            self.anime = True
        else:
            self.anime = False
        self.timer_shot += 1
        if key[pygame.K_SPACE] and self.timer_shot / FPS > 1:
            bullet = Bullet_player(bullet_player, self.rect.center, self.dir)
            bullet_player_group.add(bullet)
            self.timer_shot = 0
            shot_sound.play()
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0




class Bullet_player(pygame.sprite.Sprite):
    def __init__(self, image ,pos ,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.dir = dir
        self.speed = 5
        self.anime = False
        self.timer_anime = 0
        self.frame = 0

    def update(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime/FPS > 0.1:
                if self.frame == len(bullet_image) - 1:
                    self.frame = 0
                    self.rect.center = (-1000,0)
                    self.kill()
                else:
                    self.frame += 1
                self.timer_anime = 0
            self.image = bullet_image[self.frame]
        if self.dir == 'top':
            self.rect.y -= self.speed
        elif self.dir == 'bottom':
            self.rect.y += self.speed
        elif self.dir == 'right':
            self.rect.x += self.speed
        elif self.dir == 'left':
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, iron_group, False):
            self.anime = True
            self.speed = 0
            self.kill()
        if pygame.sprite.spritecollide(self, flag_group, True):
            self.anime = True
            self.speed = 0
            self.kill()
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.anime = True
            self.speed = 0
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = "top"
        self.timer_move = 0
        self.timer_shot=0

    def update(self):
        self.timer_move += 1
        if self.timer_move / FPS > 2:
            if random.randint(1, 4)== 1:
                self.dir = "top"
            elif random.randint(1, 4)== 2:
                self.dir = "right"
            elif random.randint(1, 4) == 3:
                self.dir = "left"
            elif random.randint(1, 4) == 4:
                self.dir = "bottom"
            self.timer_move = 0


        if self.dir == "top":
            self.image = pygame.transform.rotate(enemy_image, 360)
            self.rect.y -= self.speed
        elif self.dir == "right":
            self.image = pygame.transform.rotate(enemy_image, -90)
            self.rect.x += self.speed
        elif self.dir == "bottom":
            self.image = pygame.transform.rotate(enemy_image, +180)
            self.rect.y += self.speed
        elif self.dir == "left":
            self.image = pygame.transform.rotate(enemy_image, 90)
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self,brick_group,False) or  pygame.sprite.spritecollide(self,iron_group,False) or  pygame.sprite.spritecollide(self,water_group,False):
            self.timer_move = 0
            print(self.dir)
            if self.dir =="top":
                self.dir ="bottom"
            elif self.dir =="bottom":
                self.dir ="top"
            elif self.dir =="right":
                self.dir ="left"
            elif self.dir =="left":
                self.dir ="right"
        if pygame.sprite.spritecollide(self, bullet_player_group, True):
            self.kill()
        self.timer_shot += 1
        if self.timer_shot / FPS > 1:
            bullet_2 = Enemy_bullet(enemy_bullet_image, self.rect.center, self.dir)
            enemy_bullet_group.add(bullet_2)
            self.timer_shot = 0

class Enemy_bullet(pygame.sprite.Sprite):
    def __init__(self, image ,pos ,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.dir = dir
        self.speed = 5
        self.boom = False
    def update(self):
        global lvl
        if self.dir == 'top':
            self.rect.y -= self.speed
        elif self.dir == 'bottom':
            self.rect.y += self.speed
        elif self.dir == 'right':
            self.rect.x += self.speed
        elif self.dir == 'left':
            self.rect.x -= self.speed
        d = ((self.rect.center[0] - player.rect.center[0])) ** 2
        + (self.rect.center[1] - player.rect.center[1]) ** 2 ** (1 / 2)
        if self.boom:
            boom_sound.play()
            self.boom = False
        if pygame.sprite.spritecollide(self, iron_group, False):
            self.boom = True
            self.kill()
        if pygame.sprite.spritecollide(self, flag_group, True):
            self.boom = True
            self.kill()
        if pygame.sprite.spritecollide(self, player_group, True):
            self.boom = True
            self.kill()
            lvl ='menu'


class Flag(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, bullet_player_group, True):
            self.kill()

class Button(pygame.sprite.Sprite):
    def __init__(self,image,pos,next_lvl,text):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.next_lvl = next_lvl
        self.text = text

    def update(self):
        global lvl
        text_render = font.render(self.text,True,'white')
        sc.blit(text_render,(self.rect.x + 80, self.rect.y + 5))
        click = pygame.mouse.get_pos()


        if pygame.mouse.get_pressed()[0]:
            if self.rect.left < click[0] < self.rect.right and self.rect.top <click[1] < self.rect.bottom:
                lvl = self.next_lvl
                if lvl == 'game':
                    restart()
                    drawMaps('1.txt')

def restart():
    global water_group, brick_group, bush_group,iron_group,button_group
    global player_group, enemy_group,flag_group,bullet_player_group,enemy_bullet_group,player
    bullet_player_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    bush_group = pygame.sprite.Group()
    iron_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    flag_group = pygame.sprite.Group()
    player = Player(player_image, (200, 640))
    player_group.add(player)
    enemy_bullet_group = pygame.sprite.Group()

button_group = pygame.sprite.Group()
button_start = Button(button_image, (500,100), 'game','start')
button_group.add(button_start)
button_exit = Button(button_image, (500,180), 'exit','exit')
button_group.add(button_exit)
restart()
drawMaps('1.txt')


    clock.tick(FPS)while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl == "game":
        lvlGame()
    elif lvl == 'menu':
        startMenu()
    elif lvl == 'exit':
        pygame.quit()
        sys.exit()