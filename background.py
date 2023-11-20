
import pygame
from game_parameters import *
import random

def draw_background(land):
    # load our tiles from the assets folder
    floor = pygame.image.load("assets/sprites/floor.png").convert()
    floor_bottom = pygame.image.load("assets/sprites/floor_bottom.png").convert()
    sky = pygame.image.load("assets/sprites/background_sky.png").convert()
    clouds_1 = pygame.image.load("assets/sprites/background_clouds_1.png").convert()
    clouds_2 = pygame.image.load("assets/sprites/background_clouds_2.png").convert()
    trees_1 = pygame.image.load("assets/sprites/background_trees_1.png").convert()
    trees_2 = pygame.image.load("assets/sprites/background_trees_2.png").convert()



    # make PNGs transparent
    floor.set_colorkey((0, 0, 0))
    floor_bottom.set_colorkey((0, 0, 0))
    sky.set_colorkey((0, 0, 0))
    clouds_1.set_colorkey((0, 0, 0))
    clouds_2.set_colorkey((0, 0, 0))
    trees_1.set_colorkey((0, 0, 0))
    trees_2.set_colorkey((0, 0, 0))

    # draw the sky
    for x in range(0, SCREEN_WIDTH, SKY_TILE):
        for y in range(0, SCREEN_HEIGHT, SKY_TILE):
            land.blit(sky, (x, y))
            land.blit(clouds_1, (x, 2*SKY_TILE))
            land.blit(clouds_2, (x + SKY_TILE, 2*SKY_TILE))

    # draw the floor
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        land.blit(floor, (x, SCREEN_HEIGHT - 2*TILE_SIZE))
        land.blit(floor_bottom, (x, SCREEN_HEIGHT - TILE_SIZE))
