import pygame

import Interface
from Config import ANGLE, SPEED, GRAVITY_VECTOR, BACKGROUND_IMAGE_LEVEL_1, BLACK, FONT, GAME_FPS, RED
from Game import SCORE, rocket, WIDTH, SCREEN_SIZE, HEIGHT, GREEN, YELLOW
from Menu import Menu
from Platform import Platform
from Rocket import Rocket


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.game = Menu(self.screen, self.items)
        self.level = 1
        self.running = True
        self.score = 0
        self.fps_clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 8))  # creating of the rocket
        self.platform = Platform((WIDTH / 2, HEIGHT - 100))
        self.all_sprites.add(rocket)
        self.all_sprites.add(self.platform)
        self.playersprite = pygame.sprite.RenderClear(rocket)
        self.platfomrsprite = pygame.sprite.RenderClear(self.platform)
        self.background = pygame.image.load(BACKGROUND_IMAGE_LEVEL_1)
        self.background = pygame.transform.scale(self.background, SCREEN_SIZE)

    def start(self):
        items = [(WIDTH / 2 - 200, HEIGHT / 2, u"Game", GREEN, YELLOW, 0),
                 (WIDTH / 2 + 100, HEIGHT / 2, u"Quit", GREEN, YELLOW, 1)]
        self.game.menu(self.screen, items)

    def gameloop(self):
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
                        if rocket.fuel > 0:
                            self.rocket.gas = True
                    if event.key == pygame.K_ESCAPE:
                        self.game.menu()
                        pygame.key.set_repeat(1, 1)
                        pygame.mouse.set_visible(False)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.rocket.gas = False
                    if event.key == pygame.K_RIGHT:
                        self.rocket.angle_speed = 0
                    if event.key == pygame.K_LEFT:
                        self.rocket.angle_speed = 0

    def draw(self):
        self.playersprite.update()
        rocket.update()

        self.screen.blit(self.background, (0, 0))

        self.platfomrsprite.draw(self.screen)
        pygame.draw.rect(self.screen, BLACK,
                         (self.platform.rect[0], self.platform.rect[1] + self.platform.rect.height / 4, 3, 3))
        self.playersprite.draw(self.creen)
        pygame.display.update()

    def render_text_info(self):
        interface = Interface(SCREEN_SIZE, self.screen)
        Interface.render(interface, SCORE, 0, 0, "SCORE: ")
        Interface.render(interface, abs(round(rocket.move_direction[0], 2)), 0, 50, "HORIZONTAL SPEED: ")
        Interface.render(interface, abs(round(rocket.move_direction[1], 2)), 0, 100, "VERTICAL SPEED: ")
        Interface.render(interface, round(rocket.fuel), 0, 150, "FUEL: ")
        Interface.render(interface, self.level, WIDTH - 100, 0, "LEVEL: ")
        pygame.display.update()

    def game_over(self):
        if (rocket.position[0] - rocket.rect.width / 2) < 0 \
                or (rocket.position[0] + rocket.rect.width / 2) > WIDTH \
                or (rocket.position[1] - rocket.rect.height / 2) < 0 \
                or (rocket.position[1] + rocket.rect.height / 2) > (HEIGHT - 100):
            self.screen.fill(BLACK)
            font = pygame.font.SysFont(FONT, 40)
            for i in range(180):
                self.fps_clock.tick(GAME_FPS)
                self.screen.blit(font.render("You lose", False, RED), (WIDTH / 2, HEIGHT / 2))
                pygame.display.update()
            self.game.menu()

    def game_win(self):
        if (((rocket.rect[1] + rocket.rect.height) > (self.platform.rect[1] + self.platform.rect.height / 4))
                and (rocket.position[0] > self.platform.position[0]
                     and rocket.position[0] + rocket.rect.width < self.platform.position[0] + self.platform.rect.width)
                and abs(rocket.move_direction[0]) < 0.1
                and abs(rocket.move_direction[1]) < 0.4):
            self.screen.fill(BLACK)
            font = pygame.font.SysFont(FONT, 40)
            for i in range(180):
                self.fps_clock.tick(GAME_FPS)
                self.screen.blit(font.render("You won", False, RED), (WIDTH / 2, HEIGHT / 2))
                pygame.display.update()
            self.game.menu()


if __name__ == '__main__':
    Game().start()
