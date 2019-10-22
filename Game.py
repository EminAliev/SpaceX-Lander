import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
WINDOW_TITLE = "SPACE-X LENDER"
GAME_FPS = 60
SIZE = (WIDTH, HEIGHT)
SCORE = 100
green = 120, 240, 120
white = 255, 255, 255

speed = [1, 1]

CLOCK = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Emin rulit', True, white, None)
textRect = text.get_rect()
textRect.center = (WIDTH//2, HEIGHT//2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    textRect = textRect.move(speed)
    textRect = textRect
    if textRect.left < 0 or textRect.right > WIDTH:
        speed[0] = -speed[0]
    if textRect.top < 0 or textRect.bottom > HEIGHT:
        speed[1] = -speed[1]

    screen.fill(green)
    screen.blit(text, textRect)
    pygame.display.flip()
