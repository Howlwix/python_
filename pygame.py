import pygame
pygame.init()
screen = pygame.display.set_mode((900,700))
player = pygame.rect(600,450,70,70)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 10
    if keys[pygame.K_d]:
        player.x += 10
    if keys[pygame.K_w]:
        player.y -= 10
    if keys[pygame.K_s]:
        player.y += 10
    player.x = max(0, min(player.x, 900 - player.width))
    player.y = max(0, min(player.y, 700 - player.height))
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,224),player)
    pygame.display.update()
pygame.quit()
