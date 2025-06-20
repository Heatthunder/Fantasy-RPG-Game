import pygame
import sys

pygame.init()

# Set up display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()   # Update the display

pygame.quit()
sys.exit()
