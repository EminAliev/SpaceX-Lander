import pygame
import random

from Config import *
from Interface import Interface
from Menu import Menu
from Platform import Platform
from Rocket import Rocket


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        if FULLSCREEN:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.items = [(WIDTH / 2 - 200, HEIGHT * 0.75, u"Game", GRAY, WHITE, 0),
                      (WIDTH / 2 + 100, HEIGHT * 0.75, u"Quit", GRAY, WHITE, 1),
                      (WIDTH / 2 - 300, HEIGHT * 0.75, u"Restart", GRAY, WHITE, 0),
                      (WIDTH / 2 - 300, HEIGHT * 0.75, u"Continue", GRAY, WHITE, 0)]
        self.menu = Menu(self.screen, [self.items[0], self.items[1]])
        self.restart_menu = Menu(self.screen, [self.items[2], self.items[1]])
        self.pause_menu = Menu(self.screen, [self.items[3], self.items[1]])
        self.level = 1
        self.score = 0
        self.fps_clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 8))  # creating of the rocket
        self.platform = Platform((random.randint(WIDTH / 10, WIDTH - WIDTH / 8), HEIGHT - 100))

        self.all_sprites.add(self.rocket)
        self.all_sprites.add(self.platform)

        self.playersprite = pygame.sprite.RenderClear(self.rocket)
        self.platfomrsprite = pygame.sprite.RenderClear(self.platform)

        self.background = pygame.image.load(BACKGROUND_IMAGE_LEVEL_1)
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)

        self.sadElon = pygame.image.load(SAD_ELON).convert_alpha()
        self.happyElon = pygame.image.load(HAPPY_ELON).convert_alpha()

        self.sadElon = pygame.transform.scale(self.sadElon, ELON_SIZE)
        self.happyElon = pygame.transform.scale(self.happyElon, ELON_SIZE)

        self.interface = Interface(SCREEN_SIZE, self.screen)

    def start(self):

        self.menu.show_menu_window()
        self.launch_game()

    def launch_game(self):

        while self.running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rocket.angle_speed = -ANGLE
                    if event.key == pygame.K_RIGHT:
                        self.rocket.angle_speed = +ANGLE
                    if event.key == pygame.K_UP:
                        if self.rocket.fuel > 0:
                            self.rocket.gas = True
                    if event.key == pygame.K_ESCAPE:
                        self.pause_menu.show_menu_window()
                        # pygame.key.set_repeat(1, 1)
                        # pygame.mouse.set_visible(False)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.rocket.gas = False
                    if event.key == pygame.K_RIGHT:
                        self.rocket.angle_speed = 0
                    if event.key == pygame.K_LEFT:
                        self.rocket.angle_speed = 0

            self.game_over()
            self.game_win()
            self.draw()

    def quit_action(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

    def draw(self):

        self.playersprite.update()
        self.rocket.update()

        self.screen.blit(self.background, (0, 0))

        self.platfomrsprite.draw(self.screen)
        pygame.draw.rect(self.screen, BLACK,
                         (self.platform.rect[0], self.platform.rect[1] + self.platform.rect.height / 4, 3, 3))
        self.playersprite.draw(self.screen)

        Interface.render(self.interface, self.score, 0, 0, "SCORE: ")
        Interface.render(self.interface, abs(round(self.rocket.move_direction[0], 2)), 0, 50, "HORIZONTAL SPEED: ")
        Interface.render(self.interface, abs(round(self.rocket.move_direction[1], 2)), 0, 100, "VERTICAL SPEED: ")
        Interface.render(self.interface, round(self.rocket.fuel), 0, 150, "FUEL: ")
        Interface.render(self.interface, self.level, WIDTH - 100, 0, "LEVEL: ")

        pygame.display.update()

    def game_over(self):
        if (self.rocket.position[0] - self.rocket.rect.width / 2) < 0 \
                or (self.rocket.position[0] + self.rocket.rect.width / 2) > WIDTH \
                or (self.rocket.position[1] - self.rocket.rect.height / 2) < 0 \
                or (self.rocket.position[1] + self.rocket.rect.height / 2) > (HEIGHT - 100):
            self.screen.fill(BLACK)
            self.screen.blit(self.sadElon, (0, HEIGHT - ELON_SIZE[1]))
            font = pygame.font.SysFont(FONT, 40)
            for i in range(180):
                self.fps_clock.tick(GAME_FPS)
                self.screen.blit(font.render("You lose", False, RED), (WIDTH / 2, HEIGHT / 2))
                pygame.display.update()
            self.restart_menu.show_menu_window()
            self.restart()

    def restart(self):
        self.__init__()
        self.launch_game()

    # def continue

    def game_win(self):
        if (((self.rocket.rect[1] + self.rocket.rect.height) > (self.platform.rect[1] + self.platform.rect.height / 4))
                and (self.rocket.position[0] > self.platform.position[0]
                     and self.rocket.position[0] + self.rocket.rect.width < self.platform.position[
                         0] + self.platform.rect.width)
                and abs(self.rocket.move_direction[0]) < 0.1
                and abs(self.rocket.move_direction[1]) < 0.4)\
                and abs(self.rocket.angle) < 10:
            self.screen.blit(self.happyElon, (0, HEIGHT - ELON_SIZE[1]))
            font = pygame.font.SysFont(FONT, 40)
            for i in range(180):
                self.fps_clock.tick(GAME_FPS)
                self.screen.blit(font.render("You won", False, GREEN), (WIDTH / 2, HEIGHT / 2))
                pygame.display.update()
            self.pause_menu.show_menu_window()
            self.level += 1
            self.score += self.level * self.rocket.fuel
            self.reinit()
            self.launch_game()

    def reinit(self):
        pygame.init()
        self.running = True
        if FULLSCREEN:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.items = [(WIDTH / 2 - 200, HEIGHT * 0.75, u"Game", GRAY, WHITE, 0),
                      (WIDTH / 2 + 100, HEIGHT * 0.75, u"Quit", GRAY, WHITE, 1),
                      (WIDTH / 2 - 300, HEIGHT * 0.75, u"Restart", GRAY, WHITE, 0),
                      (WIDTH / 2 - 300, HEIGHT * 0.75, u"Continue", GRAY, WHITE, 0)]
        self.menu = Menu(self.screen, [self.items[0], self.items[1]])
        self.restart_menu = Menu(self.screen, [self.items[2], self.items[1]])
        self.pause_menu = Menu(self.screen, [self.items[3], self.items[1]])
        self.fps_clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 8))  # creating of the rocket
        self.platform = Platform((random.randint(WIDTH / 10, WIDTH - WIDTH / 8), HEIGHT - 100))

        self.all_sprites.add(self.rocket)
        self.all_sprites.add(self.platform)

        self.playersprite = pygame.sprite.RenderClear(self.rocket)
        self.platfomrsprite = pygame.sprite.RenderClear(self.platform)

        self.background = pygame.image.load(BACKGROUND_IMAGE_LEVEL_1)
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)

        self.sadElon = pygame.image.load(SAD_ELON).convert_alpha()
        self.happyElon = pygame.image.load(HAPPY_ELON).convert_alpha()

        self.sadElon = pygame.transform.scale(self.sadElon, ELON_SIZE)
        self.happyElon = pygame.transform.scale(self.happyElon, ELON_SIZE)

        self.interface = Interface(SCREEN_SIZE, self.screen)

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

