from Players import Players


# Class to handle all the user players
class User(Players):
    # Constructor
    def __init__(self):
        super(User, self).__init__()

    # Function to create player texture
    def CreatePlayerTexture(self, title):
        super(User, self).CreatePlayerTexture(title)

    # Rendering the player to the screen
    def Render(self, screen):
        super(User, self).Render(screen)

    # Updating the position of the user car
    def UpdatePosition(self):
        self.playerX += self.playerX_change
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 936:
            self.playerX = 936

        self.playerY += self.playerY_change
        if self.playerY <= 0:
            self.playerY = 0
        elif self.playerY >= 521:
            self.playerY = 521
