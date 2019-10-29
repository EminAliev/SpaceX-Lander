import time
import pygame
from pygame.math import Vector2


class Rocket(pygame.sprite.Sprite):

    def __init__(self, speed, gravity_val=(0, 0.01), pos=(0, 0)):
        super(Rocket, self).__init__()
        size = (24, 28)  # Create "wrapper" for image
        self.image = pygame.Surface(size)
        sprite = pygame.image.load("test-sprite-24x28.png").convert_alpha()  # load sprite
        self.image.blit(sprite, (0, 0))
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.position = Vector2(pos)
        self.move_direction = Vector2(0, 0)
        self.shift_direction = Vector2(0, -1)
        self.speed = speed
        self.angle = 0
        self.angle_speed = 0
        self.x, self.y = pos
        self.width, self.height = size
        self.gas = False
        self.gravity_val = gravity_val

    def x_speed_plus(self, speed):
        self.speed[0] += speed

    def y_speed_plus(self, speed):
        self.speed[1] += speed

    def gravity(self):
        self.move_direction += Vector2(self.gravity_val)

    def update(self):
        if self.angle_speed != 0:
            # Rotate the direction vector and then the image.
            self.shift_direction.rotate_ip(self.angle_speed)
            self.angle += self.angle_speed
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            # Update the position vector and the rect.
        if self.gas:
            self.move_direction += self.shift_direction * self.speed
        self.gravity()
        self.position += self.move_direction * 1
        self.rect.center = self.position

    def shift(self, speed):
        self.move_direction += self.shift_direction * self.speed
