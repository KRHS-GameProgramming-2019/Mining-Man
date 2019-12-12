#Main game file
import pygame, sys, math, random
import Titlescreen, Screens, Getters, Settings
from Player import * 
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)


image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
imgRect = image.get_rect()

screens = "menu"




while True:
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.K_RETURN:
                image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
                imgRect = image.get_rect()
                
                screen.blit(image, imgRect)
        pygame.display.flip()

    
    while screens == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();

        pygame.display.flip()

    

