import pygame
import ship
from game import game_over


class Player(ship.Ship):
    def __init__(self, screen, image, max_health, base_damage, speed, x, y, score):
        super().__init__(screen, image, max_health, base_damage, speed, x, y)

    def resize(self, eventy):
        if eventy == 1 and self.shipsize < 176:
            self.shipsize += 16
        if eventy == -1 and self.shipsize > 32:
            self.shipsize -= 16
        self.damage = self.base_damage * (self.shipsize / 100)
        self.image = pygame.transform.scale(self.image, (self.shipsize, self.shipsize))
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self, keys, delta_time):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
        if keys[pygame.K_UP]:
            self.y -= self.speed * delta_time
        if keys[pygame.K_DOWN]:
            self.y += self.speed * delta_time
        super().move(keys, delta_time)

    def hit(self,damage_taken):
        print("remaining health: ", self.health)
        super().hit(damage_taken)

    def death(self):
        print("you have died.")
        game_over()
