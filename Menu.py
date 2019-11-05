import sys

import pygame
from Config import FONT, MENU_BACKGROUND_IMAGE, SCREEN_SIZE, BIG_FONT_SIZE

""" Menu class """


class Menu:
    def __init__(self, screen, items):
        self.items = items
        self.screen = screen
        self.image = pygame.image.load(MENU_BACKGROUND_IMAGE)
        self.image = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.font_menu = pygame.font.Font(FONT, BIG_FONT_SIZE)

    """ Draws items of the menu """
    def render(self, surface, font, num_item):
        for i in self.items:
            if num_item == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    """ Shows menu and processes events with input devices """
    def show_menu_window(self):
        run = True

        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        item = 0

        while run:
            self.screen.blit(self.image, (0, 0))

            mp = pygame.mouse.get_pos()
            for i in self.items:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    item = i[5]
            self.render(self.screen, self.font_menu, item)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_LEFT:
                        if item > 0:
                            item -= 1
                    if event.key == pygame.K_RIGHT:
                        if item < len(self.items) - 1:
                            item += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if item == 0:
                        run = False
                    elif item == 1:
                        sys.exit()

            pygame.display.flip()
