
import pygame
from game_parameters import *

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_idle = pygame.image.load("../assets/sprites/player_2_idle.png").convert()
        self.image_idle.set_colorkey((0, 0, 0))
        self.image_forward = pygame.image.load("../assets/sprites/player_2_walk.png").convert()
        self.image_forward.set_colorkey((0, 0, 0))
        self.image_reverse = pygame.transform.flip(self.image_forward, True, False)
        self.image_reverse.set_colorkey((0, 0, 0))
        self.image_hurt_idle = pygame.image.load("../assets/sprites/player_2_zombie_idle.png").convert()
        self.image_hurt_idle.set_colorkey((0, 0, 0))
        self.image_hurt_forward = pygame.image.load("../assets/sprites/player_2_zombie_walk.png").convert()
        self.image_hurt_forward.set_colorkey((0, 0, 0))
        self.image_hurt_reverse = pygame.transform.flip(self.image_forward, True, False)
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

    def move_down(self):
        self.y_speed = -1 * PLAYER_SPEED

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