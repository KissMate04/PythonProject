import pygame
import ship
from game import enemies

class Enemy(ship.Ship):
    def __init__(self, screen, image, max_health, base_damage, speed, x, y):
        super().__init__(screen, image, max_health, base_damage, speed, x, y)
        self.xdirection = 1
        self.ydirection = 0

    def move(self, keys, delta_time):
        self.x += self.speed * delta_time * self.xdirection
        self.y += self.speed * delta_time * self.ydirection
        if self.x >= self.screen.get_width() - self.image.get_width() - 50 and self.ydirection == 0:
            self.xdirection = 0
            self.ydirection = 1
        elif self.y >= 300 and (self.xdirection == 0 or self.xdirection == 1):
            self.xdirection = -1
            self.ydirection = 0
        elif self.x <= 50 and self.ydirection == 0:
            self.xdirection = 0
            self.ydirection = -1
        elif self.y <= 50 and self.xdirection == 0:
            self.xdirection = 1
            self.ydirection = 0

        super().move(keys, delta_time)

    def death(self):
        print("enemy has died.")
        enemies.remove(self)

    def promotion(self):
        self.shipsize += 16
        self.damage = self.base_damage * (self.shipsize / 100)
        self.image = pygame.transform.scale(self.image, (self.shipsize, self.shipsize))
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

