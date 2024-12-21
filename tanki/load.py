import pygame
player_image = [pygame.image.load('image/player/player 1.png').convert_alpha(),
pygame.image.load('image/player/player 2.png').convert_alpha()]
brick_image = pygame.image.load('image/blocks/brick block.png').convert_alpha()
bush_image=pygame.image.load('image/blocks/bush block.png').convert_alpha()
flag_image=pygame.image.load('image/blocks/flag.png').convert_alpha()
iron_image=pygame.image.load('image/blocks/iron block.png').convert_alpha()
water_image=pygame.image.load('image/blocks/water block.png').convert_alpha()
enemy_image=pygame.image.load('image/enemy/enemy.png').convert_alpha()
enemy_bullet_image=pygame.image.load('image/enemy/enemy bullet.png').convert_alpha()
enemy2_image=pygame.image.load('image/enemy/enemy 2.png').convert_alpha()
bullet_player=pygame.image.load('image/player/player bullet.png').convert_alpha()
button_image = pygame.image.load('image/button/button.png').convert_alpha()
bullet_image = [pygame.image.load('image/player/boom/1.png').convert_alpha(),
                pygame.image.load('image/player/boom/2.png').convert_alpha(),
                pygame.image.load('image/player/boom/3.png').convert_alpha(),
                pygame.image.load('image/player/boom/4.png').convert_alpha()]
shot_sound = pygame.mixer.Sound('music/shot.mp3')
boom_sound = pygame.mixer.Sound('music/boom.mp3')