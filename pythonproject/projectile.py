import pygame


class Projectile:
    def __init__(self, x, y, size, speed, damage, shooter):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.damage = damage
        self.hitbox = pygame.Rect(
            self.x,
            self.y-self.size*1.5,
            min(self.size/4, 15),
            min(self.size, 40)
        )
        self.shooter = shooter

    def move(self):
        if self.shooter == "player":
            self.y -= self.speed
        else:
            self.y += self.speed
        self.hitbox = pygame.Rect(
            self.x,
            self.y-self.size*1.5,
            min(self.size/4,15),
            min(self.size, 40)
        )

    def draw(self, screen):
        if self.shooter == "player":
            pygame.draw.rect(screen, (255, 100, 0), self.hitbox)
        else:
            pygame.draw.rect(screen, (100, 100, 255), self.hitbox)
