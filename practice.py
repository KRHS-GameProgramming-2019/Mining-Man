import pygame, sys, math, random
from Pickaxe import *
from Player import*
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)



image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
imgRect = image.get_rect()

Man = pygame.image.load("images/Player/Guy.png")
ManRect = Man.get_rect(bottomright = [900,640])

pick = Pickaxe()

speedx = (-5)
speedy = (-3)
Pickspeed = [speedx, speedy]

#pygame.mouse.get_pos():


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pick.go()
            #MOUSEBUTTONDOWNget_pressed
    
    pick.update()       
    
    screen.blit(image, imgRect)
    screen.blit(Man.image, Man.rect)
    screen.blit(pick.image, pick.rect)
    pygame.display.flip()
    
   

