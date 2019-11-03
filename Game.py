import pygame
import random

from Interface import Interface
from Menu import Menu
from Rocket import Rocket
from Platform import Platform
from Config import *

SCORE = 100

pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()

if FULLSCREEN:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(SCREEN_SIZE)

run = True

all_sprites = pygame.sprite.Group()
rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 8))  # creating of the rocket
platform = Platform((WIDTH * 0.75, HEIGHT - 100))
all_sprites.add(rocket)
all_sprites.add(platform)

playersprite = pygame.sprite.RenderClear(rocket)
platfomrsprite = pygame.sprite.RenderClear(platform)

background = pygame.image.load(BACKGROUND_IMAGE_LEVEL_1)
background = pygame.transform.scale(background, SCREEN_SIZE)

sadElon = pygame.image.load(SAD_ELON).convert_alpha()
sadElon = pygame.transform.scale(sadElon, ELON_SIZE)

level = 1
interface = Interface(SCREEN_SIZE, screen)

items = [(WIDTH / 2 - 200, HEIGHT * 0.75, u"Game", GRAY, WHITE, 0),
         (WIDTH / 2 + 100, HEIGHT * 0.75, u"Quit", GRAY, WHITE, 1)]
game = Menu(screen, items)
game.menu()

move_left = True


def draw():
    playersprite.update()
    rocket.update()

    screen.blit(background, (0, 0))

    platfomrsprite.draw(screen)
    pygame.draw.rect(screen, BLACK, (platform.rect[0], platform.rect[1] + platform.rect.height / 4, 3, 3))
    playersprite.draw(screen)

    """ interface """
    Interface.render(interface, SCORE, 0, 0, "SCORE: ")
    Interface.render(interface, abs(round(rocket.move_direction[0], 2)), 0, 50, "HORIZONTAL SPEED: ")
    Interface.render(interface, abs(round(rocket.move_direction[1], 2)), 0, 100, "VERTICAL SPEED: ")
    Interface.render(interface, round(rocket.fuel), 0, 150, "FUEL: ")
    Interface.render(interface, level, WIDTH - 100, 0, "LEVEL: ")

    pygame.display.update()


def game_over():
    if (rocket.position[0] - rocket.rect.width / 2) < 0 \
            or (rocket.position[0] + rocket.rect.width / 2) > WIDTH \
            or (rocket.position[1] - rocket.rect.height / 2) < 0 \
            or (rocket.position[1] + rocket.rect.height / 2) > (HEIGHT - 100):
        screen.fill(BLACK)
        screen.blit(sadElon, (0, HEIGHT - ELON_SIZE[1]))
        font = pygame.font.SysFont(FONT, 40)
        for i in range(180):
            CLOCK.tick(GAME_FPS)
            screen.blit(font.render("You lose", False, RED), (WIDTH / 2, HEIGHT / 2))
            pygame.display.update()
        game.menu()


def game_win():
    if (((rocket.rect[1] + rocket.rect.height) > (platform.rect[1] + platform.rect.height / 4))
            and (rocket.position[0] > platform.position[0]
                 and rocket.position[0] + rocket.rect.width < platform.position[0] + platform.rect.width)
            and abs(rocket.move_direction[0]) < 0.1
            and abs(rocket.move_direction[1]) < 0.4):
        font = pygame.font.SysFont(FONT, 40)
        for i in range(180):
            CLOCK.tick(GAME_FPS)
            screen.blit(font.render("You won", False, GREEN), (WIDTH / 2, HEIGHT / 2))
            pygame.display.update()
        game.menu()


""" test platform moving behavior """
"""
 def move_platform():
    if move_left and platform.position[0] < WIDTH / 10:
        platform.rect = platform.position[0] - 0.01, platform.position[1]
    elif not move_left and platform.position[0] + platform.rect.width < WIDTH * 0.9:
        platform.rect = platform.position[0] + 0.01, platform.position[1]
    if random.randint(0, 1) == 0:
        return True
    else:
        return False
"""

while run:

    CLOCK.tick(GAME_FPS)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                rocket.angle_speed = -ANGLE

            if event.key == pygame.K_RIGHT:
                rocket.angle_speed = +ANGLE

            if event.key == pygame.K_UP:
                if rocket.fuel > 0:
                    rocket.gas = True

            if event.key == pygame.K_ESCAPE:
                game.menu()
                pygame.key.set_repeat(1, 1)
                pygame.mouse.set_visible(False)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                rocket.gas = False

            if event.key == pygame.K_RIGHT:
                rocket.angle_speed = 0

            if event.key == pygame.K_LEFT:
                rocket.angle_speed = 0

    # move_left = move_platform()
    game_over()
    game_win()
    draw()

pygame.quit()
