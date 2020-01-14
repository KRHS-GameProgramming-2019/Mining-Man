#Ore blocks file, add different ones (color, texture)

import math, pygame, random


ores = []

class Ore():
    def __init__(self, kind=None, pos=[0]):
        oreTypes = ["coal", "iron", "ruby", "diamond", "amethyst", "Emerald", "Rainbow"]
        if kind == None:
            num = random.randint(0,99)
            if num < 2:
                kind = "Rainbow"
            elif num < 2 + 7:
                kind = "diamond"
            elif num < 9 + 9:
                kind = "Emerald"
            elif num < 18 + 10:
                kind = "amethyst"
            elif num < 28 + 13:
                kind = "ruby"
            elif num < 41 + 17:
                kind = "iron"
            elif num < 58 + 18:
                
            else:
                    kind = "dirt"
            
        if kind == "coal":
            self.image = pygame.image.load("images/Ores/coal.png")
        elif kind == "iron":
            self.image = pygame.image.load("images/Ores/IRON.png")
        elif kind == "ruby":
            self.image = pygame.image.load("images/Ores/Rubie.png")
        elif kind == "diamond":
            self.image = pygame.image.load("images/Ores/diamond.png")
        elif kind == "amethyst":
            self.image = pygame.image.load("images/Ores/Amethest.png")
        elif kind == "Emerald":
            self.image = pygame.image.load("images/Ores/Emerald.png")
        elif kind == "Rainbow":
            self.image = pygame.image.load("images/Ores/Rainbow.png")
        elif kind == "dirt":
            self.image = pygame.image.load("images/Ores/dirt.png")
                       
        self.rect = self.image.get_rect(topleft = pos)
        
        
        
        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
     
    def moveOver(self):
        self.rect = self.rect.move([80,0])
        
    def oreCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                if not self.didBounceX:
                                    self.speedx = -self.speedx
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.didBounceY = True
                                return True
        return False
    
    


