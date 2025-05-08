import pygame
import projectile

class Ship:
    def __init__(self, screen, image,max_health, base_damage, speed, x,y):
        self.screen = screen
        self.shipsize = 32
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.shipsize, self.shipsize))
        self.max_health = max_health
        self.health = max_health
        self.base_damage = base_damage
        self.damage = base_damage * (self.shipsize / 100)
        self.speed = speed
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self, keys, delta_time):
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > self.screen.get_width() - self.shipsize:
            self.x = self.screen.get_width() - self.shipsize
        if self.y > self.screen.get_height() - self.shipsize:
            self.y = self.screen.get_height() - self.shipsize
        self.screen.blit(self.image, (self.x, self.y))

    def hit(self,damage_taken):
        self.health -= round(damage_taken)
        if self.health <= 0:
            self.death()

    def death(self):
        pass
