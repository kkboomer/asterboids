import pygame
class Projectile:
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.lifespan = 120

    def update(self, maxvel = 5):
        vel = (self.xvel**2 + self.yvel**2)**.5
        if vel > maxvel:
            self.xvel *= maxvel/vel
            self.yvel *= maxvel/vel
        self.x += self.xvel
        self.y += self.yvel
        self.draw(pygame.display.get_surface())
        self.lifespan -= 1
        
    def getDistance(self, boid):
        return ((self.x-boid.x)**2 + (self.y-boid.y)**2)**.5
        
    def draw(self, screen):
        color = "chocolate"
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)