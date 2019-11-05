import sys

from Config import FONT, WHITE, FILE_SCORE
from Menu import Menu
import pygame


class Form(Menu):
    def show_menu_window(self):
        font = pygame.font.Font(FONT, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(550, 200, 140, 32)
        color = pygame.Color('lightskyblue3')
        active = True
        text = ''
        run = True
        font_menu = pygame.font.Font(FONT, 50)
        item = 0

        while run:
            self.screen.blit(self.image, (0, 0))

            mp = pygame.mouse.get_pos()
            for i in self.items:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    item = i[5]
            self.render(self.screen, font_menu, item)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if item == 0:
                        run = False
                    elif item == 1:
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
                    if active:
                        if event.key == pygame.K_RETURN:
                            with open('score.txt', 'a') as file:
                                file.write(text + "\n")
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            txt_surface = font.render(text, True, WHITE)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.screen, color, input_box, 2)
            txt_name = font.render("NAME: ", True, WHITE)
            self.screen.blit(txt_name, (440, 205))

            pygame.display.flip()
            clock.tick(30)
