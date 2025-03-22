import pygame
from platformer.script import load_image
spider_image = load_image('image/spider')
spawner_image = pygame.image.load('block/spawner.png').convert_alpha()
block_image = pygame.image.load('block/block.jpg').convert_alpha()
#water_image = load_image('image/water').convert_alpha()
topor_image = pygame.image.load('image/topor/1.png').convert_alpha()
player_image_b = load_image('image/player/bottom')
player_image_t = load_image('image/player/top')
player_image_l = load_image('image/player/left')
player_image_r = load_image('image/player/right')
#player_image = pygame.image.load('image/player/bottom/1.png').convert_alpha()