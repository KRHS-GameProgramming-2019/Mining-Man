#Ore blocks file, add different ones (color, texture)

import math, pygame, random


ores = []

class Ore():
    def __init__(self, kind=None, pos=[0]):
        self.sound = pygame.mixer.Sound('Sound/pickaxe/test.ogg')
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
            self.image = pygame.image.load("images/Ores/coalDirt.png")
        elif kind == "iron":
            self.image = pygame.image.load("images/Ores/IRONDirt.png")
        elif kind == "ruby":
            self.image = pygame.image.load("images/Ores/RubieDirt.png")
        elif kind == "diamond":
            self.image = pygame.image.load("images/Ores/diamondDirt.png")
        elif kind == "amethyst":
            self.image = pygame.image.load("images/Ores/AmethestDirt.png")
        elif kind == "Emerald":
            self.image = pygame.image.load("images/Ores/EmeraldDirt.png")
        elif kind == "Rainbow":
            self.image = pygame.image.load("images/Ores/RainbowDirt.png")
        elif kind == "dirt":
            self.image = pygame.image.load("images/Ores/BaseDirt.png")
        elif kind == "dead":
            self.image = pygame.image.load("images/Ores/Dead.png")
                       
                       
        self.rect = self.image.get_rect(topleft = pos)
        
        self.living = True
        self.kind = kind
        
      
    def __str__(self):
        return self.kind + " at " + str(self.rect.left)+ ", " + str(self.rect.top)
        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
     
    def moveOver(self):     
        self.rect = self.rect.move([80,0])
        
    def moveDown(self):     
        self.rect = self.rect.move([0,80])
    
    def moveUp(self):     
        self.rect = self.rect.move([0,-80])
        
    def kill(self):
        self.living = False
    
    def oreCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            return True
        return False
        
    def pickCollide(self, other):
        self.sound.play()
        if self != other:
            if self.rect.right > other.rect.centerx:
                if self.rect.left < other.rect.centerx:
                    if self.rect.bottom > other.rect.centery:
                        if self.rect.top < other.rect.centery:
                            self.sound.play()
                            self.living = False
                            return True
        return False
    
    


