import pygame
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)


class Tube(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path('assets/images/tube.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    