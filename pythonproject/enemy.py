# pylint: disable=import-error, no-member, attribute-defined-outside-init
import pygame
import ship
import game
import projectile


class Enemy(ship.Ship):
    def __init__(self, screen, image, max_health, base_damage, speed, x, y):
        super().__init__(screen, image, max_health, base_damage, speed, x, y)
        self.xdirection = 1
        self.ydirection = 0
        self.dying = False
        self.time = 0

    def move(self, keys, delta_time):
        if self.dying:
            if pygame.time.get_ticks() - self.time > 500:
                game.enemies.remove(self)
            return

        self.x += self.speed * delta_time * self.xdirection
        self.y += self.speed * delta_time * self.ydirection
        if (self.x >= self.screen.get_width() - self.image.get_width() - 50
                and self.ydirection == 0):
            self.xdirection = 0
            self.ydirection = 1
        elif self.y >= 300 and self.xdirection in (0, 1):
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
        if not self.dying:
            self.image = pygame.image.load(
                'sprites\\explosion.png').convert_alpha()
            self.image = pygame.transform.scale(
                self.image, (self.shipsize, self.shipsize))

            print("enemy has died.")
            game.score += 20
            self.dying = True
            self.time = pygame.time.get_ticks()
            print("score: ", game.score)

    def promotion(self):
        self.shipsize += 16
        self.damage = self.base_damage * (self.shipsize / 100)
        self.image = pygame.transform.scale(
            self.image, (self.shipsize, self.shipsize))
        self.hitbox = pygame.Rect(
            self.x,
            self.y,
            self.image.get_width(),
            self.image.get_height())

    def shoot(self):
        if self.dying:
            return
        game.projectiles.append(
            projectile.Projectile(
                self.x + self.shipsize / 2,
                self.y + self.shipsize,
                self.shipsize / 2,
                game.PROJECTILE_SPEED,
                self.damage,
                self))
