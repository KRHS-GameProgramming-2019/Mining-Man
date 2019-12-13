import pygame, sys, math, random
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)



image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
imgRect = image.get_rect()

Man = pygame.image.load("images/Player/Guy.png")
ManRect = Man.get_rect(bottomright = [900,640])

Pick = pygame.image.load("images/Pickaxe/pickaxe.png")
PickRect = Pick.get_rect(bottomright = [860, 585])

speedx = (-5)
speedy = (-3)
Pickspeed = [speedx, speedy]




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
    screen.blit(image, imgRect)
    screen.blit(Man, ManRect)
    screen.blit(Pick, PickRect)
    pygame.display.flip()
    
    PickRect = PickRect.move(Pickspeed)
    
    

