import pygame
from asterboids.sky import Sky
from asterboids.boid import Boid
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Asterboids")
    
    running = True
    sky = Sky(800, 600, 100)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()
        

        sky.update()
        # Update the display
    
    pygame.quit()