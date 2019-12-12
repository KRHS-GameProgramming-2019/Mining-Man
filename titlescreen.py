#Screen that pops up when you open the game, has Play, Options, and Quit buttons

import Pickaxe, Ore, Game, Settings, Player, Screens, Getters, pygame

pygame.init()


def Miningman(debug=False):
    if debug:
        print("Debug Active")
    
    print(Screens.Titlescreen(debug))
    
    input("Press Any Key To Continue")
    
    done = False
    while not done:
        print(Screens.Titlescreen(debug))
        choice = Getters.getMenuOption(debug)
        
        
        if choice == "q":
            exit();
        elif choice == "Options":
            print(Options.Options(debug))
            input("Press Any Key To Continue")
            
        elif choice == "Play":
            print(Game.Game(debug))
            
        
Miningman()

