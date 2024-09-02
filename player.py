import circleshape
import pygame
import constants


class Player(circleshape.CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        
        # super has position, velociy, radius

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Left
        if keys[pygame.K_a]:
            self.rotate(dt)

        # Right
        if keys[pygame.K_d]:
            self.rotate(dt * -1)

        # Move Forward
        if keys[pygame.K_w]:
            self.move(dt)

        # Move Backward
        if keys[pygame.K_s]:
            self.move(dt * -1)