import pygame
import sys

pygame.init()

# Set up screen
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("FPS Monitor Example")

# Set up clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    # Limit to 60 FPS
    dt = clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the actual FPS
    fps = clock.get_fps()

    # Fill the screen
    screen.fill((0, 0, 0))

    # Render FPS to screen
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
