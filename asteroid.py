import circleshape
import pygame
import constants
import random


class Asteroid(circleshape.CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS * 2:
            return

        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)

        new_radius = (self.radius - constants.ASTEROID_MIN_RADIUS) / 2

        one = Asteroid(self.position.x, self.position.y, new_radius)
        two = Asteroid(self.position.x, self.position.y, new_radius)
        
        one.velocity = vector_one * 1.2
        two.velocity = vector_two * 1.2

        for container in Asteroid.containers:
            container.add(one)
            container.add(two)

    def update(self, dt):
        self.position += (self.velocity * dt)

