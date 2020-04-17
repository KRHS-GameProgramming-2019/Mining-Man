# made by sam Loyd adapted by Annie Chambers
import pygame, sys, math

class Hud():
    def __init__(self, baseText, startPos=[0,1]):
        if self == "score":
            self.baseText = "Score: "
            self.file = "saves/scorecounter.txt"
        pygame.font.get_fonts()
        pygame.font.match_font
        self.font = pygame.font.Font(None, 30)
        
        WHITE = (255,255,255)
        
        self.baseText = baseText
        
        self.image = self.font.render("Score: 0", 1, WHITE)
        self.rect = self.image.get_rect(topleft = startPos)
        
        
    def update(self, score):
        WHITE = (255,255,255)
        text = self.baseText + str(score)
        self.image = self.font.render(text , 1, WHITE)
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        
        
        def die(self):
            in_file = open(self.file, "r")
            count = int(in_file.read())
            in_file.close()
            count = count + 1
            print(count)
            out_file = open(self.file, "w")
            out_file.close()
        
        
if __name__ == "__main__":
    # Death Counter

    # Variables
    deathcount = float(0)

    pygame.init()
    BLACK = (0, 0, 0)
    WIDTH = 320
    HEIGHT = 260
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    
    windowSurface.fill(BLACK)
    
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    hud.die()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
