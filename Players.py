import TextureManager as tm


# Main player class
class Players:
    # Constructor
    def __init__(self):
        self.playerX = 0
        self.playerY = 0
        self.playerX_change = 0
        self.playerY_change = 0
        self.texture = None

    # Creating the textures
    def CreatePlayerTexture(self, title):
        self.texture = tm.Texture(title)

    # Rendering to the screen
    def Render(self, screen):
        screen.blit(self.texture, (self.playerX, self.playerY))



