import TextureManager as tm
import pygame
import math

PI = 3.14159265358979323846


class Ball:
    def __init__(self):
        self.size = 25
        self.ballX = 1000 / 2 - self.size / 2
        self.ballY = 585 / 2 - self.size / 2
        self.ballX_change = 0
        self.ballY_change = 0
        self.ball_speed = 0.3
        self.texture = tm.Texture("Images/ball.png")
        self.texture = pygame.transform.scale(self.texture, (self.size, self.size))
        self.rect = self.texture.get_rect(topleft=(self.ballX, self.ballY))

        # Rendering to the screen

    def Render(self, screen):
        screen.blit(self.texture, (self.ballX, self.ballY))

    def CollisionCheck(self, other):
        if self.rect.colliderect(other.rect):
            if (other.playerX + other.size/2 + self.size) > self.ballX > (other.playerX - 5) and (other.playerY + 5) > self.ballY > (other.playerY - 5):
                self.ballX_change = self.ball_speed
                self.ballY_change = 0
            elif (other.playerX - self.size) < self.ballX < (other.playerX + 5) and (other.playerY + 5) > self.ballY > (other.playerY - 5):
                self.ballX_change = -self.ball_speed
                self.ballY_change = 0
            elif (other.playerY - self.size) < self.ballY < (other.playerY + 5) and (other.playerX + 5) > self.ballX > (other.playerX - 5):
                self.ballX_change = 0
                self.ballY_change = -self.ball_speed
            elif (other.playerY + other.size/2 + self.size) > self.ballY > (other.playerY - 5) and (other.playerX + 5) > self.ballX > (other.playerX - 5):
                self.ballX_change = 0
                self.ballY_change = self.ball_speed
            elif self.ballX > other.playerX and self.ballY > other.playerY:
                self.ballX_change = self.ball_speed
                self.ballY_change = self.ball_speed
            elif self.ballX > other.playerX and self.ballY < other.playerY:
                self.ballX_change = self.ball_speed
                self.ballY_change = -self.ball_speed
            elif self.ballX < other.playerX and self.ballY < other.playerY:
                self.ballX_change = -self.ball_speed
                self.ballY_change = -self.ball_speed
            elif self.ballX < other.playerX and self.ballY > other.playerY:
                self.ballX_change = -self.ball_speed
                self.ballY_change = self.ball_speed
        else:
            ballSlowness = 0.0004
            if self.ballX_change > 0:
                self.ballX_change -= ballSlowness
            if self.ballX_change < 0:
                self.ballX_change += ballSlowness
            if self.ballY_change > 0:
                self.ballY_change -= ballSlowness
            if self.ballY_change < 0:
                self.ballY_change += ballSlowness

    def UpdateRect(self):
        self.rect = self.texture.get_rect(topleft=(self.ballX, self.ballY))

    def UpdatePosition(self):
        self.ballX += self.ballX_change
        if self.ballX < 20:
            self.ballX = 20
        else:
            self.ballX_change = -self.ballX_change

        if self.ballX > 936:
            self.ballX = 936
        else:
            self.ballX_change = -self.ballX_change

        self.ballY += self.ballY_change
        if self.ballY < 28:
            self.ballY = 28
        else:
            self.ballY_change = -self.ballY_change
        if self.ballY > 521:
            self.ballY = 521
        else:
            self.ballY_change = -self.ballY_change
