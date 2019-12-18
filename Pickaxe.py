import pygame
from math import *

#Pickaxe(s),    one breaks clusters and the other one breaks one block, only on the first row

class Pickaxe():
    def __init__(self, pos=[860, 585]):
        self.image = pygame.image.load("images/Pickaxe/pickaxe.png")
        self.rect = self.image.get_rect(bottomright = pos)
        self.maxSpeed = -3
        self.speed = self.speedx, self.speedy = 0,0
        self.launched = False
        self.rx = self.rect.centerx
        self.ry = self.rect.centery
        
    def go(self, pos):
        xdist = float(self.rect.centerx - pos[0])
        ydist = float(self.rect.centery - pos[1])
        if xdist > 0:
            angle = degrees(atan(ydist/xdist))
            
            print(angle)
            self.speedx = self.maxSpeed * cos(radians(angle))
            self.speedy = self.maxSpeed * sin(radians(angle))
            self.launched = True
        
    def move(self):
        self.rx += self.speedx
        self.ry += self.speedy
        x = int(self.rx)
        y = int(self.ry)
        self.rect.center = [x,y]
        
    def update(self):
        self.move();
