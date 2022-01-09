import TextureManager as tm


# Class to handle the background
class Background:
    # Constructor
    def __init__(self, image):
        self.texture = tm.Texture(image)

    # Function to render the background
    def Render(self, screen):
        screen.blit(self.texture, (0, 0))
