 #The "guy" that throws the pickaxe, must have animations

from sys import *
from math import *
import pygame


class Guy():
    def __init__(self, pos=[900,640]):
        self.image = pygame.image.load("images/Player/NewGuy.png")
        self.rect = self.image.get_rect(bottomright = pos)
        self.speed = self.speedx, self.speedy =  0,0
        
