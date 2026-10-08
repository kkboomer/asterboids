import pygame, math

from asterboids.projectile import Projectile
class Player:
    FRICTION = .99
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.angle = 0.0
        self.cooldown = 0
        self.projectiles = []
    # the player will be able to fire a projectile, if it hits a boid, it gets deleted
    def update(self, maxvel = 5):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 0.1
        if keys[pygame.K_RIGHT]:
            self.angle += 0.1
        if keys[pygame.K_UP]:
            accelX = math.cos(self.angle) * 0.1
            accelY = math.sin(self.angle) * 0.1
            self.xvel += accelX
            self.yvel += accelY
        if keys[pygame.K_SPACE] and self.cooldown == 0:
                self.fire()
                self.cooldown = 30
        
        # self.move()
        self.xvel *= self.FRICTION
        self.yvel *= self.FRICTION
        vel = (self.xvel**2 + self.yvel**2)**.5
        if vel > maxvel:
            self.xvel *= maxvel/vel
            self.yvel *= maxvel/vel
        self.x += self.xvel
        self.y += self.yvel 
        width, height = pygame.display.get_surface().get_size()
        self.x = self.x % width
        self.y = self.y % height
        self.draw(pygame.display.get_surface())
        if self.cooldown > 0:
            self.cooldown -= 1
    
    def draw(self, screen):
        # self.angle = math.atan2(self.yvel, self.xvel)    
        base_pts = [(10,0), (-5,5), (-5,-5)]
        rotated_pts = []
        for pt in base_pts:
            x = pt[0] * math.cos(self.angle) - pt[1] * math.sin(self.angle)
            y = pt[0] * math.sin(self.angle) + pt[1] * math.cos(self.angle)
            rotated_pts.append((x + self.x, y + self.y))   
        color = "lightsalmon"   
        pygame.draw.polygon(screen, color, rotated_pts)
    def fire(self):
        p = Projectile(self.x, self.y, math.cos(self.angle), math.sin(self.angle))
        self.projectiles.append(p)