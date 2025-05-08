import pygame
import projectile
import player
import enemy
import game

pygame.init()

screen = pygame.display.set_mode((600, 800), pygame.SCALED)
player = player.Player(screen, 'sprites\\startership.png', 100, 60, 4, screen.get_width() / 2 - 16, screen.get_height() - screen.get_height() / 4, 0)
running = True

ENEMY_SHOOT = pygame.USEREVENT
pygame.time.set_timer(ENEMY_SHOOT, 1000)



clock = pygame.time.Clock()
delta_time = 0.8



def level1():

    if not game.enemies:
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, screen.get_width() / 2, 100))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, screen.get_width() / 2, 300))
    if player.score == 20:
        game.enemies.clear()
        game.projectiles.clear()
        game.level = "level2"

def level2():
    if not enemy.enemies:
        enemy.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, screen.get_width() - 50, 100))
        enemy.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, screen.get_width() - 50, 300))
        enemy.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, screen.get_width() / 2, 300))
        enemy.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, 50, 300))
        enemy.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, 50, 100))
        enemy.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', 100, 20, 4, screen.get_width() / 2, 100))
    if player.score == 100:
        print("You win!")
        game.game_over()


while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            player.resize(event.y)
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            game.projectiles.append(
                projectile.Projectile(player.x + player.shipsize / 2, player.y, player.shipsize / 2, player.speed, player.damage, "player"))
        if event.type == ENEMY_SHOOT:
            for en in enemy.enemies:
                game.projectiles.append(
                    projectile.Projectile(en.x + en.shipsize / 2, en.y + en.shipsize, en.shipsize / 2, en.speed, en.damage, en))
                #if len(projectiles) > 10:
                 #   projectiles.pop(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        player.move(keys, delta_time)

    for proj in game.projectiles[:]:
        proj.move()
        proj.draw(screen)

        if proj.shooter == "player":
            for en in enemy.enemies[:]:
                if proj.hitbox.colliderect(en.hitbox):
                    print("Player projectile hit an enemy with: ", proj.damage, " damage!")
                    player.score += 5
                    en.hit(proj.damage)
                    if proj in game.projectiles:
                        game.projectiles.remove(proj)
                    break

        else:
            if proj.hitbox.colliderect(player.hitbox):
                print("Enemy projectile hit the player with: ", proj.damage, " damage!")
                player.hit(proj.damage)
                proj.shooter.promotion()
                if proj in game.projectiles:
                    game.projectiles.remove(proj)

        # Remove projectile if it goes off-screen
        if proj in game.projectiles and (proj.y < 0 or proj.y > screen.get_height()):
            game.projectiles.remove(proj)

    screen.blit(player.image, (player.x, player.y))

    for en in enemy.enemies[:]:
        en.move(keys, delta_time)
        screen.blit(en.image, (en.x, en.y))

    if game.level == "level1":
        level1()
    if game.level == "level2":
        level2()
    while game.level == "over":
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game.level = ""

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

