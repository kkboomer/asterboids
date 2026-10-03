import pygame
from asterboids.sky import Sky
from asterboids.boid import Boid
from asterboids.player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Asterboids")
    
    running = True
    sky = Sky(800, 600, 100, Player(400, 300, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("dodgerblue")
        sky.player.update()
        sky.update()
        pygame.display.flip()
    
    pygame.quit()