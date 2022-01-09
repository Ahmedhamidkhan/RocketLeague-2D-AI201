from Players import Players


# Ai player class
class AI(Players):
    # Constructor
    def __init__(self, title):
        super(AI, self).__init__(title)
        self.playerX = 615
        self.playerY = 585 / 2 - self.size / 2
        self.texture = self.playerLeft

    # Rendering the Ai to the screen
    def Render(self, screen):
        super(AI, self).Render(screen)

    # Will be used to control the movement of the AI players
    def UpdatePosition(self, ball):
        playerX = 2
        # if (ball.ballX + ball.size/2) > self.playerX:
        #     self.playerX += self.player_speed
        # else:
        #     self.playerX -= self.player_speed
        #
        # if (ball.ballY + ball.size/2) > (self.playerY + self.size/2):
        #     self.playerY += self.player_speed
        # else:
        #     self.playerY -= self.player_speed

