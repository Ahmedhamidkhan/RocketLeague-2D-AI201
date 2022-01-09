# Main file to run the program
import Game


# Creating game object
g = Game.Game()

# Main game loop
while g.isRunning():
    g.handleEvent()
    g.Render()

# After game closed, quits all libraries
g.Clean()
