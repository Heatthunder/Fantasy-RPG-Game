import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,300))

clock = pygame.time.Clock()

bob_stats = {"health":100, "damage":1}

player_pos = [250, 150]
enemyA_pos = [170, 70]
map_cords = [0, 0]

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
            player_pos[1] -= 5 
        if keys[pygame.K_s]:
            player_pos[1] += 5 
        if keys[pygame.K_a]:
            player_pos[0] -= 5 
        if keys[pygame.K_d]:
            player_pos[0] += 5 
        if keys[pygame.K_SPACE]:
            bob_stats["health"] -= 10
            print(bob_stats)
        if bob_stats["health"] == 0:
            pygame.quit()
            raise SystemExit

       # Fill the display with a solid color

    # Render the graphics here.
    # ...

    map = pygame.image.load("assets\grasslands-concept-pixilart.png")
    mapB = pygame.transform.scale(map, (500, 300))
    # rectB = 
    screen.blit(mapB, map_cords)    

    bob = pygame.image.load("assets\sr5z75c92c220faws3.png")
    # bob.set_colorkey ((0,0,0))
    Bob = pygame.transform.scale(bob, (70, 60))
    bob_box = pygame.Rect(player_pos[0],player_pos[1], 70, 60)
    rectA = (30,60,70,90)
    screen.blit(Bob, bob_box)

    weapon2 = pygame.image.load("assets\sr5zb291859ba3aws3.png")
    weapon2B = bob_box.move(50,30)
    screen.blit(weapon2, weapon2B)

    sally = pygame.image.load("assets\sr5z6cb376ca53aws3.png")
    sally_box = sally.get_rect()
    sally_box.move_ip(100, 90)
    screen.blit(sally, sally_box)
    
    if bob_box.colliderect(sally_box):
        pygame.quit()
        raise SystemExit
    
    enemyA = pygame.image.load("assets\sr5z70b2dbb43caws3.png")
    enemyA_box = pygame.Rect(enemyA_pos, (70, 60))
    EnemyA = pygame.transform.scale(enemyA, (70, 60))
    screen.blit(EnemyA, enemyA_box)

    enemyA_D = [player_pos[0] - enemyA_pos[0], player_pos[1]- enemyA_pos[1]] # enemy direction logic, etc
    # enemyA_D = [0,0] #enemyA_D unneeded?
    # if player_pos[0] < enemyA_pos[0]:
    #     enemyA_D[0] = -1
    # elif player_pos[0] > enemyA_pos[0]:
    #     enemyA_D[0] = 1
    # elif player_pos[0] == enemyA_pos[0]:
    #     enemyA_D[0] = 0
    # if player_pos[1] > enemyA_pos[1]:
    #     enemyA_D[1] = -1
    # elif player_pos[1] > enemyA_pos[1]:
    #     enemyA_D[1] = 1
    # elif player_pos[1] == enemyA_pos[1]:
    #     enemyA_D[1] = 0
    
    if enemyA_D[1] > 0:
        enemyA_pos[1] += 1
    if enemyA_D[1] < 0:
        enemyA_pos[1] -= 1
    if enemyA_pos[0] > 0:
        enemyA_pos[0] += 1
    if enemyA_D[0] < 0:
        enemyA_pos[0] -= 1

    weapon1 = pygame.image.load("assets\sr5z9a455fd099aws3.png")
    weapon1B = enemyA_box.move(50, 30)
    screen.blit(weapon1, weapon1B)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)

    # print(clock.tick)