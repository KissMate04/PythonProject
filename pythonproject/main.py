import pygame
import player
import enemy
import game

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((600, 800), pygame.SCALED)
    menu_font = pygame.font.SysFont('Futura', 100)
    p = player.Player(screen, 'sprites\\startership.png', game.PLAYER_MAX_HEALTH, game.PLAYER_BASE_DAMAGE,
                      game.PLAYER_SPEED, screen.get_width() / 2 - 16,
                      screen.get_height() - screen.get_height() / 4, 0)

    def reset():
        nonlocal p
        p = player.Player(screen, 'sprites\\startership.png', game.PLAYER_MAX_HEALTH, game.PLAYER_BASE_DAMAGE,
                          game.PLAYER_SPEED, screen.get_width() / 2 - 16,
                          screen.get_height() - screen.get_height() / 4, 0)
        game.level = "level1"
        game.score = 0

    def menu():
        start_cont_btn = pygame.draw.rect(screen, (0,0,0), (screen.get_width()/2 - 100, screen.get_height()/3 - 50, 200, 100))
        if game.score == 0:
            start_cont_text = menu_font.render("Start", True, (255, 255, 255))
        else:
            start_cont_text = menu_font.render("Continue", True, (255, 255, 255))
        screen.blit(start_cont_text, (screen.get_width()/2 - start_cont_text.get_width()/2, screen.get_height()/3 - start_cont_text.get_height()/2))

        quit_btn = pygame.draw.rect(screen, (0, 0, 0),(screen.get_width() / 2 - 100, screen.get_height() - screen.get_height() / 3 - 50, 200, 100))
        quit_text = menu_font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_text,(screen.get_width() / 2 - quit_text.get_width() / 2, screen.get_height() - screen.get_height() / 3 - start_cont_text.get_height() / 2))

        #Gombnyomás: https://www.youtube.com/watch?v=Y52JsDs4cMQ
        if start_cont_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            game.in_menu = False

        if quit_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            exit()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()



    def info(max_health, health, level, score):
        health_text = font.render(f"Health: {str(health)}/{str(max_health)}", True, (255, 255, 255))
        score_text = font.render(f"Score: {str(score)}", True, (255, 255, 255))
        level_text = ""
        if level == "level1":
            level_text = font.render("Level 1", True, (255, 255, 255))
        elif level == "level2":
            level_text = font.render("Level 2", True, (255, 255, 255))
        screen.blit(health_text, (10, 10))
        screen.blit(score_text, (screen.get_width() - 10 - score_text.get_width(), 10))
        if level_text != "":
            screen.blit(level_text, (screen.get_width() / 2 - level_text.get_width() / 2, 10))

    def level1():
        if not game.enemies:
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, screen.get_width() / 2, 100))
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, screen.get_width() / 2, 300))
        if game.score >= 100:
            game.enemies.clear()
            game.projectiles.clear()
            game.level = "level2"

    def level2():
        if not game.enemies:
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, screen.get_width() - 50, 100))
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, screen.get_width() - 50, 300))
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, screen.get_width() / 2, 300))
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, 50, 300))
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, 50, 100))
            game.enemies.append(
                enemy.Enemy(screen, 'sprites\\enemyship1.png', game.ENEMY_MAX_HEALTH, game.ENEMY_BASE_DAMAGE,
                            game.PLAYER_SPEED, screen.get_width() / 2, 100))
        if game.score >= 500:
            print("You win!")
            game.game_over()

    def play():
        info(p.max_health, p.health, game.level, game.score)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                p.resize(event.y)
            if event.type == pygame.QUIT:
                game.running = False
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                p.shoot()
            if event.type == game.ENEMY_SHOOT:
                for en in game.enemies:
                    en.shoot()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[
            pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            p.move(keys, delta_time)
        if keys[pygame.K_ESCAPE]:
            game.in_menu = True

        for proj in game.projectiles[:]:
            proj.move()
            proj.draw(screen)

            if proj.shooter == "player":
                for en in game.enemies[:]:
                    if proj.hitbox.colliderect(en.hitbox):
                        if not en.dying:
                            print("Player projectile hit an enemy with: ", proj.damage, " damage!")
                            game.score += 5
                            en.hit(proj.damage)
                        if proj in game.projectiles:
                            game.projectiles.remove(proj)
                        break

            else:
                if proj.hitbox.colliderect(p.hitbox):
                    print("Enemy projectile hit the player with: ", proj.damage, " damage!")
                    p.hit(proj.damage)
                    proj.shooter.promotion()
                    if proj in game.projectiles:
                        game.projectiles.remove(proj)

            # Remove projectile if it goes off-screen
            if proj in game.projectiles and (proj.y < 0 or proj.y > screen.get_height()):
                game.projectiles.remove(proj)

        screen.blit(p.image, (p.x, p.y))

        for en in game.enemies[:]:
            en.move(keys, delta_time)
            screen.blit(en.image, (en.x, en.y))

        if game.level == "level1":
            level1()
        if game.level == "level2":
            level2()
        if game.level == "over":
            game_over_text = game_over_font.render(f"Game Over", True, (255, 10, 10))
            screen.blit(game_over_text, (screen.get_width() / 2 - game_over_text.get_width() / 2,
                                         screen.get_height() / 2 - game_over_text.get_height() / 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            game.in_menu = True
            reset()
        if game.in_menu:
            menu()


    font = pygame.font.SysFont('Futura', 20)
    game_over_font = pygame.font.SysFont('Rocket', 50)

    clock = pygame.time.Clock()
    delta_time = 0.8



    while game.running:
        screen.fill((0, 0, 0))
        if game.in_menu:
            menu()
        else:
            play()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()



if __name__ == "__main__":
    main()