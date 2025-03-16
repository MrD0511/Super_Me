import pygame
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)



tiles_image = pygame.image.load(resource_path("assets/images/platform/tiles.png"))


class Mountain(pygame.sprite.Sprite):

    def __init__(self, x ,y):
        super().__init__()
        self.tiles = pygame.image.load(resource_path("assets/images/platform/tiles.png"))
        self.image = pygame.Surface((96,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.image.fill((0, 140, 250))
        self.image.blit(self.get_tile(32, 32, 32, 32), (32, 32))
        self.image.blit(self.get_tile(32*2, 32, 32, 32), (0, 32))
        self.image.blit(self.get_tile(32*3, 32, 32, 32), (32, 0))
        self.image.blit(self.get_tile(32*4, 32, 32, 32), (64, 32))

    def get_tile(self, x, y, width, height):

        tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

        tile_surface.blit(self.tiles, (0,0) , (x,y,height,width) )

        return tile_surface