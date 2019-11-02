import pygame
from Config import BLACK, PLATFORM_IMAGE, PLATFORM_SIZE


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Platform, self).__init__()
        self.position = pos
        self.image = pygame.Surface(PLATFORM_SIZE).convert_alpha()  # creating of the platform
        sprite = pygame.image.load(PLATFORM_IMAGE)
        sprite = pygame.transform.scale(sprite, self.image.get_size())
        self.image.blit(sprite, (0, 0))
        self.rect = self.image.get_rect()
