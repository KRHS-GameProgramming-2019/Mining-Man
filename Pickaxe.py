import pygame
from math import *

#Pickaxe(s),    one breaks clusters and the other one breaks one block, only on the first row

class Pickaxe():
    def __init__(self, pos=[860,595]):
        self.images = [pygame.image.load("images/Pickaxe/pickaxe1.png"),
                       pygame.image.load("images/Pickaxe/pickaxe2.png"),
                       pygame.image.load("images/Pickaxe/pickaxe3.png"),
                       pygame.image.load("images/Pickaxe/pickaxe4.png"),
                       pygame.image.load("images/Pickaxe/pickaxe5.png"),
                       pygame.image.load("images/Pickaxe/pickaxe6.png"),
                       pygame.image.load("images/Pickaxe/pickaxe7.png"),
                       pygame.image.load("images/Pickaxe/pickaxe8.png")
        ]
        self.frame = 0
        self.frameMax = len(self.images)-1 
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(bottomright = pos)
        self.maxSpeed = -15
        self.startPos = pos
        
        self.speed = self.speedx, self.speedy = 0,0
        self.launched = False
        self.rx = self.rect.centerx
        self.ry = self.rect.centery
        self.target = [None, None]
        self.direct = ""
        
        self.animationTimer = 0
        self.animationTimerMax = 60/10
        
        self.canHit = False
        
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
            self.canHit = True
            
    def move(self):
        self.rx += self.speedx
        self.ry += self.speedy
        x = int(self.rx)
        y = int(self.ry)
        self.rect.center = [x,y]
        
    def update(self):
        self.move()
        
        if self.direct == "send":
            self.animate2()
            if self.rect.centerx < self.target[0] and self.rect.centery < self.target[1]:
                print("hit target", self.rect.centerx, self.rect.centery, self.target)
                self.back()
        elif self.direct == "back":
            self.canHit = False
            self.animate()
            if self.rx > self.target[0] and self.ry > self.target[1]:
                self.rect = self.image.get_rect(bottomright = self.startPos)
                self.speed = self.speedx, self.speedy = 0,0
                self.launched = False
                self.rx = self.rect.centerx
                self.ry = self.rect.centery
                self.target = [None, None]
                self.direct = ""
                self.frame = 0
                self.animationTimer = 0
                self.image = self.images[self.frame]


    def animate(self):
        self.animationTimer+= 1
        if self.animationTimer > self.animationTimerMax:
            self.animationTimer = 0
            
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
            
    def animate2(self):
        self.animationTimer+= 1
        if self.animationTimer > self.animationTimerMax:
            self.animationTimer = 0
            
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += -1
            self.image = self.images[self.frame]
