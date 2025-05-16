#pylint: disable=import-error, no-member
import pygame
import ship
import game
import projectile


class Player(ship.Ship):
    def __init__(self, screen, image, max_health, base_damage, speed, x, y, score):
        super().__init__(screen, image, max_health, base_damage, speed, x, y)
        self.cooldown = 0

    def resize(self, eventy):
        if eventy == 1 and self.shipsize < 176:
            self.shipsize += 16
        if eventy == -1 and self.shipsize > 32:
            self.shipsize -= 16
        self.damage = self.base_damage * (self.shipsize / 100)
        self.image = pygame.transform.scale(self.image, (self.shipsize, self.shipsize))
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self, keys, delta_time):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed * delta_time
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed * delta_time
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed * delta_time
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed * delta_time
        super().move(keys, delta_time)

    def hit(self,damage_taken):
        print("remaining health: ", self.health)
        super().hit(damage_taken)

    def death(self):
        print("you have died.")
        game.game_over()

    def shoot(self):
        if pygame.time.get_ticks() - self.cooldown > 110+self.shipsize*1.65:
            self.cooldown = pygame.time.get_ticks()
            game.projectiles.append(
                projectile.Projectile(
                    self.x + self.shipsize / 2,
                    self.y, self.shipsize / 2,
                    game.PROJECTILE_SPEED,
                    self.damage,
                    "player")
            )
