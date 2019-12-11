import pygame, sys, math, random
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)



image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
imgRect = image.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
    screen.blit(image, imgRect)
    pygame.display.flip()

