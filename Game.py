#Main game file
import pygame, sys, math, random
from Player import * 
from Screens import *
from Getters import *
from Settings import *
from options import *
from practice import *
from Button import *
from Ore import *
from Cluster import *
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

pickaxe_sound = pygame.mixer.Sound('Sound/pickaxe/test.ogg')



#----------------------------Game Code----------------------------------




while True:
    #---------------------------Menu------------------------------------
    image = pygame.image.load("images/background/caveentrancea.png")
    imgRect = image.get_rect()
    pygame.mixer.init()
    pygame.mixer.music.load("Sound/Music/spacecave.ogg")
    pygame.mixer.music.play(loops=-1, start=0.0)
    playButton=Button("test", [100,100])
    optionsButton=Button("test", [100, 300])
    
    
    
    
    
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                playButton.update(event.pos, event.buttons)
                optionsButton.update(event.pos, event.buttons)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                playButton.click(event.pos)
                optionsButton.click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if playButton.click(event.pos):
                    screens = "game"
                if optionsButton.click(event.pos):
                    screens = "options"
            
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
                elif event.key == pygame.K_o:
                    screens = "options"
                elif event.key == pygame.K_ESCAPE:
                    sys.exit();
                elif event.key == pygame.K_u:
                    screens = "unicorn"
                elif event.key == pygame.K_n:
                    screens = "night"
                    
                    
        screen.blit(image, imgRect)
        screen.blit(playButton.image, playButton.rect)
        screen.blit(optionsButton.image, optionsButton.rect)
        pygame.display.flip()
    #--------------------------Unicorn----------------------------------
    # ~ image = pygame.image.load("images/TitleScreen/f.png")
    # ~ imgRect = image.get_rect()
    # ~ while screens == "unicorn":
        # ~ for event in pygame.event.get():
            # ~ if event.type == pygame.QUIT:
                # ~ sys.exit();
            # ~ elif event.type == pygame.KEYDOWN:
                # ~ if event.key == pygame.K_RETURN:
                    # ~ screens = "menu"
                # ~ elif event.key == pygame.K_ESCAPE:
                    # ~ sys.exit();
                    
        # ~ screen.blit(image, imgRect)
        # ~ pygame.display.flip()  
    #--------------------------Options----------------------------------             
    image = pygame.image.load("images/TitleScreen/titlescreenbackground-options1.png")
    imgRect = image.get_rect()
    while screens == "options":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    screens = "menu"
                elif event.key == pygame.K_ESCAPE:
                    screens = "menu"
        
        screen.blit(image, imgRect)
        pygame.display.flip()
    #--------------------------Game Selection-----------------------------
    image = pygame.image.load("images/TitleScreen/tempselection.png")
    imgRect = image.get_rect()
    while screens == "select":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    screens = "gameoptions"
                elif event.key == pygame.K_ESCAPE:
                    screens = "game"
                elif event.key == pygame.K_RETURN:
                    screens = "menu"
        screen.blit(image, imgRect)
        pygame.display.flip()
                    
    #--------------------------Game Options-----------------------------
    image = pygame.image.load("images/TitleScreen/titlescreenbackground-options1.png")
    imgRect = image.get_rect()
    while screens == "gameoptions":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    screens = "select"
                elif event.key == pygame.K_ESCAPE:
                    screens = "select"
                elif event.key == pygame.K_RETURN:
                    screens = "select"
         
        
        screen.blit(image, imgRect)
        pygame.display.flip()
    #--------------------------Night Mode-------------------------------
    image = pygame.image.load("images/background/black entrance.png")
    imgRect = image.get_rect()
    while screens == "night":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
                elif event.key == pygame.K_ESCAPE:
                    screens = "menu"
                elif event.key == pygame.K_o:
                    screens = "options"
                
        screen.blit(image, imgRect)
        pygame.display.flip()
        
    #---------------------------end game----------------------------------#
    image = pygame.image.load("images/background/gameover.png")
    imgRect = image.get_rect()
    
	    
    while screens == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screens = "game"
                elif event.key == pygame.K_ESCAPE:
                    screens = "menu"
        screen.blit(image, imgRect)
        pygame.display.flip()
        
        
        
    #---------------------------Game------------------------------------
    image = pygame.image.load("images/TitleScreen/tempbackground.png")
    imgRect = image.get_rect()
    pick = Pickaxe()
    guy = Guy()
    cluster = Cluster()
    oreTimer = 0              
    oreTimerMax = 3*60 # 3 seconds
    while screens == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screens = "select"
                
                # ~ if event.key ==pygame.K_SPACE:
                    # ~ for oreC in ores:
                        # ~ for ore in oreC:
                            # ~ ore.moveOver()
   
                # ~ #------Manual Ores----------#
                # ~ if event.key ==pygame.K_SPACE:
                    # ~ cluster.addCol()
                # ~ #-------End Manual Ores----------------#

            
                elif event.key == pygame.K_i:
                    print(str(cluster))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not pick.launched:
                    pick.go(event.pos)
                
                            
                #elif pick.launched:  #return before hits spot
                #   pick.back()
        
        #----------Auto Ores----------------#
        if oreTimer < oreTimerMax:
            oreTimer += 1
        else:
            oreTimer = 0
            cluster.addCol()
        #-------End Auto Ores----------------#
 
        pick.update()
        
        if pick.canHit:
            cluster.pickCollide(pick)
                       
                        
        cluster.update()
        # ~ cluster.endgame()
                    
                
        
        screen.blit(image, imgRect)
        for oreC in cluster.ores:
            for ore in oreC:
                screen.blit(ore.image, ore.rect)
        screen.blit(guy.image, guy.rect)
        screen.blit(pick.image, pick.rect)
        pygame.display.flip()
        clock.tick(60)
    

