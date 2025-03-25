import os
import pygame
def load_image(derictory):
    image_list = []
    print(os.listdir())
    files = os.listdir(derictory)
    for i in files:
        image = pygame.image.load(f'{derictory}/{i}').convert_alpha()
        image_list.append(image)
    return image_list