import pygame
from Config import ROCKET_LAUNCHER_IMAGE, ROCKET_LAUNCHER_SIZE
from pygame.math import Vector2


class Rocket(pygame.sprite.Sprite):

    def __init__(self, speed, gravity_val=(0, 0.01), pos=(0, 0)):
        super(Rocket, self).__init__()
        # size = (50, 20)  # Create "wrapper" for image
        self.image = pygame.Surface(ROCKET_LAUNCHER_SIZE, flags=pygame.SRCALPHA)  # Crete surface for the rocket
<<<<<<< HEAD
        print(self.image.get_alpha())
=======
>>>>>>> 57763962c216d281139f4edd55c293d3e853df42
        sprite = pygame.image.load(ROCKET_LAUNCHER_IMAGE).convert_alpha()  # load sprite
        sprite = pygame.transform.scale(sprite, self.image.get_size())  # scale sprite
        self.image.blit(sprite, (0, 0))  # Fill surface with image
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.position = Vector2(pos)
        self.move_direction = Vector2(0.1, 0)  # Direction of spawn movement
        self.shift_direction = Vector2(0, -1)  # Default engine thrust
        self.speed = speed  # Speed of engine
        self.angle = 0  # Default angle
        self.angle_speed = 0
        self.fuel = 100
        self.gas = False
        self.gravity_val = gravity_val  # Value of planet's gravity
        self.crashed = False

    """ Method that plays role of gravity """
    def gravity(self):
        self.move_direction += Vector2(self.gravity_val)

    """ Updating rocket's attributes """
    def update(self):
        if self.angle_speed != 0:
            """ Rotate the direction vector and then the image. """
            if not abs(self.angle + self.angle_speed) > 90:
                self.shift_direction.rotate_ip(self.angle_speed)
                self.angle += self.angle_speed
                self.image = pygame.transform.rotate(self.original_image, -self.angle)
                self.rect = self.image.get_rect(center=self.rect.center)
            """ Update the position vector and the rect. """
        if self.gas:
            self.move_direction += self.shift_direction * self.speed
            self.fuel -= 0.01
        self.gravity()
        self.position += self.move_direction * 1
        self.rect.center = self.position



