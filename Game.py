#Main game file
import pygame, sys, math, random
import Titlescreen, Screens, Getters, Settings
from Player import * 
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)




screens = "menu"




while True:
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.K_RETURN:
                image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
                imgRect = image.get_rect()
                
            

    
    while screens == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();

       

    

