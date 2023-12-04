import pygame
import random

from game_parameters import *

MIN_SPEED = 0.5
MAX_SPEED = 3.0

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image_reverse = pygame.image.load("assets/sprites/object_bomb_small.png").convert()
        self.image_reverse = pygame.transform.scale(self.image_reverse, (SKY_TILE, SKY_TILE))
        self.image_reverse.set_colorkey((0, 0, 0))
        self.image_forward = pygame.transform.flip(self.image_reverse, True, False)
        self.image = self.image_reverse
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.position = [x, y]
        self.acceleration = [0, .2]  # x acceleration, y acceleration
        self.step = .65

        # adjust velocity based on direction
        if direction == 'right':
            self.velocity = [random.randint(1, 4), -.5]  # x velocity, y velocity towards right
            self.image = self.image_reverse

        elif direction == 'left':
            self.velocity = [-(random.randint(1, 4)), -.5]  # x velocity, y velocity towards left
            self.image = self.image_forward

    def update(self):
        self.position[0] += self.velocity[0] * self.step # adjust the x position based on the x velocity
        self.position[1] += self.velocity[1] * self.step # adjust the y position based on the y velocity
        self.velocity[1] += self.acceleration[1]  # update the y velocity based on y acceleration
        self.rect.topleft = self.position  # update the rect based on the new position

    def draw(self, land):
        land.blit(self.image, self.rect)

bombs_left = pygame.sprite.Group()
bombs_right = pygame.sprite.Group()