import pygame
from math import *

#Pickaxe(s),    one breaks clusters and the other one breaks one block, only on the first row

class Pickaxe():
    def __init__(self, pos=[860,595]):
        self.image = pygame.image.load("images/Pickaxe/pickaxe.png")
        self.rect = self.image.get_rect(bottomright = pos)
        self.maxSpeed = -3
        self.startPos = pos
        self.speed = self.speedx, self.speedy = 0,0
        self.launched = False
        self.rx = self.rect.centerx
        self.ry = self.rect.centery
        self.target = [None, None]
        self.direct = ""
        
    def go(self, pos):
        xdist = float(self.rect.centerx - pos[0])
        ydist = float(self.rect.centery - pos[1])
        if xdist > 0 and ydist > 0:
            angle = degrees(atan(ydist/xdist))
            
            
            self.speedx = self.maxSpeed * cos(radians(angle))
            self.speedy = self.maxSpeed * sin(radians(angle))
            self.target = pos
            self.direct = "send"
            self.launched = True
    
    def back(self):
        xdist = float(self.rect.centerx - self.startPos[0])
        ydist = float(self.rect.centery - self.startPos[1])
        if xdist < 0 and ydist < 0:
            angle = degrees(atan(ydist/xdist))
            
            self.speedx = -(self.maxSpeed * cos(radians(angle)))
            self.speedy = -(self.maxSpeed * sin(radians(angle)))
            self.target = self.startPos
            self.direct = "back"
            self.launched = True
    
    
    
    def move(self):
        self.rx += self.speedx
        self.ry += self.speedy
        x = int(self.rx)
        y = int(self.ry)
        self.rect.center = [x,y]
        
    def update(self):
        self.move();
        if self.direct == "send":
            if self.rect.centerx < self.target[0] and self.rect.centery < self.target[1]:
                print("hit target", self.rect.centerx, self.rect.centery, self.target)
                self.back()
        elif self.direct == "back":
            if self.rx > self.target[0] and self.ry > self.target[1]:
                self.rect = self.image.get_rect(bottomright = self.startPos)
                self.speed = self.speedx, self.speedy = 0,0
                self.launched = False
                self.rx = self.rect.centerx
                self.ry = self.rect.centery
                self.target = [None, None]
                self.direct = ""
