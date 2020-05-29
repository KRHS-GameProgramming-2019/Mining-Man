#Ore blocks file, add different ones (color, texture)

import math, pygame, random
from Ore import *


class Cluster():
    def __init__(self):
        self.ores = []
        self.oreTimer = 0
        self.oreTimerMax = 60*3
        self.vanes = []
        
    def addCol(self):
        for oreC in self.ores:
            for ore in oreC:
                ore.moveOver()
        oreCollumn = []
        for i in range(7):
            oreCollumn += [Ore(None, [0, (6*80)-(i*80)])]
        self.ores += [oreCollumn]
        self.findVanes()
       
    def findVanes(self):
        self.vanes=[]
        
        #if len(self.ores) >= 1:             #first row
        for colNum, oreC in enumerate(self.ores):
            vane = []
            # ~ if colNum >  12 :
                # ~ screens == "gameover"
            currKind = None
            for oreNum, ore in enumerate(oreC):
                if not currKind:            #start of column
                    # ~ print("Col Num: ", colNum)
                    if colNum > 0 and oreNum < len(self.ores[colNum-1]):
                        if self.ores[colNum-1][oreNum].kind == ore.kind:
                            self.ores[colNum-1][oreNum].vane += [ore]
                            ore.vane = self.ores[colNum-1][oreNum].vane
                            vane = ore.vane
                            currKind = ore.kind
                            # ~ print("adding " + currKind + " to old vane")
                        else:
                            currKind = ore.kind
                            vane += [ore]
                            ore.vane = vane
                            # ~ print("starting " + currKind)
                    else:
                        currKind = ore.kind
                        vane += [ore]
                        ore.vane = vane
                        # ~ print("starting " + currKind)
                elif ore.kind == currKind:  #same block above last block
                    if colNum > 0 and oreNum < len(self.ores[colNum-1]):
                        if self.ores[colNum-1][oreNum].kind == ore.kind:
                            vane += [ore]
                            self.ores[colNum-1][oreNum].vane += vane
                            ore.vane = self.ores[colNum-1][oreNum].vane
                            vane = ore.vane
                        else: 
                            vane += [ore]
                            ore.vane = vane
                    else:
                        vane += [ore]
                        ore.vane = vane
                    # ~ print("Adding " + currKind)
                else:                       #different block below last block
                    if vane not in self.vanes: 
                        self.vanes += [vane] 
                    vane = []    
                    if colNum > 0 and oreNum < len(self.ores[colNum-1]):
                        if self.ores[colNum-1][oreNum].kind == ore.kind:
                            self.ores[colNum-1][oreNum].vane += [ore]
                            ore.vane = self.ores[colNum-1][oreNum].vane
                            vane = ore.vane
                            currKind = ore.kind
                            # ~ print("adding " + currKind + " to old vane")
                        else:
                            currKind = ore.kind
                            vane += [ore]
                            ore.vane = vane
                            # ~ print("starting new " + currKind)
                    else:
                        currKind = ore.kind
                        vane += [ore]
                        ore.vane = vane
                        # ~ print("starting new " + currKind)
            if vane not in self.vanes: 
                self.vanes += [vane]
        
        
    def __str__(self):
        out = "--------------------\n"
        for i in self.ores:
            for j in i:
                out += str(j) + "\n"
            out += "\n"
        out += ">>>>>>\n"
        for vane in self.vanes:
            if len(vane) > 0:
                out += vane[0].kind + " ore, size: " + str(len(vane)) + "\n"
        out += "--------------------\n\n"
        return out
        
        
    def pickCollide(self, other):
        for oreC in self.ores:                  #look through ore columns
            for ore in oreC:                    #look through ores in column
                if ore.pickCollide(other):      #if pick hit one
                    for vane in self.vanes:     #look through vanes to see what vane that ore is in
                        if ore in vane:         #in that vane
                            for vaneOre in vane:#kill all ores in that vane
                                vaneOre.kill()
                
    def update(self):
        didKill = self.killOres()
        for colNum, oreC in enumerate(self.ores):
            if colNum > 0 and len(oreC) == 0:
                colCount = colNum-1
                print (colNum, colCount)
                while colCount >= 0:
                    for ore in self.ores[colCount]:
                        ore.moveBack()
                    colCount -=1
                self.ores.remove(oreC)
                print("Moving Back")
            elif len(oreC) == 0:
                self.ores.remove(oreC)
                print("Removing Last ")
        if didKill:
            self.findVanes()
            
                
                
        # ~ y = 0
        # ~ for rowNum, oreC in enumerate(self.ores):
            # ~ for oreNum, ore in enumerate(oreC):
        
                
            
        
                 
                
        
    def killOres(self):
        didKill = False
        for rowNum, oreC in enumerate(self.ores):
            for oreNum, ore in enumerate(oreC):
                if not ore.living:              #found dead ore
                    print("removing: " + str(ore))
                    oreC.remove(ore)
                    didKill = True
                    for i in range(oreNum, len(oreC)):
                        oreC[i].moveDown()
        return didKill
	
	
    # ~ def endgame (self):   
        # ~ for colNum, oreC in enumerate(self.ores):
            # ~ if colNum > 2:
                 # ~ screens == endgame
		
                    
                    
                    
                    
    
    


