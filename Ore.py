#Ore blocks file, add different ones (color, texture)

from math import *
from pygame import*
from practice import *
from Game import *


ores = []

class Ore():
    def __init__(self, kind, pos):
        
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
        else:
            self.image = pygame.image.load("images/Ores/dirt.png")
                       
            self.rect = self.image.get_rect()
        ores.append(self)
        
        
        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
     
     
        
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
    
    


