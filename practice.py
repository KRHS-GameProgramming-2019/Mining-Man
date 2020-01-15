import pygame, sys, math, random
from Pickaxe import *
from Player import *
from Game import *
from Ore import *
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)


image = pygame.image.load("images/TitleScreen/tempbackground.png")
imgRect = image.get_rect()




pick = Pickaxe()
Guy = Guy()


while True:
    for event in pygame.event.get():
        imgRect = image.get_rect()
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not pick.launched:
                pick.go(event.pos)
                print(event.pos)
            #elif pick.launched:  #return before hits spot
            #    pick.back()
        
    
    
    # ~ for ball in balls:
            # ~ if balls[-1].ballCollide(ball):
                # ~ balls.remove(balls[-1])
                # ~ break
            
     # ~ for hittingBall in balls:
        # ~ for hitBall in balls:
            # ~ if hittingBall.ballCollide(hitBall):
                # ~ if hittingBall.kind == "player":
                    # ~ balls.remove(hitBall)
                    # ~ kills += 1
        # ~ for wall in walls:
            # ~ hittingBall.wallTileCollide(wall)
    
    
    
    
    
    pick.update()   
    
    screen.blit(image, imgRect)
    screen.blit(Guy.image, Guy.rect)
    screen.blit(pick.image, pick.rect)
    pygame.display.flip()
    
   

