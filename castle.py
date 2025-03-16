import pygame
import os

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    outpath = os.path.join(base_path, relative_path)
    return outpath

tiles_image = pygame.image.load(resource_path("assets/images/platform/tiles.png"))


# To get the tile
def get_tile( x, y, width, height):

    tile_surface = pygame.Surface((height,width), pygame.SRCALPHA)

    tile_surface.blit(tiles_image, (0,0) , (x,y,height,width) )

    return tile_surface

# Castle class
class Castle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((160,160), pygame.SRCALPHA)     # In this SRCALPHA adds the taransparent colour to the suface
        # It helps blending the surface to blend in the scene
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        # Generating the castle
        self.image.blit(get_tile(32*12, 32, 32, 32), (0, 96))
        self.image.blit(get_tile(32*12, 32, 32, 32), (32, 96))
        self.image.blit(get_tile(32*12, 32, 32, 32), (96, 96))
        self.image.blit(get_tile(32*12, 32, 32, 32), (128, 96))

        self.image.blit(get_tile(32*12, 32, 32, 32), (0, 128))
        self.image.blit(get_tile(32*12, 32, 32, 32), (32, 128))
        self.image.blit(get_tile(32*12, 32, 32, 32), (96, 128))
        self.image.blit(get_tile(32*12, 32, 32, 32), (128, 128))

        self.image.blit(get_tile(32*11, 32, 32, 32), (64, 96))
        self.image.blit(get_tile(32*10, 32, 32, 32), (64, 128))

        self.image.blit(get_tile(32*3, 64, 32, 32), (0, 64))
        self.image.blit(get_tile(32*2, 64, 32, 32), (32, 64))
        self.image.blit(get_tile(32*2, 64, 32, 32), (64, 64))
        self.image.blit(get_tile(32*2, 64, 32, 32), (96, 64))
        self.image.blit(get_tile(32*3, 64, 32, 32), (128, 64))

        self.image.blit(get_tile(0, 64, 32, 32), (32, 32))
        self.image.blit(get_tile(32*12, 32, 32, 32), (64, 32))
        self.image.blit(get_tile(32, 64, 32, 32), (96, 32))

        self.image.blit(get_tile(32*3, 64, 32, 32), (32, 0))
        self.image.blit(get_tile(32*3, 64, 32, 32), (64, 0))
        self.image.blit(get_tile(32*3, 64, 32, 32), (96, 0))










