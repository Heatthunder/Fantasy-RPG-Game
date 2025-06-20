import pygame
import sys
import time

pygame.init()

# Screen setup
screen = pygame.display.set_mode((900, 700), pygame.DOUBLEBUF)
pygame.display.set_caption("Vsync-ish FPS test")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Colors
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Rectangle setup
rect = pygame.Rect(50, 50, 200, 150)
velocity = pygame.Vector2(4, 2.7)

# Target frame time
target_fps = 60
frame_duration = 1.0 / target_fps

running = True
while running:
    frame_start = time.perf_counter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    rect.x += velocity.x
    rect.y += velocity.y
    if rect.left < 0 or rect.right > 900:
        velocity.x *= -1
    if rect.top < 0 or rect.bottom > 700:
        velocity.y *= -1

    # Render
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, rect)
    # Cyan square inside
    inner_size = min(rect.width, rect.height) // 3
    inner_pos = (rect.centerx - inner_size // 2, rect.centery - inner_size // 2)
    pygame.draw.rect(screen, CYAN, (*inner_pos, inner_size, inner_size))

    # FPS
    fps = clock.get_fps()
    fps_text = font.render(f"{fps:.2f} FPS", True, WHITE)
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick()  # Only used to keep get_fps() accurate

    # Precise frame pacing (hybrid strategy)
    frame_end = time.perf_counter()
    elapsed = frame_end - frame_start
    remaining = frame_duration - elapsed

    if remaining > 0.002:
        time.sleep(remaining - 0.001)  # Let the OS sleep most of the way

    while time.perf_counter() - frame_start < frame_duration:
        pass  # Fine-tuned busy-wait

pygame.quit()
sys.exit()
