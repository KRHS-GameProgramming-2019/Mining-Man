#Main game file
import pygame, sys, math, random
from Player import * 
from Screens import *
from Getters import *
from Settings import *
from  options import *
from practice import *
from Ore import *
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)
screens = "menu"

clock = pygame.time.Clock()

#Music code by caden
pygame.mixer.init()
songs = ["Sound/Music/spacecave.ogg"
]
songNum = 0
maxSongNum = len(songs)-1
pygame.mixer.music.load(songs[songNum])
pygame.mixer.music.set_volume(0.4)





while True:
    #---------------------------Menu------------------------------------
    image = pygame.image.load("images/TitleScreen/titlescreenbackground.png")
    imgRect = image.get_rect()
    pygame.mixer.init()
    pygame.mixer.music.load("Sound/Music/spacecave.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)
    
    
    
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
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
    image = pygame.image.load("images/TitleScreen/titlescreenbackground-options1.png")
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
                #elif pick.launched:  #return before hits spot
                #   pick.back()
        
        if oreTimer < oreTimerMax:
            oreTimer += 1
        else:
            oreTimer = 0
            for oreC in ores:
                for ore in oreC:
                    ore.moveOver()
            for i in range(7):
                oreCollumn = []
                oreCollumn += [Ore(None, [0, i*80])]
                ores += [oreCollumn]
        
        pick.update()   
        
        if pick.canHit:
            for oreC in ores:
                for ore in oreC:
                    if ore.pickCollide(pick):
                        oreC.remove(ore)
                    
                
        
        screen.blit(image, imgRect)
        for oreC in ores:
            for ore in oreC:
                screen.blit(ore.image, ore.rect)
        screen.blit(guy.image, guy.rect)
        screen.blit(pick.image, pick.rect)
        pygame.display.flip()
        clock.tick(60)
    

