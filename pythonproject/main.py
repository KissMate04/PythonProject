# pylint: disable=import-error, no-member
"""
Contains the game loop, levels and the menu.
"""
import sys
import pygame
import player
import enemy
import game
import boss

def main():
    """
    Initializes the game, creates player and starts the game loop.
    """
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((600, 800), pygame.SCALED)
    menu_font = pygame.font.SysFont('Futura', 100)
    p = player.Player(
        screen,
        'startership.png',
        game.PLAYER_MAX_HEALTH,
        game.PLAYER_BASE_DAMAGE,
        game.PLAYER_SPEED,
        screen.get_width() /
        2 -
        16,
        screen.get_height() -
        screen.get_height() /
        4)

    def reset():
        """"
        Resets the score, level and player
        """
        nonlocal p
        p = player.Player(
            screen,
            'startership.png',
            game.PLAYER_MAX_HEALTH,
            game.PLAYER_BASE_DAMAGE,
            game.PLAYER_SPEED,
            screen.get_width() / 2 - 16,
            screen.get_height() - screen.get_height() / 4)
        game.level = "level1"
        game.score = 0

    def menu():
        """"
        Displays menu with start/continue and quit buttons
        The game is stopped while here
        """
        start_cont_btn = pygame.draw.rect(
            screen,
            (0, 0, 0),
            (screen.get_width() / 2 - 100, screen.get_height() / 3 - 50, 200, 100)
        )
        if game.score == 0:
            start_cont_text = menu_font.render("Start", True, (255, 255, 255))
        else:
            start_cont_text = menu_font.render(
                "Continue", True, (255, 255, 255))
        screen.blit(
            start_cont_text,
            (screen.get_width() / 2 - start_cont_text.get_width() / 2,
             screen.get_height() / 3 - start_cont_text.get_height() / 2)
        )

        quit_btn = pygame.draw.rect(
            screen,
            (0, 0, 0),
            (screen.get_width() / 2 - 100,
             screen.get_height() - screen.get_height() / 3 - 50, 200, 100)
        )
        quit_text = menu_font.render("Quit", True, (255, 255, 255))
        screen.blit(
            quit_text,
            (screen.get_width() /
             2 -
             quit_text.get_width() /
             2,
             screen.get_height() -
             screen.get_height() /
             3 -
             start_cont_text.get_height() /
             2))

        # Gombnyomás: https://www.youtube.com/watch?v=Y52JsDs4cMQ
        if start_cont_btn.collidepoint(
                pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            game.in_menu = False

        if quit_btn.collidepoint(
                pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def info(max_health, health, level, score):
        """
        displays health, current level and score on top of the screen

        :param max_health: player's max health
        :param health: player's current health
        :param level: current level
        :param score: current score
        """
        health_text = font.render(
            f"Health: {str(health)}/{str(max_health)}", True, (255, 255, 255))
        score_text = font.render(
            f"Score: {str(score)}", True, (255, 255, 255))
        level_text = ""
        if level == "level1":
            level_text = font.render("Level 1", True, (255, 255, 255))
        elif level == "level2":
            level_text = font.render("Level 2", True, (255, 255, 255))
        elif level == "level3":
            level_text = font.render("Level 3", True, (255, 255, 255))
        screen.blit(health_text, (10, 10))
        screen.blit(
            score_text,
            (screen.get_width() -
             10 -
             score_text.get_width(),
             10))
        if level_text != "":
            screen.blit(level_text, (screen.get_width() /
                        2 - level_text.get_width() / 2, 10))

    def level1():
        """
        Level 1 of the game
        Continuously creates 2 enemies untill target score is reached
        Deletes enemies and projectiles and sets level to 2 once target is reached
        """
        if not game.enemies:
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    screen.get_width() / 2,
                    100))
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    screen.get_width() / 2,
                    300))
        if game.score >= game.LEVEL1_TARGET_SCORE:
            game.enemies.clear()
            game.projectiles.clear()
            game.level = "level2"

    def level2():
        """
        Level 2 of the game
        Continuously creates 6 enemies untill target score is reached
        Deletes enemies and projectiles and sets level to 3 once target is reached
        """
        if not game.enemies:
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    screen.get_width() - 50,
                    100))
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    screen.get_width() - 50,
                    300))
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    screen.get_width() / 2,
                    300))
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    50,
                    300))
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    50,
                    100))
            game.enemies.append(
                enemy.Enemy(
                    screen,
                    'enemyship1.png',
                    game.ENEMY_MAX_HEALTH,
                    game.ENEMY_BASE_DAMAGE,
                    game.ENEMY_SPEED,
                    screen.get_width() / 2,
                    100))
        if game.score >= game.LEVEL2_TARGET_SCORE:
            game.enemies.clear()
            game.projectiles.clear()
            game.level = "level3"

    def level3():
        """
        Level 3 of the game
        Continuously creates 3 boss type enemies untill target score is reached
        calls game_over once target is reached
        """
        if not game.enemies:
            game.enemies.append(
                boss.Boss(
                    screen,
                    'enemyship2.png',
                    game.ENEMY_MAX_HEALTH * 2,
                    game.ENEMY_BASE_DAMAGE * 3,
                    game.ENEMY_SPEED * 1.25,
                    screen.get_width() / 2,
                    100))
            game.enemies.append(
                boss.Boss(
                    screen,
                    'enemyship2.png',
                    game.ENEMY_MAX_HEALTH * 2,
                    game.ENEMY_BASE_DAMAGE * 3,
                    game.ENEMY_SPEED * 1.25,
                    screen.get_width() - 50,
                    300))
            game.enemies.append(
                boss.Boss(
                    screen,
                    'enemyship2.png',
                    game.ENEMY_MAX_HEALTH * 2,
                    game.ENEMY_BASE_DAMAGE * 3,
                    game.ENEMY_SPEED * 1.25,
                    50,
                    300))

        if game.score >= game.LEVEL3_TARGET_SCORE:
            print("You win!")
            game.game_over()

    def play():
        """
        Handle the main gameplay loop.

        Processes user input, updates game objects, handles collisions,
        and displays the appropriate game state (levels, game over).
        """
        info(p.max_health, p.health, game.level, game.score)
        for event in pygame.event.get():
            # Resizing player with mousewheel
            if event.type == pygame.MOUSEWHEEL:
                p.resize(event.y)
            if event.type == pygame.QUIT:
                game.running = False
            # Player shooting with left mouse click or space
            if ((event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
                p.shoot()
            # Enemy shooting automatically
            if event.type == game.ENEMY_SHOOT:
                for en in game.enemies:
                    en.shoot()

        # Player movement and exiting the menu with keyboard
        keys = pygame.key.get_pressed()
        if any(
            keys[key] for key in [
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_w,
                pygame.K_a,
                pygame.K_s,
                pygame.K_d]):
            p.move(keys)
        if keys[pygame.K_ESCAPE]:
            game.in_menu = True

        for proj in game.projectiles[:]:
            proj.move()
            proj.draw(screen)

            # Check projectile for collision with enemies
            # if hit then add 5 points to score, print message with damage info,
            # remove projectile and damage the enemy
            if proj.shooter == "player":
                for en in game.enemies[:]:
                    if proj.hitbox.colliderect(en.hitbox):
                        if not en.dying:
                            print(
                                "Player an enemy with: ",
                                proj.damage,
                                " damage!")
                            game.score += 5
                            en.hit(proj.damage)
                        if proj in game.projectiles:
                            game.projectiles.remove(proj)
                        break

            else:
                # Check projectile for collision with player
                # if hit damage the player, remove projectile and print damage info
                if proj.hitbox.colliderect(p.hitbox):
                    print(
                        "Enemy the player with: ",
                        proj.damage,
                        " damage!")
                    p.hit(proj.damage)
                    proj.shooter.promotion()
                    if proj in game.projectiles:
                        game.projectiles.remove(proj)

            # Remove projectile if it goes off-screen
            if proj in game.projectiles and (
                    proj.y < 0 or proj.y > screen.get_height()):
                game.projectiles.remove(proj)

        screen.blit(p.image, (p.x, p.y))

        for en in game.enemies[:]:
            en.move(keys)
            screen.blit(en.image, (en.x, en.y))

        # If the game is over display Game Over, wait 2 second then call reset and
        # put player in the menu
        if game.level == "over":
            game_over_text = game_over_font.render(
                "Game Over", True, (255, 10, 10))
            screen.blit(
                game_over_text,
                (screen.get_width() / 2 - game_over_text.get_width() / 2,
                 screen.get_height() / 2 - game_over_text.get_height() / 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            game.in_menu = True
            reset()
        if game.in_menu:
            menu()
        elif game.level == "level1":
            level1()
        elif game.level == "level2":
            level2()
        elif game.level == "level3":
            level3()

    font = pygame.font.SysFont('Futura', 20)
    game_over_font = pygame.font.SysFont('Rocket', 50)

    clock = pygame.time.Clock()


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
