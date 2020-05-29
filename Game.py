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
from Text import *
pygame.init()

size = [900, 640]
screen = pygame.display.set_mode(size)
screens = "menu"

counter = 1;
score = Hud("Score: ", [780,30])
kills = 0

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
    playButton=Button("test", [350,100])
    optionsButton=Button("test", [350, 300])
    exitButton=Button("test", [350, 500])
    nightButton=Button("test", [100,200])
    
    while screens == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                
                playButton.update(event.pos, event.buttons)
                optionsButton.update(event.pos, event.buttons)
                exitButton.update(event.pos, event.buttons)
                nightButton.update(event.pos, event.buttons)
           
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                playButton.click(event.pos)
                optionsButton.click(event.pos)
                exitButton.click(event.pos)
                nightButton.click(event.pos)
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if playButton.click(event.pos):
                    screens = "game"
                if optionsButton.click(event.pos):
                    screens = "options"
                if nightButton.click(event.pos):
                    screens = "night"
                if exitButton.click(event.pos):
                    sys.exit()
        
        screen.blit(image, imgRect)
        screen.blit(playButton.image, playButton.rect)
        screen.blit(optionsButton.image, optionsButton.rect)
        screen.blit(exitButton.image, exitButton.rect)
        screen.blit(nightButton.image, nightButton.rect)
        pygame.display.flip()

#-------------------------- Options-------------------------------------         
    image = pygame.image.load("images/TitleScreen/titlescreenbackground-options1.png")
    imgRect = image.get_rect()
    backButton=Button("test", [675,50]) 
    
    while screens == "options":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                backButton.update(event.pos, event.buttons)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                backButton.click(event.pos)
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if backButton.click(event.pos):
                    screens = "menu"
                
        screen.blit(image, imgRect)
        screen.blit(backButton.image, backButton.rect)
        pygame.display.flip()
        
    #--------------------------Game Selection-----------------------------
    image = pygame.image.load("images/TitleScreen/tempselection.png")
    imgRect = image.get_rect()
    resumeButton=Button("test", [350,100])
    optionsButton=Button("test", [350, 300])
    menuButton=Button("test", [350, 500])
    
    while screens == "select":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                
                resumeButton.update(event.pos, event.buttons)
                optionsButton.update(event.pos, event.buttons)
                menuButton.update(event.pos, event.buttons)
           
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                resumeButton.click(event.pos)
                optionsButton.click(event.pos)
                menuButton.click(event.pos)
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if resumeButton.click(event.pos):
                    screens = "game"
                if optionsButton.click(event.pos):
                    screens = "gameoptions"
                if menuButton.click(event.pos):
                    screens = "menu"
            
        screen.blit(image, imgRect)
        screen.blit(resumeButton.image, resumeButton.rect)
        screen.blit(optionsButton.image, optionsButton.rect)
        screen.blit(menuButton.image, menuButton.rect)
        pygame.display.flip()
                    
    #--------------------------Game Options-----------------------------
    image = pygame.image.load("images/TitleScreen/titlescreenbackground-options1.png")
    imgRect = image.get_rect()
    backButton=Button("test", [675,50]) 
    
    while screens == "gameoptions":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                backButton.update(event.pos, event.buttons)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                backButton.click(event.pos)
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if backButton.click(event.pos):
                    screens = "select"
         
        
        screen.blit(image, imgRect)
        screen.blit(backButton.image, backButton.rect)
        pygame.display.flip()
    #--------------------------Night Mode-------------------------------
    image = pygame.image.load("images/background/black entrance.png")
    imgRect = image.get_rect()
    playButton=Button("test", [350,100])
    optionsButton=Button("test", [350, 300])
    exitButton=Button("test", [350, 500])
    
    while screens == "night":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.MOUSEMOTION:
                
                playButton.update(event.pos, event.buttons)
                optionsButton.update(event.pos, event.buttons)
                exitButton.update(event.pos, event.buttons)
                
           
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                playButton.click(event.pos)
                optionsButton.click(event.pos)
                exitButton.click(event.pos)
                
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if playButton.click(event.pos):
                    screens = "game"
                if optionsButton.click(event.pos):
                    screens = "options"
                if exitButton.click(event.pos):
                    sys.exit()
                
        screen.blit(image, imgRect)
        screen.blit(playButton.image, playButton.rect)
        screen.blit(optionsButton.image, optionsButton.rect)
        screen.blit(exitButton.image, exitButton.rect)
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
            score.update(kills)
        #-------End Auto Ores----------------#
   
        pick.update()
        
        def rareness(kind = 0):
            kind = ore.kind
            if kind == "coal":
                rare = 2
            elif kind == "iron":
                rare = 3
            elif kind == "ruby":
                rare = 4
            elif kind == "diamond":
                rare = 7
            elif kind == "amethyst":
                rare = 5
            elif kind == "emerald":
                rare = 6
            elif kind == "rainbow":
                rare = 8
            elif kind == "dirt":
                rare = 1
            elif kind == "dead":
                rare = 0
            elif kind == None :
                rare = 0
            print("rareness: ")
            print(rare)
        
        if pick.canHit:
            cluster.pickCollide(pick)
            rareness()
            kills +=((len(cluster.vanes)))
            
        for oreCollumn in cluster.ores:
            if len(oreCollumn) > 10:
                screens == "gameover"
                print("end of game")
            
        
        
        score.update(kills)
                       
                        
        cluster.update()
        # ~ cluster.endgame()
                    
                
        
        screen.blit(image, imgRect)
        for oreC in cluster.ores:
            for ore in oreC:
                screen.blit(ore.image, ore.rect)
        screen.blit(guy.image, guy.rect)
        screen.blit(pick.image, pick.rect)
        screen.blit(score.image, score.rect)
        pygame.display.flip()
        clock.tick(60)
    

