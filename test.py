import pygame
import sys

pygame.init()

# Set up screen
screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FPS test")

# Set up clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Rectangle setup
BLUE = (0, 0, 255)
rect = pygame.Rect(50, 50, 100, 50)
velocity = pygame.Vector2(5, 3)

# Frame toggle for skipping
draw_this_frame = True

running = True
while running:
    dt = clock.tick(61)  # 60 FPS cap

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic
    rect.x += velocity.x
    rect.y += velocity.y

    if rect.left < 0 or rect.right > screen_width:
        velocity.x *= -1
    if rect.top < 0 or rect.bottom > screen_height:
        velocity.y *= -1

    # Toggle whether to draw this frame
    draw_this_frame = not draw_this_frame
    if not draw_this_frame:
        continue  # Skip rendering this frame

    # Render
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, BLUE, rect)

    # FPS display
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
