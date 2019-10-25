import pygame
from Rocket import Rocket

WIDTH, HEIGHT = 1280, 720
WINDOW_TITLE = "SPACE-X LENDER"
GAME_FPS = 60
SIZE = (WIDTH, HEIGHT)
SCORE = 100
GREEN = (120, 240, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

rocket = Rocket(WIDTH/2, HEIGHT/2, GREEN, [0, 1])

pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
run = True

while run:

    CLOCK.tick(GAME_FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     rocket.y_speed_plus(-5)

        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_DOWN:
            #     pass
            if event.key == pygame.K_UP:
                rocket.y_speed_plus(3)
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_LEFT:
                pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.x_speed_plus(-1)
            if event.key == pygame.K_RIGHT:
                rocket.x_speed_plus(1)
            if event.key == pygame.K_UP:
                rocket.y_speed_plus(-3)
            # if event.key == pygame.K_DOWN:
            #     pass

    rocket.move(screen)
    screen.fill(BLACK)
    rocket.draw(screen)
    pygame.display.update()

pygame.quit()





