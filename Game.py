import pygame
from Rocket import Rocket
from Config import *

WIDTH, HEIGHT = 1280, 720
WINDOW_TITLE = "SPACE-X LENDER"
GAME_FPS = 60
SIZE = (WIDTH, HEIGHT)
SCORE = 100
SPEED = 0.05

pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
run = True


all_sprites = pygame.sprite.Group()
# rocket = Rocket(WIDTH / 2, HEIGHT / 2, GREEN, SPEED)
rocket = Rocket(SPEED, (0, 0.01), (WIDTH / 2, HEIGHT / 2))
all_sprites.add(rocket)
platform = pygame.Surface((30, 1))
pygame.draw.line(platform, WHITE, (0, 0), (30, 0), 1)
playersprite = pygame.sprite.RenderPlain(rocket)
# platform.fill(WHITE)


def draw():
    playersprite.update()
    # rocket.move(screen)
    rocket.update()
    screen.fill(BLACK)
    playersprite.draw(screen)
    # screen.blit(rocket.image, (rocket.x, rocket.y))
    screen.blit(platform, (WIDTH / 2 - 15, HEIGHT - 5))
    # all_sprites.draw(screen)
    pygame.display.update()


while run:

    CLOCK.tick(GAME_FPS)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     rocket.y_speed_plus(-5)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # rocket.x_speed_plus(-1)
                rocket.angle_speed = -ANGLE
            if event.key == pygame.K_RIGHT:
                # rocket.x_speed_plus(1)
                rocket.angle_speed = +ANGLE
            if event.key == pygame.K_UP:
                rocket.gas = True

        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_DOWN:
            #     pass
            if event.key == pygame.K_UP:
                rocket.gas = False
            if event.key == pygame.K_RIGHT:
                rocket.angle_speed = 0
            if event.key == pygame.K_LEFT:
                rocket.angle_speed = 0
            # if event.key == pygame.K_DOWN:
            #     pass
    draw()

pygame.quit()
