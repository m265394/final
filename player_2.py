
import pygame
from game_parameters import *

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image_idle = pygame.image.load("assets/sprites/player_2_idle.png").convert()
        self.image_idle = pygame.transform.scale(self.image_idle, (TILE_SIZE, TILE_SIZE))
        self.image_idle.set_colorkey((0, 0, 0))
        self.image_forward = pygame.image.load("assets/sprites/player_2_walk.png").convert()
        self.image_forward = pygame.transform.scale(self.image_forward, (TILE_SIZE, TILE_SIZE))
        self.image_forward.set_colorkey((0, 0, 0))
        self.image_reverse = pygame.transform.flip(self.image_forward, True, False)
        self.image_reverse = pygame.transform.scale(self.image_reverse, (TILE_SIZE, TILE_SIZE))
        self.image_reverse.set_colorkey((0, 0, 0))
        self.image_hurt_idle = pygame.image.load("assets/sprites/player_2_zombie_idle.png").convert()
        self.image_hurt_idle = pygame.transform.scale(self.image_hurt_idle, (TILE_SIZE, TILE_SIZE))
        self.image_hurt_idle.set_colorkey((0, 0, 0))
        self.image_hurt_forward = pygame.image.load("assets/sprites/player_2_zombie_walk.png").convert()
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
        self.jumping = False
        self.velocity = 5
        self.mass = 1


    def grounded(self):
        if not self.jumping:
           self.jumping = True

    def jump(self):
        if self.jumping:
            force = (1 / 2) * self.mass * (self.velocity ** 2)
            self.y -= force
            self.velocity -= 1

            if self.velocity < 0:
                self.mass = -1

            if self.velocity == -6:
                self.jumping = False
                self.velocity = 5
                self.mass = 1

    def fall(self):
        if not self.jumping and self.y != (SCREEN_HEIGHT - 3*TILE_SIZE):
            self.y = min(self.y + 2, (SCREEN_HEIGHT - 3*TILE_SIZE) )

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