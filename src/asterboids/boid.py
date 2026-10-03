import math, pygame
class Boid:
    def __init__(self, x, y, xvel, yvel, isPreadator):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.isPreadator = isPreadator
        self.draw(pygame.display.get_surface())
    def update(self, newVel):
        self.xvel += newVel[0]
        self.yvel += newVel[1]
        # update the boid location
        self.moveForward()
        self.draw(pygame.display.get_surface())
        return
    def getDistance(self, boid):
        return ((self.x-boid.x)**2 + (self.y-boid.y)**2)**.5
    
    def getLocation(self):
        return (self.x, self.y)    
    
    def moveForward(self, minVel = 1, maxVel = 5):
        # check and limit velocity
        vel = self.getVelocity()
        if vel > 0:
            if vel < minVel:
                self.xvel *= minVel/vel
                self.yvel *= minVel/vel
            elif vel > maxVel:
                self.xvel *= maxVel/vel
                self.yvel *= maxVel/vel
        if math.isnan(self.xvel):
            self.xvel = 0
        if math.isnan(self.yvel):
            self.yvel = 0
            
        # safe to update pos now
        self.x += self.xvel
        self.y += self.yvel
        self.draw(pygame.display.get_surface())
        
    def getVelocity(self):
        return (self.xvel**2 + self.yvel**2)**.5
    
    def draw(self, screen):
        angle = math.atan2(self.yvel, self.xvel)
        
        base_pts = [(10,0), (-5,5), (-5,-5)]
        rotated_pts = []
        
        for pt in base_pts:
            x = pt[0] * math.cos(angle) - pt[1] * math.sin(angle)
            y = pt[0] * math.sin(angle) + pt[1] * math.cos(angle)
            rotated_pts.append((x + self.x, y + self.y))
        if self.isPreadator:
            color = (255, 0, 0)
        else:
            color = (255, 255, 255)
        pygame.draw.polygon(screen, color, rotated_pts)
    def bounceOffWalls(self, width, height):
        pad, turn = 30, .2
        # pad is the how close the boid can get to the border of the screen
        # turn is what we either add or subrtact form the velocity to help the boid avoid the edge
        if self.x < pad:
            self.xvel += turn
        if self.x > width - pad:
            self.xvel -= turn
        if self.y < pad:
            self.yvel += turn
        if self.y > height - pad:
            self.yvel -= turn
            
    def wrapAround(self, width, height):
        if self.x < 0:
            self.x += width
        elif self.x > width:
            self.x -= width
        if self.y < 0:
            self.y += height
        elif self.y > height:
            self.y -= height