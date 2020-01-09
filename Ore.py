#Ore blocks file, add different ones (color, texture)

from math import *
from pygame import*

class Ore():
    def __init__(self, image, pos):
        self.images = [pygame.image.load("images/Ores/coal.png"),
                       pygame.image.load("images/Ores/IRON.png"),
                       pygame.image.load("images/Ores/diamond.png"),
                       pygame.image.load("images/Ores/Rubie.png"),
                       pygame.image.load("images/Ores/Amethest.png")]
                       
        self.rect = self.image.get_rect()
        self.frame = 0
        self.frameMax = len(self.images)-1 
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        
        
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
    
    

# ~ image1 = pygame.image.load("images/Background/background.png")
    # ~ rect1 = image1.get_rect(topleft = [0,0])
    # ~ image2 = pygame.image.load("images/ores/coal.png")
    # ~ rect2 = image2.get_rect(midtop = [940/2,0])
    # ~ image3 = pygame.image.load("images/ores/rubie.png")
    # ~ rect3 = image.get_rect(midleft = [300,600])
    # ~ image4 = pygame.image.load("images/ores/IRON.png")
    # ~ rect4 = image.get_rect(bottomright = [600,940])
    # ~ image5 = pygame.image.load("images/ores/Amethest.png")
    # ~ rect5 = image.get_rect(midbottom = [940/2,600])
