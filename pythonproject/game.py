# pylint: disable=import-error, no-member
"""
Module for managing game state and global game settings.

Contains global variables for game settings, state tracking,
and lists of game objects (projectiles, enemies).
"""
import pygame

pygame.init()

# Settings:
# game speed
DELTA_TIME = 0.8
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
CHANCE_OF_DIRECTION_CHANGE = 0.01   # 0.01 = 1% chance
# projectile
PROJECTILE_SPEED = 4
# score to progress
LEVEL1_TARGET_SCORE = 100
LEVEL2_TARGET_SCORE = 500
LEVEL3_TARGET_SCORE = 800
# End of settings

projectiles = []
enemies = []
level = "level1"
score = 0
running = True
in_menu = True


def game_over():
    """
    Handle game over state.

    Clears all enemies and projectiles from the game, and
    sets the game level to "over" to trigger the game over screen.
    """
    enemies.clear()
    projectiles.clear()
    global level
    level = "over"
