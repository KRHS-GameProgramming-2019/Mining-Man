from sys import *
from math import *
import pygame


class Button():
    def __init__(self, name, pos=[0,0]):
        self.name=name
        self.baseImage=pygame.image.load("Images/Buttons/"+name+".png")
        self.hoverImage=pygame.image.load("Images/Buttons/"+name+"_hover.png")
        self.clickedImage=pygame.image.load("Images/Buttons/"+name+"_clicked.png")
        self.image=self.baseImage
        self.rect=self.image.get_rect(topleft = pos)
        
    def update(self, pos, clicked):
        if (pos[0] > self.rect.left and 
            pos[0] < self.rect.right and 
            pos[1] > self.rect.top and 
            pos[1] < self.rect.bottom):
                if clicked == (0,0,0):
                    self.image = self.hoverImage
                else:
                    self.image = self.clickedImage
        else:
                self.image = self.baseImage
                
    def click(self, pos):
        if (pos[0] > self.rect.left and 
            pos[0] < self.rect.right and 
            pos[1] > self.rect.top and 
            pos[1] < self.rect.bottom):
                self.image = self.clickedImage
                return True
        else:
                self.image = self.baseImage
                return False
        
        
        
        
