import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_MAX_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(angle)
        velocity_two = self.velocity.rotate(-angle)
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = velocity_one * 1.2
        ast2.velocity = velocity_two * 1.2