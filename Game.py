#Main game file
import pygame, sys, math, random
from Player import * 
from Screens import *
from Getters import *
from Settings import *
from options import *
from practice import *
from Ore import *
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)
screens = "menu"

clock = pygame.time.Clock()

while True:
    #---------------------------Menu------------------------------------
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
                    
    #--------------------------Unicorn----------------------------------
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

    #--------------------------Options----------------------------------             
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
                
    #---------------------------Game------------------------------------
    image = pygame.image.load("images/TitleScreen/tempbackground.png")
    imgRect = image.get_rect()
    pick = Pickaxe()
    guy = Guy()
    ores = []
    oreTimer = 0
    oreTimerMax = 60*3
    while screens == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit();
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not pick.launched:
                    pick.go(event.pos)
                    print(event.pos)
                #elif pick.launched:  #return before hits spot
                #   pick.back()
        
        if oreTimer < oreTimerMax:
            oreTimer += 1
        else:
            oreTimer = 0
            for ore in ores:
                ore.moveOver()
            for i in range(7):
                ores += [Ore(None, [0, i*80])]
        
        pick.update()   
        
        if pick.canHit:
            for ore in ores:
                if ore.pickCollide(pick):
                    ores.remove(ore)
                    
                
        
        screen.blit(image, imgRect)
        screen.blit(guy.image, guy.rect)
        for ore in ores:
            screen.blit(ore.image, ore.rect)
        screen.blit(pick.image, pick.rect)
        pygame.display.flip()
        print(clock.get_fps())
        clock.tick(60)
    

