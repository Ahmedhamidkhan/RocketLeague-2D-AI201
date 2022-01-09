import pygame
import User
import AI
import Background
import Ball
import Menu
import time


# Main game class
class Game:
    # Constructor
    def __init__(self):
        self.goal = [0, 0]
        self.running = True
        try:
            pygame.init()
        except:
            self.running = False

        self.runMenu = True

        self.background = Background.Background("Images/background.jpeg")
        self.player = User.User("Images/player1.png")
        self.ai = AI.AI("Images/player2.png")
        self.ball = Ball.Ball()
        self.menu = Menu.Menu()
        self.screen = pygame.display.set_mode((1000, 585))
        pygame.display.set_caption("Cars")
        self.icon = pygame.image.load('Images/sport-car.png')
        pygame.display.set_icon(self.icon)
        self.r = False
        self.l = False
        self.u = False
        self.d = False

    # Returns the variable that tells if game is running or not
    def isRunning(self):
        return self.running

    # Function to handle all events
    def handleEvent(self):

        self.player.UpdateRect()
        self.ai.UpdateRect()
        self.ball.UpdateRect()

        if self.runMenu:
            run = self.menu.mainMenu(self.screen)
            self.runMenu = False
            if run:
                self.running = False

        # Runs through all pygame events
        for event in pygame.event.get():
            # If the close button is pressed, game ends
            if event.type == pygame.QUIT:
                self.running = False

            # Players movement for now
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.runMenu = True
                if event.key == pygame.K_LEFT:
                    self.l = True
                    self.player.playerX_change -= self.player.player_speed
                if event.key == pygame.K_RIGHT:
                    self.r = True
                    self.player.playerX_change = self.player.player_speed
                if event.key == pygame.K_UP:
                    self.u = True
                    self.player.playerY_change = -self.player.player_speed
                if event.key == pygame.K_DOWN:
                    self.d = True
                    self.player.playerY_change = self.player.player_speed

            if self.r:
                self.player.ChangeTex(self.player.playerRight)
            if self.l:
                self.player.ChangeTex(self.player.playerLeft)
            if self.u:
                self.player.ChangeTex(self.player.playerUp)
            if self.d:
                self.player.ChangeTex(self.player.playerDown)

            if self.r and self.u:
                self.player.ChangeTex(self.player.playerUpRight)
            if self.r and self.d:
                self.player.ChangeTex(self.player.playerDownRight)
            if self.l and self.u:
                self.player.ChangeTex(self.player.playerUpLeft)
            if self.l and self.d:
                self.player.ChangeTex(self.player.playerDownLeft)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.l = False
                    self.player.playerX_change = 0
                if event.key == pygame.K_RIGHT:
                    self.r = False
                    self.player.playerX_change = 0
                if event.key == pygame.K_UP:
                    self.u = False
                    self.player.playerY_change = 0
                if event.key == pygame.K_DOWN:
                    self.d = False
                    self.player.playerY_change = 0

        self.ball.CollisionCheck(self.player)
        self.ball.UpdatePosition()

        self.ball.CollisionCheck(self.ai)
        self.ball.UpdatePosition()

        # Updating players to new positions
        self.player.UpdatePosition()
        self.ai.UpdatePosition(self.ball)

        goal_check = self.ball.isGoal()

        if goal_check == 1:
            self.goal[0] += 1
        elif goal_check == 2:
            self.goal[1] += 1

        # self.ball.CollisionCheck(self.ai)

    # Rendering everything to the screen
    def Render(self):
        self.background.Render(self.screen)
        self.player.Render(self.screen)
        self.ai.Render(self.screen)
        self.ball.Render(self.screen)
        pygame.display.update()

    # Clean memory when program is closed
    def Clean(self):
        pygame.quit()

    # def GameOver(self):
