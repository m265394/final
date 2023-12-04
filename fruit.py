import pygame
import random

from game_parameters import *

MIN_SPEED = 0.5
MAX_SPEED = 3.0

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/object_blue.png").convert()
        self.image = pygame.transform.scale(self.image, (SKY_TILE, SKY_TILE))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.position = [x, y]
        self.acceleration = [0, .2]  # x acceleration, y acceleration

        # adjust velocity based on direction
        if direction == 'right':
            self.velocity = [random.randint(2,7), -.5]  # x velocity, y velocity towards right
        elif direction == 'left':
            self.velocity = [-(random.randint(2, 7)), -.5]  # x velocity, y velocity towards left

    def update(self):
        self.position[0] += self.velocity[0]  # adjust the x position based on the x velocity
        self.position[1] += self.velocity[1]  # adjust the y position based on the y velocity
        self.velocity[1] += self.acceleration[1]  # update the y velocity based on y acceleration
        self.rect.topleft = self.position  # update the rect based on the new position
    # def update_right(self):
    #     self.position[0] += self.velocity_left[0]  # adjust the x position based on the x velocity
    #     self.position[1] += self.velocity_left[1]  # adjust the y position based on the y velocity
    #     self.velocity_right[0] += self.acceleration[0]  # update the x velocity based on x acceleration
    #     self.velocity_right[1] += self.acceleration[1]  # update the y velocity based on y acceleration
    #     self.rect.topleft = self.position  # update the rect based on the new position

    def draw(self, land):
        land.blit(self.image, self.rect)

fruits_left = pygame.sprite.Group()
fruits_right = pygame.sprite.Group()
