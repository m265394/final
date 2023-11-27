import pygame
import sys
import random
import time

# import all necessary files
from background import draw_background
from game_parameters import *
from player_1 import Player1
from player_2 import Player2


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

# create players
player_1 = Player1(2*TILE_SIZE, SCREEN_HEIGHT - 3*TILE_SIZE) # initializing player 1 on the left
player_2 = Player2(SCREEN_WIDTH - 2*TILE_SIZE, SCREEN_HEIGHT - 3*TILE_SIZE) # initializing player 2 on the right


# load new font to keep score
score = 0
score_font = pygame.font.Font("assets/fonts/Hexagonal.ttf", 36)

# load a sound

# load alternate hearts
player_1_life_icon = pygame.image.load("assets/sprites/player_1_heart.png").convert()
new_player_1_life_icon = pygame.transform.scale(player_1_life_icon, (TILE_SIZE, TILE_SIZE) )
new_player_1_life_icon.set_colorkey( (0, 0, 0) )

player_2_life_icon = pygame.image.load("assets/sprites/player_2_heart.png").convert()
new_player_2_life_icon = pygame.transform.scale(player_2_life_icon, (TILE_SIZE, TILE_SIZE) )
new_player_2_life_icon.set_colorkey( (0, 0, 0) )

# set number of lives
lives_1 = NUM_LIVES
lives_2 = NUM_LIVES

jumping_1 = False
jump_count_1 = 10
jumping_2 = False
jump_count_2 = 10


while (lives_1 > 0 and running) or (lives_2 > 0 and running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # pygame.quit here would shut down the game

        # control player 1
        if event.type == pygame.KEYDOWN:
            if not jumping_1:
                if event.key == pygame.K_w:
                    jumping_1 = True
                    player_1.move_up()
            else:
                if jump_count_1 >= -10:
                    bound = 1
                    if jump_count_1 < 0:
                        bound = -1
                    player_1 = (jump_count_1 ** 2) * (1 / 2) * bound
                    jump_count_1 -= 1

                else:
                    jumping_1 = False
                    jump_count_1 = 10

            #if event.key == pygame.K_s:
                #player_1.move_down()

            if event.key == pygame.K_a:
                player_1.move_left()
            if event.key == pygame.K_d:
                player_1.move_right()

        if event.type == pygame.KEYUP:
            player_1.stop()


        # control player 2
        if event.type == pygame.KEYDOWN:
            if not jumping_2:
                if event.key == pygame.K_UP:
                    jumping_2 = True
                    player_2.move_up()
            else:
                if jump_count_2 >= -10:
                    bound = 1
                    if jump_count_2 < 0:
                        bound = -1
                    player_2 = (jump_count_2 ** 2) * (1 / 2) * bound
                    jump_count_2 -= 1

                else:
                    jumping_2 = False
                    jump_count_2 = 10

            # if event.key == pygame.K_DOWN:
            # player_2.move_down()

            if event.key == pygame.K_LEFT:
                player_2.move_left()
            if event.key == pygame.K_RIGHT:
                player_2.move_right()

        if event.type == pygame.KEYUP:
            player_2.stop()

    # draw the background
    screen.blit(background, (0, 0))

    # draw objects
    #objects.update()

    # update players
    player_1.update()
    player_2.update()



    # update score on screen
    text_1 = score_font.render(f"{score}", True, (255, 146, 0))
    screen.blit(text_1, (text_1.get_width() - 15, 0) )

    text_2 = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text_2, (SCREEN_WIDTH - text_2.get_width() - 15, 0) )

    #screen.blit(player_1.image_idle, (SCREEN_WIDTH/2, 0))
    screen.blit(background, (0, 0))
    player_1.draw(screen)
    player_2.draw(screen)

    # draw lives
    for i in range(lives_1):
        screen.blit(new_player_1_life_icon, (i*TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    for j in range(lives_2):
        screen.blit(new_player_2_life_icon, ( (SCREEN_WIDTH-TILE_SIZE) - j * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

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
