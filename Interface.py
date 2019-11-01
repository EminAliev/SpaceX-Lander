import pygame

from Config import BLUE, WHITE


class Interface:
    def __init__(self, size, screen):
        self.size = size
        self.screen = screen

    # @staticmethod
    def render(self):
        clock = pygame.time.Clock()
        frame_count = 0
        text_font = pygame.font.Font(None, 60)
        text_image = text_font.render(str(frame_count), True, WHITE)
        text_width = text_image.get_width()

        text_x = self.size[0] - text_width
        text_y = 0

        self.screen.fill(BLUE)
        self.screen.blit(text_image, (text_x, text_y))

        pygame.display.update()
        clock.tick_busy_loop(60)

        frame_count += 1
