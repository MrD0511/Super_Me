import pygame
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)


tiles = pygame.image.load(resource_path("assets/images/platform/tiles.png"))

def get_tile( x, y, width, height):
    tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

    tile_surface.blit(tiles, (0,0) , (x,y,height,width) )

    return tile_surface

class Bush(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32*5, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0, 140, 250))

        self.image.blit(get_tile(32*5, 32, 32, 32), (0, 0))
        self.image.blit(get_tile(32*7, 32 ,32, 32), (32, 0))
        self.image.blit(get_tile(32*7, 32 ,32, 32), (64, 0))
        self.image.blit(get_tile(32*7, 32 ,32, 32), (96, 0))
        self.image.blit(get_tile(32*6, 32, 32, 32), (128, 0))

class Small_Bush(pygame.sprite.Sprite):

        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((32*3, 32))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.image.fill((0, 140, 250))

            self.image.blit(get_tile(32*5, 32, 32, 32), (0, 0))
            self.image.blit(get_tile(32*7, 32 ,32, 32), (32, 0))
            self.image.blit(get_tile(32*6, 32, 32, 32), (64, 0))
    
