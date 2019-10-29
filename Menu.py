import sys

import pygame

from Game import screen


class Menu:
    def __init__(self, items=[400, 350, u'Item', (250, 250, 30), (250, 30, 250)]):
        self.items = items

    def render(self, font_type, font, num_item):
        for i in self.items:
            if num_item == i[5]:
                font_type.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                font_type.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        run = True
        font_menu = pygame.font.Font("/fonts/BOD_I.TTF", 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        item = 0
        while run:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.items:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    item = i[5]
            self.render(screen, font_menu, item)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if item > 0:
                            item -= 1
                    if event.key == pygame.K_DOWN:
                        if item < len(self.items) - 1:
                            item += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if item == 0:
                        run = False
                    elif item == 1:
                        sys.exit()

            screen.blit(screen, 0, 0)  
            pygame.display.flip()
