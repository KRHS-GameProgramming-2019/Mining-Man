#Ore blocks file, add different ones (color, texture)

from math import *
from pygame import*

class Ore():
     def __init__(self, image, pos):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
    
    

