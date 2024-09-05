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

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

# Define constants for the screen width and height
SCREEN_WIDTH = screen_width-10
SCREEN_HEIGHT = screen_height-50



# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
# На весь экран
#pygame.FULLSCREEN вместо pygame.RESIZABLE

FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()





# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # pygame.draw.rect(screen, (255,0,0), 10, 2, 10)

    # This line says "Draw surf onto the screen at the center"
    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    
    # Flip the display
    # pygame.display.flip()

    pygame.display.update()
clock.tick(FPS)


# Done! Time to quit.
pygame.quit()
pygame.display