# pylint: disable=import-error, no-member, attribute-defined-outside-init
import random
import pygame
import enemy
import game
import ship



class Boss(enemy.Enemy):
    def __init__(self, screen, image, max_health, base_damage, speed, x, y):
        super().__init__(screen, image, max_health, base_damage, speed, x, y)

    def move(self, keys, delta_time):
        if self.dying:
            if pygame.time.get_ticks() - self.time > 500:
                game.enemies.remove(self)
            return

        self.x += self.speed * delta_time * self.xdirection
        self.y += self.speed * delta_time * self.ydirection
        if self.x >= self.screen.get_width() - self.image.get_width() - 20:
            self.xdirection = -1
        elif self.x <= 20:
            self.xdirection = 1
        if self.y >= 350:
            self.ydirection = -1
        elif self.y <= 30:
            self.ydirection = 1

        if random.random() < 0.005 and not self.dying:
            self.change_direction()

        ship.Ship.move(self, keys, delta_time)

    def change_direction(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        random_direction = random.choice(directions)
        self.xdirection = random_direction[0]
        self.ydirection = random_direction[1]

    def hit(self, damage_taken):
        super().hit(damage_taken)

        # Randomly change direction when hit
        if not self.dying:
            self.change_direction()
