#Main game file
import pygame, sys, math, random
from Player import * 
from Screens import *
from Getters import *
from Settings import *
from options import *
from practice import *
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
                    
      
    image = pygame.image.load("images/TitleScreen/f.png")
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
                    
                    
                    
                    
       

    image1 = pygame.image.load("images/Background/background.png")
    rect1 = image1.get_rect(topleft = [0,0])
    image2 = pygame.image.load("images/ores/coal.png")
    rect2 = image2.get_rect(midtop = [940/2,0])
    image3 = pygame.image.load("images/ores/rubie.png")
    rect3 = image.get_rect(midleft = [300,600])
    image4 = pygame.image.load("images/ores/IRON.png")
    rect4 = image.get_rect(bottomright = [600,940])
    image5 = pygame.image.load("images/ores/Amethest.png")
    rect5 = image.get_rect(midbottom = [940/2,600])
    
    while screens == "game":
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit();
            
            

        screen.blit(image, imgRect)
        screen.blit(image1, rect1)
        screen.blit(image2, rect2)
        screen.blit(image3, rect3)
        screen.blit(image4, rect4)
        screen.blit(image5, rect5)
                

        
        pygame.display.flip()

    

