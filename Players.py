import TextureManager as tm
import pygame


# Main player class
class Players:
    # Constructor
    def __init__(self, title):
        self.size = 50
        self.playerX = 0
        self.playerY = 0
        self.playerX_change = 0
        self.playerY_change = 0
        self.texture = tm.Texture(title)
        self.texture = pygame.transform.scale(self.texture, (self.size, self.size))
        self.rect = self.texture.get_rect(topleft=(self.playerX, self.playerY))
        self.playerLeft = pygame.transform.rotate(self.texture, 90)
        self.playerRight = pygame.transform.rotate(self.texture, -90)
        self.playerUp = pygame.transform.rotate(self.texture, 0)
        self.playerDown = pygame.transform.rotate(self.texture, 180)
        self.playerUpLeft = pygame.transform.rotate(self.texture, 45)
        self.playerUpRight = pygame.transform.rotate(self.texture, -45)
        self.playerDownLeft = pygame.transform.rotate(self.texture, 125)
        self.playerDownRight = pygame.transform.rotate(self.texture, -125)

    # Rendering to the screen
    def Render(self, screen):
        screen.blit(self.texture, (self.playerX, self.playerY))

    def UpdateRect(self):
        self.rect = self.texture.get_rect(topleft=(self.playerX, self.playerY))

    # def UpdatePosition(self):
    #     self.rect = self.texture.get_rect(topleft=(self.playerX, self.playerY))

    def ChangeTex(self, tex):
        self.texture = tex
