#Ore blocks file, add different ones (color, texture)

import math, pygame, random
from Ore import *


class Cluster():
    def __init__(self):
        self.ores = []
        self.oreTimer = 0
        self.oreTimerMax = 60*3
        
    def addCol(self):
        for oreC in self.ores:
            for ore in oreC:
                ore.moveOver()
        oreCollumn = []
        for i in range(7):
            oreCollumn += [Ore(None, [0, (6*80)-(i*80)])]
        self.ores += [oreCollumn]
        
    def __str__(self):
        out = "--------------------"
        for i in self.ores:
            for j in i:
                out += str(j) + "\n"
            out += "\n"
        out += "--------------------"
        return out
        
        
    def moveDown(self):     
        self.rect = self.rect.move([0,80])
        
    def pickCollide(self, other):
        for oreC in self.ores:
            for ore in oreC:
                ore.pickCollide(other)
                
    def update(self):
        self.killOres()
        
    def killOres(self):
        for oreC in self.ores:
            for ore in oreC:
                if not ore.living:
                    oreC.remove(ore)
    
    


