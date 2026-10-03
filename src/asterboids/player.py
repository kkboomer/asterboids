import pygame, math
class Player:
    def __init__(self, x, y, xvel, yvel):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
    # the player will be able to fire a projectile, if it hits a boid, it gets deleted
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.xvel -= 1
        if keys[pygame.K_RIGHT]:
            self.xvel += 1
        if keys[pygame.K_UP]:
            self.yvel -= 1
        if keys[pygame.K_DOWN]:
            self.yvel += 1
        # self.move()
        self.x += self.xvel
        self.y += self.yvel
        self.draw(pygame.display.get_surface())
    
    def draw(self, screen):
        angle = math.atan2(self.yvel, self.xvel)    
        base_pts = [(10,0), (-5,5), (-5,-5)]
        rotated_pts = []
        for pt in base_pts:
            x = pt[0] * math.cos(angle) - pt[1] * math.sin(angle)
            y = pt[0] * math.sin(angle) + pt[1] * math.cos(angle)
            rotated_pts.append((x + self.x, y + self.y))   
        color = "lightsalmon"   
        pygame.draw.polygon(screen, color, rotated_pts)