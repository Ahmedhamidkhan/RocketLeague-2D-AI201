import TextureManager as tm



class Ball:
    def __init__(self):
        self.ballX = 0
        self.ballY = 0
        self.ballX_change = 0
        self.ballY_change = 0
        self.texture = None

        # Rendering to the screen
    def Render(self, screen):
        screen.blit(self.texture, (self.ballX, self.ballY))

    def CreateBallTexture(self, title):
        self.texture = tm.Texture(title)