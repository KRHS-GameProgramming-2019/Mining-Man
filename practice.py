import pygame, sys, math, random
from Pickaxe import *
from Player import*
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)


image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
imgRect = image.get_rect()


pick = Pickaxe()
Guy = Guy()

speedx = (-4)
speedy = (-4)
Pickspeed = [speedx, speedy]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            pick.go()
    
    pick.update()       
    
    screen.blit(image, imgRect)
    screen.blit(Guy.image, Guy.rect)
    screen.blit(pick.image, pick.rect)
    pygame.display.flip()
    
   

