from Players import Players


# Ai player class
class AI(Players):
    # Constructor
    def __init__(self):
        super(AI, self).__init__()

    # Creates the texture for all the AI players
    def CreatePlayerTexture(self, title):
        super(AI, self).CreatePlayerTexture(title)

    # Rendering the Ai to the screen
    def Render(self, screen):
        super(AI, self).Render(screen)

    # Will be used to control the movement of the AI players
    # def UpdatePosition(self):
        # The AI part will go here
