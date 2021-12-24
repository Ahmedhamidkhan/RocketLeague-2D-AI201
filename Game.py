import pygame
import User
import AI
import Background


# Main game class
class Game:
    # Constructor
    def __init__(self):
        self.running = True
        try:
            pygame.init()
        except:
            self.running = False

        self.background = Background.Background()
        self.player = User.User()
        self.ai = AI.AI()
        self.screen = pygame.display.set_mode((1000, 585))
        pygame.display.set_caption("Cars")
        self.icon = pygame.image.load('Images/sport-car.png')
        pygame.display.set_icon(self.icon)

    # Function to initialize variable values
    def Initialization(self):
        self.background.CreateBackgroundTexture()
        self.player.CreatePlayerTexture("Images/player1.png")
        self.ai.CreatePlayerTexture("Images/player2.png")

    # Returns the variable that tells if game is running or not
    def isRunning(self):
        return self.running

    # Function to handle all events
    def handleEvent(self):
        # Runs through all pygame events
        for event in pygame.event.get():
            # If the close button is pressed, game ends
            if event.type == pygame.QUIT:
                self.running = False

            # Players movement for now
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.playerX_change = -0.3
                if event.key == pygame.K_RIGHT:
                    self.player.playerX_change = 0.3
                if event.key == pygame.K_UP:
                    self.player.playerY_change = -0.3
                if event.key == pygame.K_DOWN:
                    self.player.playerY_change = 0.3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.playerY_change = 0

        # Updating players to new positions
        self.player.UpdatePosition()

    # Rendering everything to the screen
    def Render(self):
        self.background.Render(self.screen)
        self.player.Render(self.screen)
        self.ai.Render(self.screen)
        pygame.display.update()

    # Clean memory when program is closed
    def Clean(self):
        pygame.quit()

    # def GameOver(self):
