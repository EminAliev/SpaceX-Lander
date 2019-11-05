import pygame

from Config import BLUE, FONT_SIZE


class Interface:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    def render(self, param, x, y, text):
        text_font = pygame.font.Font(None, FONT_SIZE)
        text_image = text_font.render(text + str(param), True, BLUE)

        self.screen.blit(text_image, (x, y))

        # pygame.display.update()
