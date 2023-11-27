

import pygame
from game_parameters import *
import time

class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_idle = pygame.image.load("assets/sprites/player_1_idle.png").convert()
        self.image_idle = pygame.transform.scale(self.image_idle, (TILE_SIZE, TILE_SIZE) )
        self.image_idle.set_colorkey((0, 0, 0))
        self.image_forward = pygame.image.load("assets/sprites/player_1_walk.png").convert()
        self.image_forward = pygame.transform.scale(self.image_forward, (TILE_SIZE, TILE_SIZE))
        self.image_forward.set_colorkey((0, 0, 0))
        self.image_reverse = pygame.transform.flip(self.image_forward, True, False)
        self.image_reverse = pygame.transform.scale(self.image_reverse, (TILE_SIZE, TILE_SIZE))
        self.image_reverse.set_colorkey((0, 0, 0))
        self.image_hurt_idle = pygame.image.load("assets/sprites/player_1_robot_idle.png").convert()
        self.image_hurt_idle = pygame.transform.scale(self.image_hurt_idle, (TILE_SIZE, TILE_SIZE))
        self.image_hurt_idle.set_colorkey((0, 0, 0))
        self.image_hurt_forward = pygame.image.load("assets/sprites/player_1_robot_walk.png").convert()
        self.image_hurt_forward = pygame.transform.scale(self.image_hurt_forward, (TILE_SIZE, TILE_SIZE))
        self.image_hurt_forward.set_colorkey((0, 0, 0))
        self.image_hurt_reverse = pygame.transform.flip(self.image_forward, True, False)
        self.image_hurt_reverse = pygame.transform.scale(self.image_hurt_reverse, (TILE_SIZE, TILE_SIZE))
        self.image_hurt_reverse.set_colorkey((0, 0, 0))
        self.image = self.image_idle
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = PLAYER_SPEED
        #time.sleep(1)
        #self.y_speed = -1 * PLAYER_SPEED

        # if not jumping:

        # else:
        # if jump_count_1 >= -10:
        # bound = 1
        # if jump_count_1 < 0:
        # bound = -1
        # player_1 = (jump_count_1 ** 2) * (1 / 2) * bound
        # jump_count_1 -= 1

        # else:
        # jumping_1 = False
        # jump_count_1 = 10

        # if event.key == pygame.K_s:
        # player_1.move_down()


    def move_down(self):
        self.y_speed = -1 * PLAYER_SPEED
        self.image = self.image_idle

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        self.image = self.image_reverse

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.image_forward

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0
        self.image = self.image_idle

    def update(self):
        self.x += self.x_speed
        self.y -= self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

        if self.x >= (SCREEN_WIDTH - TILE_SIZE):
            self.x_speed = 0
        if self.x <= 0:
            self.x_speed = 0

        if self.y >= (SCREEN_HEIGHT - TILE_SIZE):
            self.y_speed = 0
        if self.y <= 0:
            self.y_speed = 0

    def draw(self, land):
        land.blit(self.image, self.rect)