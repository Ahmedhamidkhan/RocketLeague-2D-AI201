import TextureManager as tm


# Class to handle the background
class Background:
    # Constructor
    def __init__(self):
        self.texture = tm.Texture("Images/background.jpeg")

    # Function to render the background
    def Render(self, screen):
        screen.blit(self.texture, (0, 0))
