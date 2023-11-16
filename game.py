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


pygame.quit()
sys.quit()