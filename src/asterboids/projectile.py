class Projectile:
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel

    def update(self, maxvel = 5):
        vel = (self.xvel**2 + self.yvel**2)**.5
        if vel > maxvel:
            self.xvel *= maxvel/vel
            self.yvel *= maxvel/vel
        self.x += self.xvel
        self.y += self.yvel
        

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, "yellow", (int(self.x), int(self.y)), 5)