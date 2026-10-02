import random
from asterboids.boid import Boid
class Sky:
    def __init__(self,width, height, boid_num):
        self.width = width
        self.height = height
        self.boid_num = boid_num
        self.boids = []
        self.predatorNum = 4
        #self.predators = []
        self.BOUNCE_OFF_WALLS = True
        self.WRAP_AROUND = False
        for i in range(boid_num):
            self.boids.append(Boid(
                random.uniform(0, width), 
                random.uniform(0, height), 
                random.uniform(-1, 1), 
                random.uniform(-1, 1), False
                ))
        for i in range(self.predatorNum):
            self.boids.append(Boid(
                random.uniform(0, width), 
                random.uniform(0, height), 
                random.uniform(-1, 1), 
                random.uniform(-1, 1), True
                ))
    
    def update(self):
        for b in (self.boids):
            flockXVel, flockYVel = self.flock(b, 50, .0003)
            alignXVel, alignYVel = self.align(b, 50, .01)
            avoidXVel, avoidYVel = self.avoid(b, 50, .0003)
            predXVel, predYVel = self.predator(b, 150, .0005)
            b.update([flockXVel+alignXVel+avoidXVel+predXVel, flockYVel+alignYVel+avoidYVel+predYVel])
            #either wrap around or bounce off the walls, we decide later
            if self.BOUNCE_OFF_WALLS:
                b.bounceOffWalls(self.width, self.height)
            elif self.WRAP_AROUND:
                b.wrapAround(self.width, self.height)
    
    ## we apply the logic for the rules here
    # rule 1: steer twrd  center of nearby boids
    def flock(self, boid, distance, power):
        neighbors = [b for b in self.boids if b != boid and b.getDistance(boid) < distance]
        if not neighbors:
            return 0, 0
        meanX = sum([b.x for b in neighbors])/len(neighbors)
        meanY = sum([b.y for b in neighbors])/len(neighbors)
        return (meanX - boid.x) *power, (meanY - boid.y) * power
    
    
    # mimic dir and speed of nearby boids
    def align(self,boid, distance, power):
        neighbors = [b for b in self.boids if b != boid and b.getDistance(boid) < distance]
        if not neighbors:
            return 0, 0
        meanXVel = sum([b.xvel for b in neighbors])/len(neighbors)
        meanYVel = sum([b.yvel for b in neighbors])/len(neighbors)
        return (meanXVel - boid.xvel) *power, (meanYVel - boid.yvel) * power
    
    def avoid(self, boid, distance, power):
        neighbors = [b for b in self.boids if b != boid and b.getDistance(boid) < distance]
        if not neighbors:
            return 0, 0
        closenessX, closenessY = 0, 0
        for n in neighbors:
            closeness = distance - boid.getDistance(n)
            closenessX += (boid.x - n.x) * closeness
            closenessY += (boid.y - n.y) * closeness
        return (closenessX) *power, (closenessY) * power
    
    def predator(self, boid, distance, power):
        closenessX, closenessY = 0, 0
        predators = [b for b in self.boids if b.isPreadator]
        for p in predators:
            dist = boid.getDistance(p)
            if dist < distance:
                closeness = distance - dist
                closenessX += (boid.x - p.x) * closeness
                closenessY += (boid.y - p.y) * closeness
        return (closenessX) * power, (closenessY) * power