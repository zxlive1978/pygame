# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # pygame.draw.rect(screen, (255,0,0), 10, 2, 10)

    # Flip the display
    # pygame.display.flip()

    pygame.display.update()
    clock.tick(FPS)


# Done! Time to quit.
pygame.quit()
pygame.display