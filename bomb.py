import pygame
import random

from game_parameters import *

MIN_SPEED = 0.5
MAX_SPEED = 3.0

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_reverse = pygame.image.load("assets/sprites/object_bomb_small.png").convert()
        self.image_reverse = pygame.transform.scale(self.image_reverse, (SKY_TILE, SKY_TILE))
        self.image_reverse.set_colorkey((0, 0, 0))
        self.image_forward = pygame.transform.flip(self.image_reverse, True, False)
        self.image = self.image_reverse
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, land):
        land.blit(self.image, self.rect)

bombs_left = pygame.sprite.Group()
bombs_right = pygame.sprite.Group()