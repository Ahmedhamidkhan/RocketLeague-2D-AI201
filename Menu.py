# Main file to run the program
import Background
import pygame


class Menu:
    def __init__(self):
        self.background = Background.Background("Images/menu.jpg")
        self.background.texture = pygame.transform.scale(self.background.texture, (1000, 585))
        self.font = pygame.font.SysFont(None, 20)
        self.click = False
        self.mainClock = pygame.time.Clock()

    def drawText(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def mainMenu(self, screen):
        while True:
            self.background.Render(screen)
            # self.draw_text('ROCKET LEAGUE', self.font, (255, 255, 255), screen, 450, 20)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(370, 420, 200, 50)
            pygame.draw.rect(screen, (0, 0, 255), button_1)
            self.drawText('PLAY', self.font, (255, 255, 255), screen, 455, 435)

            if button_1.collidepoint((mx, my)):
                if self.click:
                    return False

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)
