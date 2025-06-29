import pygame

pygame.init()

screen = pygame.display.set_mode((500,300))

clock = pygame.time.Clock()

bob_stats = {"health":100}

player_pos = [250, 150]

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos[0] -= 10 
        if keys[pygame.K_s]:
            player_pos[0] += 10 
        if keys[pygame.K_a]:
            player_pos[1] -= 10 
        if keys[pygame.K_d]:
            player_pos[1] += 10 
        if keys[pygame.K_SPACE]:
            bob_stats["health"] -= 20

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    bob = pygame.image.load("assets\sr5z75c92c220faws3.png")
    bobR = bob.get_rect()
    bob_pos = (player_pos[1],player_pos[0], player_pos[1]+ 32, player_pos[0]+ 33)
    rectA = (30,60,70,90)
    screen.blit(bob, bob_pos)

    # pygame.Surface.set_colorkey (0,0,0) 

    # sally = pygame.image.load("assets\sr5z6cb376ca53aws3.png")
    # sallyR = sally.get_rect()
    # screen.blit(sally, sallyR)
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)