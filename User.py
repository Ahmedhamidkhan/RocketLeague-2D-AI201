from Players import Players
import pygame


# Class to handle all the user players
class User(Players):
    # Constructor
    def __init__(self, title):
        super(User, self).__init__(title)
        self.playerX = 1000/3
        self.playerY = 585/2 - self.size/2
        self.texture = self.playerRight

    # Rendering the player to the screen
    def Render(self, screen):
        super(User, self).Render(screen)

    # Updating the position of the user car
    def UpdatePosition(self):
        newX = self.playerX + self.playerX_change
        if 20 <= newX <= 925:
            self.playerX = newX

        newY = self.playerY + self.playerY_change
        if 20 < newY < 505:
            self.playerY = newY


    # def CollisionCheck(self, other):
    #     if self.rect.colliderect(other.rect):
    # check for collision between cars
