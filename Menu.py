# Main file to run the program
import sys

import Background
import pygame


class Menu:
    def __init__(self):
        self.mainClock = pygame.time.Clock()

    def drawText(self, text, surface, x, y, size, color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def mainMenu(self, screen):
        click = False
        background = Background.Background("Images/menu.jpg")
        background.texture = pygame.transform.scale(background.texture, (1000, 585))
        while True:
            background.Render(screen)
            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(370, 420, 200, 50)
            button_2 = pygame.Rect(370, 500, 200, 50)
            pygame.draw.rect(screen, (0, 0, 255), button_1)
            pygame.draw.rect(screen, (0, 0, 255), button_2)
            self.drawText('PLAY', screen, 455, 435, 20)
            self.drawText('EXIT', screen, 455, 515, 20)
            if button_1.collidepoint((mx, my)):
                if click:
                    return False
            if button_2.collidepoint((mx, my)):
                if click:
                    return True
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def pauseMenu(self, screen):
        click = False
        background = Background.Background("Images/menu.jpg")
        background.texture = pygame.transform.scale(background.texture, (1000, 585))
        while True:
            background.Render(screen)
            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(370, 420, 200, 50)
            button_2 = pygame.Rect(370, 500, 200, 50)
            pygame.draw.rect(screen, (0, 0, 255), button_1)
            pygame.draw.rect(screen, (0, 0, 255), button_2)
            self.drawText('RESUME', screen, 452, 435, 20)
            self.drawText('EXIT', screen, 455, 515, 20)
            if button_1.collidepoint((mx, my)):
                if click:
                    return False
            if button_2.collidepoint((mx, my)):
                if click:
                    return True
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def endMenu(self, screen, win):
        click = False
        background = Background.Background("Images/end.jpg")
        background.texture = pygame.transform.scale(background.texture, (1000, 585))
        while True:
            background.Render(screen)
            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(370, 420, 200, 50)
            button_2 = pygame.Rect(370, 500, 200, 50)
            pygame.draw.rect(screen, (0, 0, 255), button_1)
            pygame.draw.rect(screen, (0, 0, 255), button_2)
            self.drawText(win+" Has Won", screen, 200, 250, 150, color=(255, 80, 0))
            self.drawText('RESTART', screen, 450, 435, 20)
            self.drawText('EXIT', screen, 455, 515, 20)
            if button_1.collidepoint((mx, my)):
                if click:
                    return False
            if button_2.collidepoint((mx, my)):
                if click:
                    return True
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.mainClock.tick(60)
