import pygame
import random

from game_parameters import *

MIN_SPEED = 0.5
MAX_SPEED = 3.0

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/object_blue.png").convert()
        self.image = pygame.transform.scale(self.image, (SKY_TILE, SKY_TILE))
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, land):
        land.blit(self.image, self.rect)

fruits_left = pygame.sprite.Group()
fruits_right = pygame.sprite.Group()