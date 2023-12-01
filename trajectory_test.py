import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Starting position and initial velocity
pos = [50, HEIGHT - 500]
velocity = [5, -1]  # x velocity, y velocity
acceleration = [0, .5]  # x acceleration, y acceleration

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position based on velocity and acceleration
    pos[0] += velocity[0]
    pos[1] += velocity[1]
    velocity[0] += acceleration[0]
    velocity[1] += acceleration[1]

    # Draw the object (a simple square in this case)
    pygame.draw.rect(screen, BLUE, (pos[0], pos[1], 20, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()