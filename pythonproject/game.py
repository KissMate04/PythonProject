import pygame

projectiles = []
enemies = []
level = "level1"
score = 0

def game_over():
    enemies.clear()
    projectiles.clear()
    global level
    level = "over"

