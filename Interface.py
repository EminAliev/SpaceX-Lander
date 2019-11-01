import pygame

from Config import BLUE, WHITE


class Interface:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def render(self, param, x, y, text):
        text_font = pygame.font.Font(None, 60)
        text_image = text_font.render(text + str(param), True, WHITE)

        self.screen.blit(text_image, (x, y))

        pygame.display.update()
