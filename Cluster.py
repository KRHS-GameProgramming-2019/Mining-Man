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
        currKind = None
        
        #if len(self.ores) >= 1:             #first row
        for oreC in self.ores:
            vane = []
            for ore in oreC:
                if not currKind:            #start of column
                    currKind = ore.kind
                    vane += [ore]
                    print("starting " + currKind)
                elif ore.kind == currKind:  #same block below last block
                    vane += [ore]
                    print("Adding " + currKind)
                else:                       #different block below last block
                    self.vanes += [vane]         
                    vane = [ore]
                    currKind = ore.kind
                    print("Starting new " + currKind)
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
        if self.killOres():
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
                    
                    
                    
                    
    
    


