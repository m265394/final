import pygame
import sys
import random
import time

# import all necessary files
from background import draw_background, add_fruit, add_star, add_heart, add_bomb
from game_parameters import *
from player_1 import Player1
from player_2 import Player2
from fruit import fruits_left, fruits_right
from star import stars_left, stars_right
from heart import hearts_left, hearts_right
from bomb import bombs_left, bombs_right

#initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Under Fire")

# clock object
clock = pygame.time.Clock()



# Main Loop
running = True

# copy background
background = screen.copy()
draw_background(background)

# create players
player_1 = Player1(SCREEN_WIDTH/2 - TILE_SIZE, SCREEN_HEIGHT - 3*TILE_SIZE) # initializing player 1 on the left
player_2 = Player2(SCREEN_WIDTH/2, SCREEN_HEIGHT - 3*TILE_SIZE) # initializing player 2 on the right

# draw fruits
add_fruit(2)

# draw stars
add_star(1)

# draw hearts
add_heart(1)

# draw bombs
add_bomb(1)


# load new font to keep score
score_1 = 0
score_2 = 0
score_font_1 = pygame.font.Font("assets/fonts/Hexagonal.ttf", 36)
score_font_2 = pygame.font.Font("assets/fonts/sunshine.ttf", 36)
game_over_font = pygame.font.Font("assets/fonts/RedUndeadExpanded.ttf", 42)

# load sounds
#music = pygame.mixer.Sound("assets/sounds/chomp.wav")

fatality = pygame.mixer.Sound("assets/sounds/fatality.mp3")

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
velocity_2 = 5
mass_2 = 1


while (lives_1 > 0 and running) or (lives_2 > 0 and running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # pygame.quit here would shut down the game

        # control player 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1.jumping = True


            if event.key == pygame.K_a:
                player_1.move_left()
            if event.key == pygame.K_d:
                player_1.move_right()

        if event.type == pygame.KEYUP:
            player_1.stop()


        # control player 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_2.jumping = True
            if event.key == pygame.K_LEFT:
                player_2.move_left()
            if event.key == pygame.K_RIGHT:
                player_2.move_right()

        if event.type == pygame.KEYUP:
            player_2.stop()


    # draw the background
    screen.blit(background, (0, 0))

    # draw objects
    fruits_left.update()
    fruits_right.update()
    stars_left.update()
    stars_right.update()
    hearts_left.update()
    hearts_right.update()
    bombs_left.update()
    bombs_right.update()

    # update players
    player_1.jump()
    player_2.jump()
    player_1.update()
    player_2.update()

    # check for collisions between player_1 and items
    points_1 = pygame.sprite.spritecollide(player_1, fruits_left or fruits_right, True)
    if points_1:
        #pygame.mixer.Sound.play(chomp)
        score_1 += len(points_1)
        add_fruit(len(points_1))


    super_1 = pygame.sprite.spritecollide(player_1, stars_left or stars_right, True)
    if super_1:
        #pygame.mixer.Sound.play(chomp)
        score_1 = score_1 + 5*len(super_1)
        add_star(len(super_1)/10)

    # check if player collides with bombs
    result_1 = pygame.sprite.spritecollide(player_1, bombs_left or bombs_right, True)
    if result_1:
        #pygame.mixer.Sound.play(bubbles)
        lives_1 -= len(result_1)
        add_bomb(len(result_1))

    # check for collisions between player_2 and items
    points_2 = pygame.sprite.spritecollide(player_2, fruits_left or fruits_right, True)
    if points_2:
        # pygame.mixer.Sound.play(chomp)
        score_2 += len(points_2)
        add_fruit(len(points_2))

    super_2 = pygame.sprite.spritecollide(player_2, stars_left or stars_right, True)
    if super_2:
        # pygame.mixer.Sound.play(chomp)
        score_2 = score_2 + 5 * len(super_2)
        add_star(len(super_2) / 10)

    # check if player collides with bombs
    result_2 = pygame.sprite.spritecollide(player_2, bombs_left or bombs_right, True)
    if result_2:
        # pygame.mixer.Sound.play(bubbles)
        lives_1 -= len(result_2)
        add_bomb(len(result_2))

    # update score on screen
    text = score_font_1.render(f"SCORE: {score_1}", True, (255, 146, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 15, 0))

    text_2 = score_font_2.render(f"{score_2}", True, (255, 0, 0))
    screen.blit(text_2, (SCREEN_WIDTH - text_2.get_width() - 15, 0) )

    #screen.blit(player_1.image_idle, (SCREEN_WIDTH/2, 0))
    screen.blit(background, (0, 0))
    player_1.draw(screen)
    player_2.draw(screen)
    fruits_left.draw(screen)
    fruits_right.draw(screen)
    stars_left.draw(screen)
    stars_right.draw(screen)
    hearts_left.draw(screen)
    hearts_right.draw(screen)
    bombs_left.draw(screen)
    bombs_right.draw(screen)

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
#screen.blit(background, (0,0))
screen.fill((70,150,230))

# show game over message
message = game_over_font.render("GAME OVER", True, (0, 0, 0) )
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - 4*message.get_height()/2) )

#show final score
score_text_1 = score_font_1.render(f"SCORE: {score_1}", True, (255, 146, 0) )
screen.blit(score_text_1, (SCREEN_WIDTH/2 - 4*score_text_1.get_width()/2, SCREEN_HEIGHT/2 + score_text_1.get_height()/2))

score_text_2 = score_font_2.render(f"SCORE: {score_2}", True, (255, 0, 0) )
screen.blit(score_text_2, (SCREEN_WIDTH/2 + 2*score_text_2.get_width()/2, SCREEN_HEIGHT/2 + score_text_2.get_height()/2))

# update display
pygame.display.flip()

# play game over sound
time.sleep(1)
pygame.mixer.Sound.play(fatality)

# wait for user to exit the game
## This is where you would put a 'play again' function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()