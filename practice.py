import pygame, sys, math, random
from Pickaxe import *
from Player import*
from Game import *
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)


image = pygame.image.load("images/TitleScreen/tempbackground.png")
imgRect = image.get_rect()




pick = Pickaxe()
Guy = Guy()


while True:
    for event in pygame.event.get():
        coal = pygame.image.load("images/ores/coal.png")
        image2

        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not pick.launched:
                pick.go(event.pos)
                print(event.pos)
            #elif pick.launched:  #return before hits spot
            #    pick.back()
        
    
    pick.update()   
    
    screen.blit(image, imgRect)
    screen.blit(Guy.image, Guy.rect)
    screen.blit(pick.image, pick.rect)
    pygame.display.flip()
    
   

