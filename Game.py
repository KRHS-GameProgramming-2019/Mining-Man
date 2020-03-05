#----------------------------Setup Code---------------------------------
#Main game file
import pygame, sys, math, random
from Player import * 
from Screens import *
from Getters import *
from Settings import *
from options import *
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

pickaxe_sound = pygame.mixer.Sound('Sound/pickaxe/test.ogg')




    #------------------------Game Code----------------------------------




while True:
    #---------------------------Menu------------------------------------
    image = pygame.image.load("images/background/caveentrance.png")
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
                elif event.key == pygame.K_n:
                    screens = "night"
                    
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
        
    #--------------------------Night Mode-------------------------------
    image = pygame.image.load("images/background/black entrance.png")
    imgRect = image.get_rect()
    while screens == "night":
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
                # ~ if event.key ==pygame.K_SPACE:
                    # ~ for oreC in ores:
                        # ~ for ore in oreC:
                            # ~ ore.moveOver()
                    oreCollumn = []
                    for i in range(7):
                        oreCollumn += [Ore(None, [0, (6*80)-(i*80)])]
                    ores += [oreCollumn]
            
                elif event.key == pygame.K_i:
                    print ("--------------------")
                    for i in ores:
                        for j in i:
                            print (str(j) + "\t")
                        print ("\n")
                    print ("--------------------")
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
            oreCollumn = []
            for i in range(7):
                oreCollumn += [Ore(None, [0, i*80])]
            ores += [oreCollumn]
        
        pick.update()   
        
        deadBlocks = []
        deadBlockCols = []
        if pick.canHit:
            for col, oreC in enumerate(ores):
                for y, ore in enumerate(oreC):
                    if ore.pickCollide(pick):
                        deadBlocks += [ore]
                        deadBlockCols += [col]
                        kind = ore.kind
                        oreY = ore.rect.y
                        for block in oreC:
                            if block.rect.y < oreY:
                                print("Block:", str(block))
                                block.moveDown()
                        if col+1 < len(ores) and y < len(ores[col+1]):
                            print("col+1: ", col+1, y, "\t", len(ores), len(ores[col+1]))
                            if ores[col+1][y].kind == kind:
                                deadBlocks += [ores[col+1][y]]
                                deadBlockCols += [col+1]
                                for block in ores[col+1]:
                                    if block.rect.y < oreY:
                                        print("Block:", str(block))
                                        block.moveDown()
                        if col-1 > 0 and y < len(ores[col-1]):
                            print("col-1: ", col-1, y, "\t", len(ores), len(ores[col-1]))
                            if ores[col-1][y].kind == kind:
                                deadBlocks += [ores[col-1][y]]
                                deadBlockCols += [col-1]
                                for block in ores[col-1]:
                                    if block.rect.y < oreY:
                                        print("Block:", str(block))
                                        block.moveDown()
                        #only check above collison
                        
                        if y+1 < len(oreC) and ores[col][y+1].kind == kind:
                            deadBlocks += [ores[col][y+1]]
                            deadBlockCols += [col]
                            for block in oreC:
                                if block.rect.y < oreY:
                                    print("Block:", str(block))
                                    block.moveDown()
                        if y-1 > 0 and ores[col][y-1].kind == kind:
                            deadBlocks += [ores[col][y-1]]
                            deadBlockCols += [col]
                            for block in oreC:
                                if block.rect.y < oreY:
                                    print("Block:", str(block))
                                    block.moveDown()
                                    block.moveDown()
                                    
                        break;
                            
                        
        for i, block in enumerate(deadBlocks):
            print(block)
            if block in ores[deadBlockCols[i]]:
                ores[deadBlockCols[i]].remove(block)
                    
                
        screen.blit(image, imgRect)
        for oreC in ores:
            for ore in oreC:
                screen.blit(ore.image, ore.rect)
        screen.blit(guy.image, guy.rect)
        screen.blit(pick.image, pick.rect)
        pygame.display.flip()
        clock.tick(60)
    

