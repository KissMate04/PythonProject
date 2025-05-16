# pylint: disable=import-error, no-member
import pygame

pygame.init()

# Settings:
# enemy shooting cooldown
ENEMY_SHOOT = pygame.USEREVENT
pygame.time.set_timer(ENEMY_SHOOT, 1000)
# player
PLAYER_MAX_HEALTH = 100
PLAYER_SPEED = 4
PLAYER_BASE_DAMAGE = 63
# enemy
ENEMY_MAX_HEALTH = 100
ENEMY_SPEED = 4
ENEMY_BASE_DAMAGE = 20
# boss
BOSS_MAX_HEALTH = 200
BOSS_SPEED = 5
BOSS_BASE_DAMAGE = 60
# projectile
PROJECTILE_SPEED = 4
# score to progress
LEVEL1_TARGET_SCORE = 1
LEVEL2_TARGET_SCORE = 5
LEVEL3_TARGET_SCORE = 800
# End of settings

projectiles = []
enemies = []
level = "level1"
score = 0
running = True
in_menu = True


def game_over():
    enemies.clear()
    projectiles.clear()
    global level
    level = "over"
