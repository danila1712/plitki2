import pygame
import os
import sys
import random



pygame.init()
FPS = 60
WIDTH = 1200
HEIGHT = 800
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
from load import *
def game_lvl():
    sc.fill('white')
    spawn.update()
    player_group.update()
    player_group.draw(sc)
    eyes_group.update()
    eyes_group.draw(sc)
    food_group.update()
    food_group.draw(sc)
    enemy_1_group.update()
    enemy_1_group.draw(sc)
    enemy_2_group.update()
    enemy_2_group.draw(sc)
    pygame.display.update()

def restart():
    global eyes_group, player_group, enemy_1_group,enemy_2_group,food_group, spawn
    eyes_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_1_group = pygame.sprite.Group()
    enemy_2_group = pygame.sprite.Group()
    food_group = pygame.sprite.Group()
    spawn = Spawn()
    player = Player(player_image, (100,100))
    player_group.add(player)

class Eyes(pygame.sprite.Sprite):
    def __init__(self,pos,block,type):
        pygame.sprite.Sprite.__init__(self)
        self.image = eyes_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.block = block
        self.type = type
        self.pos = pos
    def update(self):
        self.rect.center = self.block.rect.center
        if self.type == 1:
            if (
                pygame.sprite.spritecollide(self, food_group, False)
                and self.block.agr == False
            ):
                food = pygame.sprite.spritecollide(self,food_group, False )[0]
                self.block.agr = True
                self.block.food = food
        if self.type == 2:
            if (
                pygame.sprite.spritecollide(self, enemy_1_group, False)
                and self.block.agr == False
            ):
                food = pygame.sprite.spritecollide(self,enemy_1_group, False )[0]
                self.block.agr = True
                self.block.food = food



class Player(pygame.sprite.Sprite):
    def __init__(self, image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.pos = self.rect.center
        self.speed = 5
        self.pos_maps = 0
        self.dir = 0
        self.key = pygame.key.get_pressed()

    def update(self):
        self.key = pygame.key.get_pressed()

        if pygame.sprite.spritecollide(self,food_group, True):
            self.image = pygame.transform.rotozoom(self.image,0,1.05)
            self.pos = self.rect.center
            self.rect.center = self.pos
        if pygame.sprite.spritecollide(self,enemy_1_group,False):
            enemy = pygame.sprite.spritecollide(self,enemy_1_group,False)[0]
            if enemy.image.get_height() <= self.image.get_height():
                enemy.eyes.kill()
                enemy.kill()
                self.pos = self.rect.center
                self.image = pygame.transform.rotozoom(self.image,0,1.05)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

        if self.key[pygame.K_a]:
            self.dir = 'left'
            self.rect.x -= self.speed

        elif self.key[pygame.K_d]:
            self.dir = 'right'
            self.rect.x += self.speed

        elif self.key[pygame.K_w]:
            self.dir = 'top'
            self.rect.y -= self.speed

        elif self.key[pygame.K_s]:
            self.dir = 'bottom'
            self.rect.y += self.speed

class Enemy_1(pygame.sprite.Sprite):
    def __init__(self, image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = self.rect.center
        self.timer_move = 0
        self.speed_x = random.randint(-5,5)
        self.speed_y = random.randint(-5,5)
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(0, HEIGHT - 50)
        self.center = pos
        self.pos = pos
        self.food = None
        self.agr = False

    def update(self):
        self.timer_move += 1
        if self.timer_move / FPS > 3 and self.agr == False:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(-1, 1)
            self.timer_move = 0

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0:
            self.speed_x *= -1
        elif self.rect.top <= 0:
            self.speed_y *= -1
        elif self.rect.right >= WIDTH:
            self.speed_x *= -1
        elif self.rect.bottom >= HEIGHT:
            self.speed_y *= -1



        if self.agr:
            if self.rect.center[0] > self.food.rect.center[0]:
                self.speed_x = -1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1
            else:
                self.speed_x = 1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1

        if pygame.sprite.spritecollide(self,food_group,True):
            self.pos = self.rect.center
            self.image = pygame.transform.rotozoom(self.image, 0, 1.05)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

            self.eyes.pos = self.rect.center
            self.eyes.image = pygame.transform.rotozoom(self.eyes.image,0,1.05)
            self.eyes.rect = self.eyes.image.get_rect()
            self.eyes.rect.center = self.eyes.pos
            self.agr = False

class Enemy_2(pygame.sprite.Sprite):
    def __init__(self, image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = self.rect.center
        self.timer_move = 0
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(0, HEIGHT - 50)
        self.food = None
        self.agr = False

    def update(self):
        self.timer_move += 1
        if self.timer_move / FPS > 3:
            self.speed_x = random.randint(-5, 5)
            self.speed_y = random.randint(-5, 5)
            self.timer_move = 0
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0:
            self.speed_x *= -1
        elif self.rect.top <= 0:
            self.speed_y *= -1
        elif self.rect.right >= WIDTH:
            self.speed_x *= -1
        elif self.rect.bottom >= HEIGHT:
            self.speed_y *= -1


        if self.timer_move/FPS > 3 and self.agr == False:
            self.speed_x = random.randint(-1,1)
            self.speed_y = random.randint(-1,1)
            self.timer_move = 0

        if self.agr:
            if self.rect.center[0] > self.food.rect.center[0]:
                self.speed_x = -1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1
            else:
                self.speed_x = 1
                if self.rect.center[1] > self.food.rect.center[1]:
                    self.speed_y = -1
                else:
                    self.speed_y = 1

        if pygame.sprite.spritecollide(self, player_group, False):
            food = pygame.sprite.spritecollide(self, player_group, False)[0]
            if self.image.get_height() / food.image.get_height() > 0.5:
                food.player.kill()


        if pygame.sprite.spritecollide(self,enemy_1_group,False):
            food = pygame.sprite.spritecollide(self, enemy_1_group,False)[0]
            if self.image.get_height() / food.image.get_height() > 0.5:

                food.eyes.kill()
                food.kill()
                self.image = pygame.transform.rotozoom(self.image, 0,1.05)
                self.pos = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

                self.eyes.pos = self.rect.center
                self.eyes.image = pygame.transform.rotozoom(self.eyes.image,0,1.05)
                self.eyes.rect = self.eyes.image.get_rect()
                self.eyes.rect.center = self.eyes.pos
                self.agr = True
            else:
                self.agr = False

class Food(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-50)
        self.rect.y = random.randint(0,HEIGHT-50)

class Spawn():
    def __init__(self):
        self.timer  = 0

    def update(self):
        if len(food_group) < 20:
            food = Food(food_image)
            food_group.add(food)
        if len(enemy_1_group) < 5:
            pos = (random.randint(100,WIDTH - 100),random.randint(100,HEIGHT - 100 ))
            enemy = Enemy_1(enemy_1_image, pos)
            eyes = Eyes(enemy.rect.center, enemy, 1)
            enemy.eyes = eyes
            eyes_group.add(eyes)
            enemy_1_group.add(enemy)

        if len(enemy_2_group) < 5:
            pos = (random.randint(100,WIDTH - 100),random.randint(100,HEIGHT - 100))
            enemy = Enemy_2(enemy_2_image, pos)
            eyes = Eyes(enemy.rect.center,enemy,2)
            enemy.eyes = eyes
            eyes_group.add(eyes)
            enemy_2_group.add(enemy)

restart()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_lvl()
    clock.tick(FPS)