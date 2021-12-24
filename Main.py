# Main file to run the program
import Game


# Creating game object
g = Game.Game()
# Initializing all required variable valules
g.Initialization()

# Main game loop
while g.isRunning():
    g.handleEvent()
    g.Render()

# After game closed, quits all libraries
g.Clean()
