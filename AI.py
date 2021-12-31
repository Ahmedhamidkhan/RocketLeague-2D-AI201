from Players import Players


# Ai player class
class AI(Players):
    # Constructor
    def __init__(self, title):
        super(AI, self).__init__(title)

    # Rendering the Ai to the screen
    def Render(self, screen):
        super(AI, self).Render(screen)

    # Will be used to control the movement of the AI players
    # def UpdatePosition(self, ball):
