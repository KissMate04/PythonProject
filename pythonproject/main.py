import pygame
import projectile
import player
import enemy
import game

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 800), pygame.SCALED)
player = player.Player(screen, 'sprites\\startership.png', game.PLAYER_MAX_HEALTH, game.PLAYER_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() / 2 - 16, screen.get_height() - screen.get_height() / 4, 0)
running = True


font = pygame.font.SysFont('Futura', 20)
game_over_font = pygame.font.SysFont('Rocket', 50)
pygame.time.set_timer(ENEMY_SHOOT, 1000)

clock = pygame.time.Clock()
delta_time = 0.8

def info(max_health, health, level, score):
    health_text = font.render(f"Health: {str(health)}/{str(max_health)}", True, (255, 255, 255))
    score_text = font.render(f"Score: {str(score)}", True, (255, 255, 255))
    level_text = ""
    if level == "level1":
        level_text = font.render("Level 1", True, (255, 255, 255))
    elif level == "level2":
        level_text = font.render("Level 2", True, (255, 255, 255))
    screen.blit(health_text, (10, 10))
    screen.blit(score_text, (screen.get_width()-10-score_text.get_width(), 10))
    if level_text != "":
        screen.blit(level_text, (screen.get_width()/2 - level_text.get_width()/2, 10))


def level1():
    if not game.enemies:
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() / 2, 100))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() / 2, 300))
    if game.score >= 100:
        game.enemies.clear()
        game.projectiles.clear()
        game.level = "level2"

def level2():
    if not game.enemies:
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() - 50, 100))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() - 50, 300))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() / 2, 300))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, 50, 300))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, 50, 100))
        game.enemies.append(enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE, game.PLAYER_SPEED, screen.get_width() / 2, 100))
    if game.score >= 500:
        print("You win!")
        game.game_over()


while running:
    screen.fill((0,0,0))
    info(player.max_health, player.health, game.level, game.score)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            player.resize(event.y)
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            game.projectiles.append(
                projectile.Projectile(player.x + player.shipsize / 2, player.y, player.shipsize / 2, game.PROJECTILE_SPEED, player.damage, "player"))
        if event.type == game.ENEMY_SHOOT:
            for en in game.enemies:
                game.projectiles.append(
                    projectile.Projectile(en.x + en.shipsize / 2, en.y + en.shipsize, en.shipsize / 2, game.PROJECTILE_SPEED, en.damage, en))
                #if len(projectiles) > 10:
                 #   projectiles.pop(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        player.move(keys, delta_time)

    for proj in game.projectiles[:]:
        proj.move()
        proj.draw(screen)

        if proj.shooter == "player":
            for en in game.enemies[:]:
                if proj.hitbox.colliderect(en.hitbox):
                    print("Player projectile hit an enemy with: ", proj.damage, " damage!")
                    game.score += 5
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

    for en in game.enemies[:]:
        en.move(keys, delta_time)
        screen.blit(en.image, (en.x, en.y))

    if game.level == "level1":
        level1()
    if game.level == "level2":
        level2()
    while game.level == "over":
        print("i get here")
        #screen.fill((0, 0, 0))
        game_over_text = game_over_font.render(f"Game Over.\nScore: {game.score}", True, (255, 10, 10))
        screen.blit(game_over_text, (screen.get_width()/2 - game_over_text.get_width()/2, screen.get_height()/2 - game_over_text.get_height()/2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game.level = ""

    pygame.display.flip()
    clock.tick(60)


pygame.quit()

