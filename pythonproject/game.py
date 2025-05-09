import pygame

pygame.init()

#Settings:
#enemy shooting cooldown
ENEMY_SHOOT = pygame.USEREVENT
pygame.time.set_timer(ENEMY_SHOOT, 1000)
#player
PLAYER_MAX_HEALTH = 100
PLAYER_SPEED = 4
PLAYER_BASE_DAMAGE = 63
#enemy
ENEMY_MAX_HEALTH = 100
ENEMY_SPEED = 4
ENEMY_BASE_DAMAGE = 20
#projectile
PROJECTILE_SPEED = 4
#End of settings

projectiles = []
enemies = []
level = "menu"
score = 0

def game_over():
    enemies.clear()
    projectiles.clear()
    global level
    level = "over"

