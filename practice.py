import pygame, sys, math, random
from Pickaxe import *
from Player import*
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)


image = pygame.image.load("images/TitleScreen/tempbackground.png")
imgRect = image.get_rect()


pick = Pickaxe()
Guy = Guy()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not pick.launched:
                pick.go(event.pos)
                print(event.pos)
            if pick.launched:
                pick.back([850,590])
        
    
    pick.update()   
    
    if pick.rect.left < 0 or pick.rect.top < 0:
        pick = Pickaxe()   
    
    screen.blit(image, imgRect)
    screen.blit(Guy.image, Guy.rect)
    screen.blit(pick.image, pick.rect)
    pygame.display.flip()
    
   

