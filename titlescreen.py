import Pickaxe, Ore, Player, Game

def MiningMan(debug=False):
    if debug:
        print("Debug Active")
    
    print(Screens.titleScreen(debug))
    
    input("Press Any Key To Continue")
    
    done = False
    while not done:
        print(Screens.mainMenu(debug))
        choice = Getters.getMenuOption(debug)
        
        if choice == "esc":
            exit();
        elif choice == "Play":
            print(Game.Game(debug))
            
        elif choice == "Options":
            print(Options.Options(debug))
           
            
        
MiningMan()


