
import pygame
from game_parameters import *
from fruit import Fruit, fruits_left, fruits_right
from star import Star, stars_left, stars_right
from heart import Heart, hearts_left, hearts_right
from bomb import Bomb, bombs_left, bombs_right

def draw_background(land):
    # load our tiles from the assets folder
    floor = pygame.image.load("assets/sprites/floor.png").convert()
    floor_bottom = pygame.image.load("assets/sprites/floor_bottom.png").convert()
    sky = pygame.image.load("assets/sprites/background_sky.png").convert()
    clouds_1 = pygame.image.load("assets/sprites/background_clouds_1.png").convert()
    clouds_2 = pygame.image.load("assets/sprites/background_clouds_2.png").convert()
    trees_1 = pygame.image.load("assets/sprites/background_trees_1.png").convert()
    trees_2 = pygame.image.load("assets/sprites/background_trees_2.png").convert()
    tank_right= pygame.image.load("assets/sprites/tank_small.png").convert()

    # scale images
    new_sky = pygame.transform.scale(sky, (TILE_SIZE, TILE_SIZE) )
    new_clouds_1 = pygame.transform.scale(clouds_1, (TILE_SIZE, TILE_SIZE) )
    new_clouds_2 = pygame.transform.scale(clouds_2, (TILE_SIZE, TILE_SIZE) )
    new_tank_right = pygame.transform.scale(tank_right, (TILE_SIZE, TILE_SIZE) )

    # make PNGs transparent
    floor.set_colorkey((0, 0, 0))
    floor_bottom.set_colorkey((0, 0, 0))
    new_sky.set_colorkey((0, 0, 0))
    new_clouds_1.set_colorkey((0, 0, 0))
    new_clouds_2.set_colorkey((0, 0, 0))
    trees_1.set_colorkey((0, 0, 0))
    trees_2.set_colorkey((0, 0, 0))
    new_tank_right.set_colorkey((0, 0, 0))

    #flipped tanks
    new_tank_left = pygame.transform.flip(new_tank_right, True, False)
    new_tank_left.set_colorkey((0, 0, 0))

    # draw the sky
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            land.blit(new_sky, (x, y))
            land.blit(new_clouds_1, (x, 2*TILE_SIZE))
            land.blit(new_clouds_2, (x + 2*TILE_SIZE, 2*TILE_SIZE))

    # draw the floor
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        land.blit(floor, (x, SCREEN_HEIGHT - 2*TILE_SIZE))
        land.blit(floor_bottom, (x, SCREEN_HEIGHT - TILE_SIZE))



    # draw the tanks
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            land.blit(new_tank_right, (0, SCREEN_HEIGHT - (3* y + 3*TILE_SIZE) )) # 3 in front of 'y' indicates how many tanks on screen >3 = more tanks
            land.blit(new_tank_left, (SCREEN_WIDTH - TILE_SIZE, SCREEN_HEIGHT - (3*y + 3*TILE_SIZE)) )


def add_fruit_left(num_fruit):
    # remove current list
    fruits_left.empty()
    #add fruits from tanks
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_fruit):
            fruits_left.add(Fruit(TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'right'))


def add_fruit_right(num_fruit):
    fruits_right.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_fruit):
            fruits_right.add(Fruit(SCREEN_WIDTH - TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'left'))

def add_star_left(num_star):
    stars_left.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_star):
            stars_left.add(Star(TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'right'))


def add_star_right(num_star):
    stars_right.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_star):
            stars_right.add(Star(SCREEN_WIDTH - TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'left'))


def add_heart_left(num_heart):
    hearts_left.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_heart):
            hearts_left.add(Heart(TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'right'))


def add_heart_right(num_heart):
    hearts_right.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_heart):
            hearts_right.add(Heart(SCREEN_WIDTH - TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'left'))

def add_bomb_left(num_bomb):
    bombs_left.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_bomb):
            bombs_left.add(Bomb(TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'right'))


def add_bomb_right(num_bomb):
    bombs_right.empty()
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        for _ in range(num_bomb):
            bombs_right.add(Bomb(SCREEN_WIDTH - TILE_SIZE, SCREEN_HEIGHT - (3 * y + 3 * TILE_SIZE), direction = 'left'))