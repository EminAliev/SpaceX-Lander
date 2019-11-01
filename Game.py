import pygame
import time
from Menu import Menu
from Rocket import Rocket
from Config import *

WIDTH, HEIGHT = 1280, 720

SIZE = (WIDTH, HEIGHT)
SCORE = 100

pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
run = True

all_sprites = pygame.sprite.Group()
rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 2))
# rocket = Rocket(SPEED, GRAVITY_VECTOR, (0, 0))
all_sprites.add(rocket)
platform = pygame.Surface((60, 6))
pygame.draw.rect(platform, WHITE, (0, 0), 1)
playersprite = pygame.sprite.RenderPlain(rocket)


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


items = [(WIDTH / 2 - 200, HEIGHT / 2, u"Game", GREEN, YELLOW, 0),
         (WIDTH / 2 + 100, HEIGHT / 2, u"Quit", GREEN, YELLOW, 1)]
game = Menu(screen, items)
game.menu()


def game_over(rocket):
    if (rocket.position[0] - rocket.rect.width / 2) < 0 \
            or (rocket.position[0] + rocket.rect.width / 2) > WIDTH \
            or (rocket.position[1] - rocket.rect.height / 2) < 0 \
            or (rocket.position[1] + rocket.rect.height / 2) > HEIGHT:
        screen.fill(BLACK)
        font = pygame.font.SysFont(FONT, 40)
        screen.blit(font.render("You lose", False, RED), (WIDTH/2, HEIGHT/2))
        pygame.display.update()
        time.sleep(3)
        game.menu()
        return False
    else:
        return True


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

    run = game_over(rocket)
    draw()

pygame.quit()
