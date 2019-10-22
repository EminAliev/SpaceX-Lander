import pygame

WIDTH, HEIGHT = 800, 800
WINDOW_TITLE = "SPACE-X LENDER"
GAME_FPS = 60
SIZE = (WIDTH, HEIGHT)
SCORE = 100
GREEN = (120, 240, 120)
WHITE = (255, 255, 255)

pygame.init()

speed = [1, 1]

CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)

"""def gamePlay():
    rocket = pygame.Rect(WIDTH // 2), HEIGHT - 180, 60, 180)"""


def control(self, events):
    """
    Функция, отвещающая за обработку нажатия клавиш.
    """
    for event in events:
        if event.type == pygame.QUIT:
            return 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.y_speed = 1
            if event.key == pygame.K_UP:
                self.y_speed = 1
            if event.key == pygame.K_RIGHT:
                self.x_speed = 1
            if event.key == pygame.K_LEFT:
                self.x_speed = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_speed = -2
            if event.key == pygame.K_RIGHT:
                self.x_speed = 2
            if event.key == pygame.K_UP:
                self.y_speed = -2
            if event.key == pygame.K_DOWN:
                self.y_speed = 2
