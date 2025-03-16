import pygame
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)


tiles = pygame.image.load(resource_path("assets/images/platform/tiles.png"))

# To get the tile
def get_tile( x, y, width, height):
    tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

    tile_surface.blit(tiles, (0,0) , (x,y,height,width) )

    return tile_surface


# Cloud Class
class Cloud(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((160, 64), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.image.blit(get_tile(32*10, 0, 32, 32), (0,0))
        self.image.blit(get_tile(32*9, 0, 32, 32), (0, 32))
        self.image.blit(get_tile(32*8, 0, 32, 32), (32, 0))
        self.image.blit(get_tile(32*7, 0, 32, 32), (32, 32))
        self.image.blit(get_tile(32*8, 0, 32, 32), (64, 0))
        self.image.blit(get_tile(32*7, 0, 32, 32), (64, 32))
        self.image.blit(get_tile(32*8, 0, 32, 32), (96, 0))
        self.image.blit(get_tile(32*7, 0, 32, 32), (96, 32))
        self.image.blit(get_tile(32*12, 0, 32, 32), (128, 0))
        self.image.blit(get_tile(32*11, 0, 32, 32), (128, 32))

    def update(self):
        self.rect.x -= 1


# Small cloud class
class Small_Cloud(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32*3,32*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.image.blit(get_tile(32*10, 0, 32, 32), (0, 0))
        self.image.blit(get_tile(32*8, 0, 32, 32), (32, 0))
        self.image.blit(get_tile(32*12, 0, 32, 32), (64, 0))
        self.image.blit(get_tile(32*9, 0, 32, 32), (0, 32))
        self.image.blit(get_tile(32*7, 0 ,32, 32), (32, 32))
        self.image.blit(get_tile(32*11, 0, 32, 32), (64, 32))