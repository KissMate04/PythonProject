import pygame

pygame.init()

screen = pygame.display.set_mode((750, 900), pygame.SCALED)
shipsize = 32
startership_img = pygame.image.load('sprites\startership.png').convert_alpha()
startership_img = pygame.transform.scale(startership_img, (shipsize, shipsize))
running = True
x,y=0,0
clock = pygame.time.Clock()
delta_time = 0.8
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1 and shipsize < 176:
                shipsize += 16
            if event.y == -1 and shipsize > 32:
                shipsize -= 16
            startership_img = pygame.transform.scale(startership_img, (shipsize, shipsize))
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 4 * delta_time
    if keys[pygame.K_RIGHT]:
        x += 4 * delta_time
    if keys[pygame.K_UP]:
        y -= 4 * delta_time
    if keys[pygame.K_DOWN]:
        y += 4 * delta_time

    screen.blit(startership_img, (x, y))
    #hitbox = pygame.Rect(x,y,startership_img.get_width(), startership_img.get_height())
    #target = pygame.Rect(x, 100, 32, 32)
    #pygame.draw.rect(screen, (255,255,0),target)
    #collision = hitbox.colliderect(target)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()