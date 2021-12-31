from Players import Players
import pygame


# Class to handle all the user players
class User(Players):
    # Constructor
    def __init__(self, title):
        super(User, self).__init__(title)

    # Rendering the player to the screen
    def Render(self, screen):
        super(User, self).Render(screen)

    # Updating the position of the user car
    def UpdatePosition(self):
        super(User, self).UpdatePosition()
        self.playerX += self.playerX_change
        if self.playerX <= 20:
            self.playerX = 20
        elif self.playerX >= 925:
            self.playerX = 925

        self.playerY += self.playerY_change
        if self.playerY <= 28:
            self.playerY = 28
        elif self.playerY >= 505:
            self.playerY = 505

    # def CollisionCheck(self, other):
    #     if self.rect.colliderect(other.rect):
    # check for collision between cars
