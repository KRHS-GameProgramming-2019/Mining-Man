#Ore blocks file, add different ones (color, texture)

import math, pygame, random


ores = []

class Ore():
    def __init__(self, kind=None, pos=[0]):
        oreTypes = ["coal", "iron", "ruby", "diamond", "amethyst", "Emerald", "Rainbow"]
        if kind == None:
            num = random.randint(0,99)
            if num < 11:
                kind = "Rainbow"
            elif num < 11 + 11:
                kind = "diamond"
            elif num < 22 + 11:
                kind = "Emerald"
            elif num < 33 + 11:
                kind = "amethyst"
            elif num < 44 + 11:
                kind = "ruby"
            elif num < 55 + 11:
                kind = "iron"
            elif num < 66 + 11:
                kind = "coal"
                
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
        
        self.living = True
        
        
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
                            self.living = False
                            return True
        return False
        
    def pickCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.centerx:
                if self.rect.left < other.rect.centerx:
                    if self.rect.bottom > other.rect.centery:
                        if self.rect.top < other.rect.centery:
                            self.living = False
                            return True
        return False
    
    


