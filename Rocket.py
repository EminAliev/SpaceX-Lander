import time
import pygame


class Rocket:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.color = color
        self.acceleration = False  # ускорение
        self.startAcceleration = time.time()
        self.fuel = 1000
        self.speed = speed

    def move_up(self):
        self.y = self.y + 2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, screen):
        width, height = screen.get_size()
        if (self.x < width - self.width) and (self.x > 0) and (self.y > 0) and (self.y < height - self.height):
            print(self.speed[1])
            self.y += self.speed[1] + 1
            self.x += self.speed[0]
        elif self.y < height - self.height:
            self.speed = [0, 1]

    def x_speed_plus(self, speed):
        self.speed[0] += speed

    def y_speed_plus(self, speed):
        self.speed[1] += speed
