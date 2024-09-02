import pygame
from constants import *
import player

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

    # Instantiate the Player
    player.Player.containers = (updatable, drawable)
    character = player.Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT /2)

    

   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        
        # Control the frame rate to 60 FPS
        dt = clock.tick(60)  # Use the tick() method on the Clock instance
        
        # Draw the player
        for u in updatable:
            u.update(dt)

        for d in drawable:
           d.draw(screen)

         
        # Update screen after receiving all inputs
        pygame.display.flip()

if __name__ == "__main__":
    main()


