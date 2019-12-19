#Main game file
import pygame, sys, math, random
from Player import * 
from Screens import *
from Getters import *
from Settings import *
from options import *
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)




screens = "menu"





while True:
    
    image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
    imgRect = image.get_rect()
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
                    import practice
                elif event.key == pygame.K_o:
                    screens = "options"
                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
                elif event.key == pygame.K_u:
                    screens = "unicorn"
                    
                    
                    
        screen.blit(image, imgRect)
        pygame.display.flip()
                    
      
    image = pygame.image.load("images/TitleScreen/f.jpg")
    imgRect = image.get_rect()
    while screens == "unicorn":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "menu"
                
                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
                    
                    
                    
        screen.blit(image, imgRect)
        pygame.display.flip()  
      
      
                    
                    
    image = pygame.image.load("images/TitleScreen/titlescreenbackground-optionstest.png")
    imgRect = image.get_rect()
    while screens == "options":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "menu"
                    
                    
        screen.blit(image, imgRect)
        pygame.display.flip()
                    
                    
                    
                    
       

    image = pygame.image.load("images/Background/background.png")
    imgRect = image.get_rect()
    while screens == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
                

        screen.blit(image, imgRect)
        pygame.display.flip()

    

