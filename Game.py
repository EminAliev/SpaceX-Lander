import pygame
import random

from Config import *
from Interface import Interface
from Menu import Menu
from Form import Form
from Platform import Platform
from Rocket import Rocket

""" Decorator, that creates of main window of the game, sets menu items, initializes different types of menu, 
sprites and backgrounds, initializes interface """


def init_window():
    def my_decorator(function):

        def wrapper(self):
            pygame.init()
            self.running = True

            func = function(self)

            if FULLSCREEN:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                self.screen = pygame.display.set_mode(SCREEN_SIZE)

            self.items = [(WIDTH / 2 - 200, HEIGHT * 0.75, u"Game", GRAY, WHITE, 0),
                          (WIDTH / 2 + 100, HEIGHT * 0.75, u"Quit", GRAY, WHITE, 1),
                          (WIDTH / 2 - 300, HEIGHT * 0.75, u"Restart", GRAY, WHITE, 0),
                          (WIDTH / 2 - 300, HEIGHT * 0.75, u"Continue", GRAY, WHITE, 0),
                          (WIDTH / 2 - 300, HEIGHT * 0.75, u"sada", GRAY, WHITE, 0)]

            self.fps_clock = pygame.time.Clock()

            self.menu = Menu(self.screen, [self.items[0], self.items[1]])
            self.restart_menu = Menu(self.screen, [self.items[2], self.items[1]])
            self.pause_menu = Menu(self.screen, [self.items[3], self.items[1]])
            self.record = Form(self.screen, [self.items[2], self.items[1]])

            self.all_sprites = pygame.sprite.Group()
            self.rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 8))  # creating of the rocket
            self.platform = Platform((random.randint(WIDTH / 10, WIDTH - WIDTH / 8), HEIGHT - 100))

            self.all_sprites.add(self.rocket)
            self.all_sprites.add(self.platform)

            self.player_sprite = pygame.sprite.RenderClear(self.rocket)
            self.platform_sprite = pygame.sprite.RenderClear(self.platform)

            self.background = pygame.image.load(BACKGROUND[random.randint(0, len(BACKGROUND) - 1)])
            self.background = pygame.transform.scale(self.background, SCREEN_SIZE)

            self.sadElon = pygame.image.load(SAD_ELON).convert_alpha()
            self.sadElon = pygame.transform.scale(self.sadElon, ELON_SIZE)

            self.happyElon = pygame.image.load(HAPPY_ELON).convert_alpha()
            self.happyElon = pygame.transform.scale(self.happyElon, ELON_SIZE)

            self.gas_rocket = pygame.image.load(ROCKET_LAUNCHER_GAS_IMAGE).convert_alpha()
            self.gas_rocket = pygame.transform.scale(self.gas_rocket, ROCKET_LAUNCHER_SIZE)

            self.interface = Interface(SCREEN_SIZE, self.screen)

            return func

        return wrapper

    return my_decorator


""" Main class of game logic """


class Game:

    @init_window()
    def __init__(self):

        self.level = 1
        self.score = 0

    """ Opens start menu and then launch main loop """

    def start(self):

        self.menu.show_menu_window()
        self.launch_game()

    """ Launches game loop """

    def launch_game(self):

        while self.running:

            self.fps_clock.tick(GAME_FPS)

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
            self.save_score()

    def quit_action(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

    """ Draws full frame: background, rocket, platform and interface"""

    def draw(self):

        self.player_sprite.update()
        self.rocket.update()

        self.screen.blit(self.background, (0, 0))

        self.platform_sprite.draw(self.screen)

        if self.rocket.gas:
            rocket_image = pygame.transform.rotate(self.gas_rocket, -self.rocket.angle)

            self.screen.blit(rocket_image, self.rocket.rect)
        else:
            self.player_sprite.draw(self.screen)

        Interface.render(self.interface, round(self.score), MARGIN, MARGIN, "SCORE: ")
        Interface.render(self.interface, abs(round(self.rocket.move_direction[0], 2)), MARGIN, MARGIN * 2, "HORIZONTAL SPEED: ")
        Interface.render(self.interface, abs(round(self.rocket.move_direction[1], 2)), MARGIN, MARGIN * 3, "VERTICAL SPEED: ")
        Interface.render(self.interface, round(self.rocket.fuel, 2), MARGIN, MARGIN * 4, "FUEL: ")
        Interface.render(self.interface, self.level, WIDTH * 0.9, MARGIN, "LEVEL: ")

        pygame.display.update()

    """ Fully restarts game with setting score and level to default values """

    def restart(self):
        self.__init__()
        self.launch_game()

    """ Checks if rocket is out of the bounds or drowned, if it is, shows dead screen and opens menu """

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
                self.screen.blit(font.render("You lose", False, RED), (WIDTH * 0.45, HEIGHT / 2))
                pygame.display.update()
            self.save_score()
            self.record.show_menu_window()
            self.restart()

    """ Checks if rocket is on the right position and have right angle with speed to confirm that rocket landed """

    def game_win(self):
        if (((self.rocket.rect[1] + self.rocket.rect.height) > (self.platform.rect[1] + self.platform.rect.height / 4))
            and (self.rocket.position[0] > self.platform.position[0]
                 and self.rocket.position[0] + self.rocket.rect.width < self.platform.position[
                     0] + self.platform.rect.width)
            and abs(self.rocket.move_direction[0]) < 0.1
            and abs(self.rocket.move_direction[1]) < 0.4) \
                and abs(self.rocket.angle) < 5:
            self.screen.blit(self.happyElon, (0, HEIGHT - ELON_SIZE[1]))
            font = pygame.font.SysFont(FONT, 40)
            for i in range(180):
                self.fps_clock.tick(GAME_FPS)
                self.screen.blit(font.render("You won", False, GREEN), (WIDTH * 0.45, HEIGHT / 2))
                pygame.display.update()
            self.pause_menu.show_menu_window()
            self.recreate_game_pole()
            self.launch_game()
            self.save_score()

    """ Recreates game window with saving current level and score values """

    @init_window()
    def recreate_game_pole(self):
        self.level += 1
        self.score += self.level * self.rocket.fuel

    """ Saves score to score.txt file """

    def save_score(self):
        file = open('score.txt', 'w')

        file.write(str(self.score))

        file.close()
