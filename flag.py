import pygame
import os

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)

# This is for the pillar
class Pillar(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        
        self.image = pygame.image.load(resource_path('assets/images/flag_pillar.png'))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.flag = Flag(x + 10, self.image.get_height() - 235)     # I hardcoded it

    def update(self):                                                           # when mario collides with flag. which means game ended.
        if self.flag.flag_moving and self.flag.rect.y < self.rect.y + 240:
            self.flag.rect.y += 5  # Move flag down slowly

# Flag class
class Flag(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()
        
        self.image = pygame.transform.flip(pygame.image.load(resource_path('assets/images/flag.png')), True, False)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.flag_moving = False

