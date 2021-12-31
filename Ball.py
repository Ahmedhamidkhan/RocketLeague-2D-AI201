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
            rel = (other.playerY + (self.size / 2)) - (self.ballY + (self.size / 2))
            norm = rel / (self.size / 2)
            bounce = norm * (5 * PI / 12)
            self.ballX_change = self.ball_speed * math.cos(bounce)
            self.ballY_change = self.ball_speed * -(math.sin(bounce))
        else:
            if self.ballX_change > 0:
                self.ballX_change -= 0.0001
            elif self.ballX_change < 0:
                self.ballY_change += 0.0001
            if self.ballY_change > 0:
                self.ballY_change -= 0.0001
            elif self.ballY_change < 0:
                self.ballY_change += 0.0001

    def UpdatePosition(self):
        if self.ballX <= 20 or self.ballX >= 936:
            self.ballX_change = -self.ballX_change

        self.ballX += self.ballX_change

        if self.ballY <= 28 or self.ballY >= 521:
            self.ballY_change = -self.ballY_change

        self.ballY += self.ballX_change

        self.rect = self.texture.get_rect(topleft=(self.ballX, self.ballY))
