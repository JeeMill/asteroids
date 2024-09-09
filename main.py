import pygame
from constants import *
import player, asteroid, asteroidfield, shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Instantiate the Clock object
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Instantiate the Player
    player.Player.containers = (updatable, drawable)
    character = player.Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT /2)

    # Insantiate Asteroids
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)

    ast = asteroidfield.AsteroidField()
    updatable.add(ast)

    # Instantiate Shots
    shot.Shot.containers = (updatable, drawable, shots)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        
        # Control the frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0  # Use the tick() method on the Clock instance
        
        # Draw the player
        for u in updatable:
            u.update(dt)

        for d in drawable:
           d.draw(screen)

        for a in asteroids:
            a.update(dt)
            a.draw(screen)

        for c in asteroids:
            if c.collision(character) == True:
                print("Game Over!")
                sys.exit()

            for s in shots:
                if c.collision(s) == True:
                    c.split()
                    s.kill()
         
        # Update screen after receiving all inputs
        pygame.display.flip()

if __name__ == "__main__":
    main()


