import pygame
import sys
import random
import time

# import all necessary files
from background import draw_background
from game_parameters import *


#initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Under Fire")

# clock object
clock = pygame.time.Clock()


# Main Loop
running = True
background = screen.copy()
draw_background(background)


# load new font to keep score
score = 0
score_font = pygame.font.Font("assets/fonts/pink_and_blue.otf", 36)

# load a sound

# load alternate fish and game over
life_icon = pygame.image.load("assets/sprites/player_1_heart.png").convert()
life_icon.set_colorkey( (0, 0, 0) )

# set number of lives
lives = NUM_LIVES

while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # pygame.quit here would shut down the game


    # draw the background
    screen.blit(background, (0, 0))


    # update score on screen
    text = score_font.render(f"{score}", True, (0, 29, 255))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 15, 0) )

    # draw lives
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    # update the display
    pygame.display.flip()


    # set the frame rate to 60 FPS
    clock.tick(60)

# create new game over background
screen.blit(background, (0,0))

# update display
pygame.display.flip()

# play game over sound

# wait for user to exit the game
## This is where you would put a 'play again' function
while True:
    for event in pygame.event.get():
        #quit pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
