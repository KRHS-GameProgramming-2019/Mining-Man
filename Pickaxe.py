import pygame

#Pickaxe(s),    one breaks clusters and the other one breaks one block, only on the first row

class Pickaxe():
    def __init__(self, pos=[860, 585]):
        self.image = pygame.image.load("images/Pickaxe/pickaxe.png")
        self.rect = self.image.get_rect(bottomright = pos)
        self.maxSpeed = self.maxSpeedx, self.maxSpeedy = -5,-5
        self.speed = self.speedx, self.speedy =  0,0
        
    def go(self):
        self.speed = self.maxSpeed
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def update(self):
        self.move();
